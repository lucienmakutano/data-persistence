from data_app import api, app, db
import urllib.request
from flask_restful import Resource, reqparse
import json
from data_app.model import Users

parser = reqparse.RequestParser()
parser.add_argument('email', type=str, required=True, help="You must provide your email")
parser.add_argument('name', type=str, required=True, help="Your name is required")
parser.add_argument('username', type=str, required=True, help="Username is required")


def isThisUserInTheDb(users, user):
    for u in users:
        if u.name == user.name:
            return {"message": "this name is already taken"}, 203

        elif u.email == user.email:
            return {"message this email is already taken"}, 203

        elif u.username == user.username:
            return {"message": "this username is already taken"}, 203

    return False


@app.route('/')
def index():
    return """
        <h3>Welcome</h3>
        <ul>
          <li>go to /populate to register 10 users</li>
          <li>make a DELETE request to /delete to delete the last user</li>
          <li>make a POST request to /signup to add a new user</li>
        </ul>
    """


class Persistence(Resource):
    def get(self):
        url = 'http://jsonplaceholder.typicode.com/users'
        users = urllib.request.urlopen(url)

        if not users.getcode() == 200:
            return {"message": "resource not found"}, 404

        json_data_users = json.loads(users.read())

        for i in range(len(json_data_users)):
            user = Users(
                email=json_data_users[i]['email'],
                username=json_data_users[i]['username'],
                name=json_data_users[i]['name']
            )

            db.session.add(user)

        db.session.commit()

        return {"message": "users created"}, 201


class DeleteLastUser(Resource):
    def delete(self):
        user = Users.query.order_by(Users.id.desc()).first()

        if user is None:
            return {"message": "The data store is empty"}, 404

        db.session.delete(user)
        db.session.commit()

        return {"message": "deleted"}, 200


class SignUp(Resource):

    def __init__(self):
        self.name = parser.parse_args().get('name')
        self.email = parser.parse_args().get('email')
        self.username = parser.parse_args().get('username')

    def post(self):
        user = Users(username=self.username, name=self.name, email=self.email)

        users = Users.query.all()

        isUser = isThisUserInTheDb(users, user)

        if isUser:
            return isUser

        db.session.add(user)

        db.session.commit()

        return {"message": "user created"}, 201


api.add_resource(Persistence, '/populate')
api.add_resource(DeleteLastUser, '/delete')
api.add_resource(SignUp, '/signup')
