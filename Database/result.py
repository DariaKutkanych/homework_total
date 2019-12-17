from flask import Flask, request
from flask_restful import Api, Resource
import sqlite3

from Database.api import get_data, post_data

app = Flask(__name__)
api = Api(app)


class Users(Resource):
    def get(self):
        return get_data("Users")

    def post(self):
        data = request.get_json()
        return post_data("Users", data), 205


class Posts(Resource):
    def get(self):
        return get_data("Posts")

    def post(self):
        data = request.get_json()
        return post_data("Posts", data), 205


class PostsByUsers(Resource):
    def get(self, user_id):
        return get_data("Posts", user_id)


api.add_resource(Users, "/users")
api.add_resource(Posts, "/posts")
api.add_resource(PostsByUsers, "/users/<int:user_id>/posts")


if __name__ == "__main__":
    app.run(debug=True)
