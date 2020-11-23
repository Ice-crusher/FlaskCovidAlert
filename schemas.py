from extensions import ma
from models import NearbyTouch


class NearbyTouchSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = NearbyTouch
        #fields = ('id', 'userId', 'time', 'geographicCoordinateX', 'geographicCoordinateY', 'nearbyIdentifier', 'opponentId')


nearby_touch_schema = NearbyTouchSchema()
