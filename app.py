from flask import Flask, render_template, request, session
from extensions import db
from extensions import ma
from datetime import timedelta
import os
from routes.main import main
import time

app = Flask(__name__)

ENV = 'dev'

if ENV == 'prod':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///./sql_app.db"
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "super_secret_key"

app.register_blueprint(main)

db.init_app(app)
with app.app_context():
    db.create_all()
    
# Init schemas
#nearby_touch_schema = NearbyTouchSchema()
# nearby_touches_schema = NearbyTouchSchema(many=True)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
