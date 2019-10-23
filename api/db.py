from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis

# pylint: disable=C0103
sql = SQLAlchemy()
redis = FlaskRedis()
# pylint: enable=C0103
