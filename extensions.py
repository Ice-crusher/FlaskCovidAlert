from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

db = SQLAlchemy()
ma = Marshmallow()

fcmApiKey = os.environ.get('FCM_API_KEY')
# fcmApiKey = "AAAAujOMeAE:APA91bEVG034XkqY-UGjen3iLkkj1XUEkb7yEfudgKj5qyabvdD-gUJkeAg3tPPuXPAZRgGAuDY2eDTbfZ5NPqF__OchVvfnlBTvxz5EwM1XLifLxm528pygZCRCSRT2RQs5C3hOXJgQ"
mainWebSiteUrl = "https://www.gov.pl/web/koronawirus/wiadomosci"

def model_exists(model_class):
    engine = db.get_engine(bind=model_class.__bind_key__)
    return model_class.metadata.tables[model_class.__tablename__].exists(engine)
