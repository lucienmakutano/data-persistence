try:
    from flask import Flask
    from flask_restful import Api
    from flask_sqlalchemy import SQLAlchemy
    from flask_login import LoginManager
    import secrets
except ModuleNotFoundError:
    print('could not load the modules')

app = Flask(__name__)
api = Api(app)

app.config.from_pyfile('settings.py')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://bc1b301810a782:a9287c9e@us-cdbr-east-06.cleardb.net/heroku_0691c8fd14cb558'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = secrets.token_hex(16)


db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_message = "your session has expired"
login_manager.login_view = 'login'
login_manager.login_message_category = 'warning'

from data_app import data_api
