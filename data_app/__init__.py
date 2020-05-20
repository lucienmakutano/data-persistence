try:
    from flask import Flask
    from flask_restful import Api
    from flask_sqlalchemy import SQLAlchemy
except Exception:
    print('could not load the modules')

app = Flask(__name__)
api = Api(app)

app.config.from_pyfile('settings.py')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://bc1b301810a782:a9287c9e@us-cdbr-east-06.cleardb.net/heroku_0691c8fd14cb558'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

from data_app import data_api
