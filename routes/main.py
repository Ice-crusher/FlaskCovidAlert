from flask import Blueprint, render_template, request, redirect, url_for, session, json
from models import NearbyTouch, User
from extensions import db
# from schemas import nearby_touch_schema
import time


main = Blueprint('main', __name__)

TIME_7DAYS_NS = 7 * 24 * 60 * 60 * (10**9)

@main.route('/nearbyTouch', methods=['POST'])
def nearby_touch():
    androidId = request.json['androidId']
    geographicCoordinateX = request.json.get('geographicCoordinateX', None)
    geographicCoordinateY = request.json.get('geographicCoordinateY', None)
    nearbyIdentifier = request.json['nearbyIdentifier']
    opponentNearbyIdentifier = request.json['opponentNearbyIdentifier']
    near_touch = NearbyTouch(androidId=androidId,
                             geographicCoordinateX=geographicCoordinateX,
                             geographicCoordinateY=geographicCoordinateY,
                             nearbyIdentifier=nearbyIdentifier,
                             opponentNearbyIdentifier=opponentNearbyIdentifier)
    db.session.add(near_touch)
    db.session.commit()

    return json.dumps({"message": "Stay safe!"}), 200
    # return nearby_touch_schema.jsonify(near_touch)

@main.route('/sick', methods=['POST'])
def sick():
    androidId = request.json['androidId']
    timestamp = time.time_ns()
    # todo get all touched device by this user in last 7 days
    list = NearbyTouch.query.filter(
        (NearbyTouch.androidId == androidId),
        (NearbyTouch.time > (timestamp - TIME_7DAYS_NS))
    ).all()

    for item in list:


    return json.dumps({"message": str(len(list))}), 200
    # todo send FCM to previous touched devices


@main.route("/login", methods=['POST'])
def login():
    # todo create or update user data
    androidId = request.json['androidId']
    fcmToken = request.json['fcmToken']

    localUser = User.query.filter_by(androidId=androidId).first()

    if localUser is None:
        user = User(androidId=androidId,
                    fcmToken=fcmToken)
        db.session.add(user)
        db.session.commit()

        return json.dumps({"message": "User created."}), 200
    else:
        localUser.androidId = androidId
        localUser.fcmToken = fcmToken
        db.session.commit()
        return json.dumps({"message": "User updated."}), 200

@main.route('/logout', methods=['DELETE'])
def logout():
    session.pop('user', None)
    return json.dumps({"message": "Successful logout."}), 200
