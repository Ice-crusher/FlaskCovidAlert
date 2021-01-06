from extensions import app, db, ma, ENV
from extensions import db
import os
from routes.main import main
import flask_monitoringdashboard as dashboard

dashboard.bind(app)  # add analytics to "/dashboard"

if ENV == 'dev':
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


if __name__ == '__main__':
    app.run()
