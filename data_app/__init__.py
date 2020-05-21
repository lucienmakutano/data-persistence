try:
    from flask import Flask
    from flask_restful import Api
    from flask_sqlalchemy import SQLAlchemy
except Exception:
    print('could not load the modules')

app = Flask(__name__)
api = Api(app)

app.config.from_pyfile('settings.py')
app.config['SQLALCHEMY_DATABASE_URI'] = f'{ app.config.get('CLEARDB_DATABASE_URL ) }'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

from data_app import data_api
