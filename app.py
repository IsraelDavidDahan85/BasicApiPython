import os

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import logging

from models.userModel import db
from routers.index import api_bp
from logger.log import log
app = Flask(__name__)
ma = Marshmallow(app)

default_log = logging.getLogger('werkzeug')
default_log.setLevel(logging.ERROR)


# applies CORS headers to all routes, enabling resources to be accessed
CORS(app, origins="*")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/python'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    log.info('Starting server...')
    app.run(host="0.0.0.0", port=5555)
