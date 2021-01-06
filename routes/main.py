from flask import Blueprint, render_template, request, redirect, url_for, session, json
from models import NearbyTouch, User, Sick
from extensions import db, mainWebSiteUrl, cache
import heatmap_render
import fcm_notifications
import uuid
import numpy as np
import time

TIME_7DAYS_NS = 7 * 24 * 60 * 60 * (10**9)

main = Blueprint('main', __name__)

@main.route('/nearbyTouch', methods=['POST'])
def nearby_touch():
    userId = request.json['userId']
    geographicCoordinateX = request.json.get('geographicCoordinateX', None)
    geographicCoordinateY = request.json.get('geographicCoordinateY', None)
    opponentId = request.json['opponentId']
    near_touch = NearbyTouch(userId=userId,
                             geographicCoordinateX=geographicCoordinateX,
                             geographicCoordinateY=geographicCoordinateY,
                             # nearbyIdentifier=nearbyIdentifier,
                             opponentId=opponentId)
    db.session.add(near_touch)
    db.session.commit()

    return json.dumps({"message": "Stay safe!"}), 200
    # return nearby_touch_schema.jsonify(near_touch)

@main.route('/sick', methods=['POST'])
def sick():
    userId = request.json['userId']
    timestamp = time.time_ns()

    sick_inst = Sick(userId=userId)
    db.session.add(sick_inst)
    db.session.commit()

    # get all touched device by this user in last 7 days
    events = NearbyTouch.query.filter(
        (NearbyTouch.userId == userId),
        (NearbyTouch.time > (timestamp - TIME_7DAYS_NS))
    ).all()

    usersFCM = set()

    for event in events:
        userToSend = User.query.filter(
            (User.userId == event.opponentId)
        ).first()
        if userToSend is not None:
            usersFCM.add(userToSend.fcmToken)
    fcm_notifications.sendNotifications(list(usersFCM))

    return json.dumps({"Founded events": str(len(events)),
                       "Founded fcms": str(usersFCM)}), 200


@main.route("/login", methods=['POST'])
def login():
    # create or update user data
    email = request.json['email']
    fcmToken = request.json['fcmToken']

    localUser = User.query.filter_by(email=email).first()

    if localUser is None:
        user = User(email=email,
                    userId=str(uuid.uuid4()),
                    fcmToken=fcmToken)
        db.session.add(user)
        db.session.commit()
        return {
            "userId": user.userId,
            "email": user.email,
            "fcmToken": user.fcmToken,
            "mainWebSiteUrl": mainWebSiteUrl
        }
        # return user_schema.dump(user)
    else:  # update fcm token
        localUser.fcmToken = fcmToken
        db.session.commit()
        return {
            "userId": localUser.userId,
            "email": localUser.email,
            "fcmToken": localUser.fcmToken,
            "mainWebSiteUrl": mainWebSiteUrl
        }
        # return user_schema.dump(localUser)


@main.route('/', defaults={'path': ''})
@main.route('/<path:path>')
def catch_all(path):
    return redirect(url_for('main.statistics'))


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/statistics', methods=['GET'])
@cache.cached(timeout=60)  # cached for 60 seconds
def statistics():
    print("Cached time is:" + str(time.time_ns()))
    touches_data, infected_touches_data = get_heatmap_data()
    return heatmap_render.get_map_html(touches_data=touches_data, infected_touches_data=infected_touches_data)


#  return lat, lon, magnitude
def get_heatmap_data():
    #  todo group with magnitude
    touches_data = []

    # all touches events
    timestamp = time.time_ns()
    touches_events = NearbyTouch.query.filter(
        (NearbyTouch.time > (timestamp - TIME_7DAYS_NS))
    ).all()

    # sick incidents reported by users
    sick_events = Sick.query.filter(
        (Sick.time > (timestamp - TIME_7DAYS_NS))
    ).all()

    infected_touches_data = []
    infected_user_ids = set()
    for sick_event in sick_events:
        infected_user_ids.add(sick_event.userId)

    for touch_event in touches_events:
        # x, y, magnitude
        touches_data.append([touch_event.geographicCoordinateX, touch_event.geographicCoordinateY, 1])
        # complexity of search is O(n), because search complexity through set() equals O(1) (HashTable)
        if touch_event.userId in infected_user_ids:
            infected_touches_data.append([touch_event.geographicCoordinateX, touch_event.geographicCoordinateY, 2])


    # print(type(sick_events))

    data = (
            np.random.normal(size=(100, 3)) *
            np.array([[1, 1, 1]]) +
            np.array([[48, 5, 1]])
    ).tolist()

    data1 = (
            np.random.normal(size=(100, 3)) *
            np.array([[1, 1, 1]]) +
            np.array([[48, 5, 1]])
    ).tolist()
    return data, data1



# @main.route('/logout', methods=['DELETE'])
# def logout():
#     session.pop('user', None)
#     return json.dumps({"message": "Successful logout."}), 200
