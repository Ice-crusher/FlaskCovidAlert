from extensions import ma, mainWebSiteUrl
from models import NearbyTouch
from models import User


class NearbyTouchSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        # fields = ('userId', 'time', 'geographicCoordinateX', 'geographicCoordinateY', 'nearbyIdentifier', 'opponentId')
        model = NearbyTouch
        created_at = ma.auto_field(dump_only=True)


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ("email", "userId", "fcmToken", "mainWebSiteUrl")
        model = User


nearby_touch_schema = NearbyTouchSchema()
nearby_touches_schema = NearbyTouchSchema(many=True)
user_schema = UserSchema()
