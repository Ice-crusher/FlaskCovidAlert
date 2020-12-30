from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

db = SQLAlchemy()
ma = Marshmallow()

# fcmApiKey = "AAAAujOMeAE:APA91bEVG034XkqY-UGjen3iLkkj1XUEkb7yEfudgKj5qyabvdD-gUJkeAg3tPPuXPAZRgGAuDY2eDTbfZ5NPqF__OchVvfnlBTvxz5EwM1XLifLxm528pygZCRCSRT2RQs5C3hOXJgQ"
fcmApiKey = os.environ.get('FCM_API_KEY')
mainWebSiteUrl = "https://www.gov.pl/web/koronawirus/wiadomosci"
