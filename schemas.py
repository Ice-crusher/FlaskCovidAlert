from extensions import ma, mainWebSiteUrl
from models import NearbyTouch
from models import User


class NearbyTouchSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = NearbyTouch
        #fields = ('id', 'userId', 'time', 'geographicCoordinateX', 'geographicCoordinateY', 'nearbyIdentifier', 'opponentId')


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ("email", "userId", "fcmToken", "mainWebSiteUrl")
        model = User


nearby_touch_schema = NearbyTouchSchema()
user_schema = UserSchema()
