from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def model_exists(model_class):
    engine = db.get_engine(bind=model_class.__bind_key__)
    return model_class.metadata.tables[model_class.__tablename__].exists(engine)
