from extensions import db
import time


class NearbyTouch(db.Model):
    __tablename__ = 'NearbyTouches'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.String(100), index=True)
    time = db.Column(db.BigInteger, nullable=False)
    geographicCoordinateX = db.Column(db.Float, nullable=True)
    geographicCoordinateY = db.Column(db.Float, nullable=True)
    opponentId = db.Column(db.String(100), nullable=False)

    def __init__(self, userId, opponentId,
                 geographicCoordinateX=None, geographicCoordinateY=None):
        self.userId = userId
        self.time = time.time_ns()
        self.geographicCoordinateX = geographicCoordinateX
        self.geographicCoordinateY = geographicCoordinateY
        self.opponentId = opponentId


class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), index=True)
    instanceId = db.Column(db.String(100), unique=True)
    userId = db.Column(db.String(100), unique=True)
    fcmToken = db.Column(db.String(200), index=True)

    def __init__(self, email, instanceId, userId, fcmToken):
        self.email = email
        self.instanceId = instanceId
        self.userId = userId
        self.fcmToken = fcmToken


class Sick(db.Model):
    __tablename__ = 'Sick'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.String(100), nullable=False)
    time = db.Column(db.BigInteger, nullable=False)

    def __init__(self, userId):
        self.userId = userId
        self.time = time.time_ns()


