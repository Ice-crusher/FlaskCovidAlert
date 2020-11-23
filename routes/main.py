from flask import Blueprint, render_template, request, redirect, url_for, session, json
from models import NearbyTouch, User
from extensions import db
# from schemas import nearby_touch_schema
import time


main = Blueprint('main', __name__)

TIME_7DAYS_NS = 7 * 24 * 60 * 60 * (10**9)

@main.route('/nearbyTouch', methods=['POST'])
def nearby_touch():
    userId = request.json['userId']
    geographicCoordinateX = request.json.get('geographicCoordinateX', None)
    geographicCoordinateY = request.json.get('geographicCoordinateY', None)
    # nearbyIdentifier = request.json['nearbyIdentifier']#delete
    opponentId = request.json['opponentId'] #change to id
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
    # todo get all touched device by this user in last 7 days
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

    # todo send FCM to previous touched devices

    return json.dumps({"Founded events": str(len(list)),
                       "Founded users": str(usersFCM)}), 200


@main.route("/login", methods=['POST'])
def login():
    # todo create or update user data
    userId = request.json['userId']
    fcmToken = request.json['fcmToken']

    localUser = User.query.filter_by(userId=userId).first()

    if localUser is None:
        user = User(userId=userId,
                    fcmToken=fcmToken)
        db.session.add(user)
        db.session.commit()

        return json.dumps({"message": "User created."}), 200
    else:
        
        localUser.userId = userId
        localUser.fcmToken = fcmToken
        db.session.commit()
        return json.dumps({"message": "User updated."}), 200

# @main.route('/logout', methods=['DELETE'])
# def logout():
#     session.pop('user', None)
#     return json.dumps({"message": "Successful logout."}), 200
