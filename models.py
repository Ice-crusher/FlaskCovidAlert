from extensions import db
import time


class NearbyTouch(db.Model):
    __tablename__ = 'NearbyTouch'
    id = db.Column(db.Integer, primary_key=True)
    androidId = db.Column(db.String(100), unique=True)
    time = db.Column(db.Integer, nullable=False)
    geographicCoordinateX = db.Column(db.Float, nullable=True)
    geographicCoordinateY = db.Column(db.Float, nullable=True)
    nearbyIdentifier = db.Column(db.Integer, nullable=False)
    opponentNearbyIdentifier = db.Column(db.Integer, nullable=False)

    def __init__(self, androidId, nearbyIdentifier, opponentNearbyIdentifier,
                 geographicCoordinateX=None, geographicCoordinateY=None):
        self.androidId = androidId
        self.time = time.time_ns()
        self.geographicCoordinateX = geographicCoordinateX
        self.geographicCoordinateY = geographicCoordinateY
        self.nearbyIdentifier = nearbyIdentifier
        self.opponentNearbyIdentifier = opponentNearbyIdentifier


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    androidId = db.Column(db.String(100), unique=True)
    fcmToken = db.Column(db.String(100), unique=True)

    def __init__(self, androidId, fcmToken):
        self.androidId = androidId
        self.fcmToken = fcmToken


class Sick(db.Model):
    __tablename__ = 'sick'
    id = db.Column(db.Integer, primary_key=True)
    androidId = db.Column(db.String(100), unique=True)
    time = db.Column(db.Integer, nullable=False)
    nearbyIdentifier = db.Column(db.Integer, nullable=False)

    def __init__(self, androidId, nearbyIdentifier, timeNs):
        self.androidId = androidId
        self.time = timeNs
        self.nearbyIdentifier = nearbyIdentifier


