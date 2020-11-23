from extensions import db
import time


class NearbyTouch(db.Model):
    __tablename__ = 'NearbyTouch'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.String(100), index=True)
    time = db.Column(db.Integer, nullable=False)
    geographicCoordinateX = db.Column(db.Float, nullable=True)
    geographicCoordinateY = db.Column(db.Float, nullable=True)
    opponentId = db.Column(db.Integer, nullable=False)

    def __init__(self, userId, opponentId,
                 geographicCoordinateX=None, geographicCoordinateY=None):
        self.userId = userId
        self.time = time.time_ns()
        self.geographicCoordinateX = geographicCoordinateX
        self.geographicCoordinateY = geographicCoordinateY
        self.opponentId = opponentId


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.String(100), unique=True)
    fcmToken = db.Column(db.String(100), unique=True)

    def __init__(self, userId, fcmToken):
        self.userId = userId
        self.fcmToken = fcmToken


class Sick(db.Model):
    __tablename__ = 'sick'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.String(100), unique=True)
    time = db.Column(db.Integer, nullable=False)
    nearbyIdentifier = db.Column(db.Integer, nullable=False)

    def __init__(self, userId, nearbyIdentifier, timeNs):
        self.userId = userId
        self.time = timeNs
        self.nearbyIdentifier = nearbyIdentifier


