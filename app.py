import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import rq_dashboard
from utils import add_basic_auth

app = Flask(__name__)

app.config.from_object(os.getenv('APP_SETTINGS', 'config.DevelopmentConfig'))

db = SQLAlchemy(app)

if not app.config.get('TESTING'):
    add_basic_auth(rq_dashboard.blueprint,
                   os.getenv('USER', 'admin'), os.getenv('PASSWORD', '[]'))

app.register_blueprint(rq_dashboard.blueprint, url_prefix='/monitor')


@app.route('/')
def hello():
    return 'Nothing to see here. :)'


if __name__ == '__main__':

    app.run()
