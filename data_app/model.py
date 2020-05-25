try:
    from data_app import db, login_manager
    from flask_login import UserMixin
except ModuleNotFoundError:
    print("module not found")


@login_manager.user_loader
def user_loader(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    def __init__(self, name, email, username):
        self.name = name
        self.email = email
        self.username = username

    def __repr__(self):
        return '<Users %r %r %r %r>' % (self.id, self.name, self.username, self.email)
