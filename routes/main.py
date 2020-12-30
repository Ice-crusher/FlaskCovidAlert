from flask import Blueprint, render_template, request, redirect, url_for, session, json
from models import NearbyTouch, User, Sick
from extensions import db, mainWebSiteUrl
import fcm_notifications
import uuid
from schemas import user_schema
import time


main = Blueprint('main', __name__)

TIME_7DAYS_NS = 7 * 24 * 60 * 60 * (10**9)

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
    list = NearbyTouch.query.filter(
        (NearbyTouch.userId == userId),
        (NearbyTouch.time > (timestamp - TIME_7DAYS_NS))
    ).all()

    usersFCM = set()

    for event in list:
        userToSend = User.query.filter(
            (User.userId == event.opponentId)
        ).first()
        if userToSend is not None:
            usersFCM.add(userToSend.fcmToken)

    fcm_notifications.sendNotifications(list(usersFCM))

    return json.dumps({"Founded events": str(len(list)),
                       "Founded fcms": str(usersFCM)}), 200


@main.route("/login", methods=['POST'])
def login():
    # todo create or update user data
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

# @main.route('/logout', methods=['DELETE'])
# def logout():
#     session.pop('user', None)
#     return json.dumps({"message": "Successful logout."}), 200
