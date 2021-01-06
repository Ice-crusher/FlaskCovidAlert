from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_caching import Cache
import os

app = Flask(__name__)
db = SQLAlchemy()
ma = Marshmallow()
cache = Cache(config={'CACHE_TYPE': 'simple', "CACHE_DEFAULT_TIMEOUT": 300})  # default cache 5 min
cache.init_app(app)

fcmApiKey = os.environ.get('FCM_API_KEY')
ENV = os.environ.get('ENV')
mainWebSiteUrl = "https://www.gov.pl/web/koronawirus/wiadomosci"
