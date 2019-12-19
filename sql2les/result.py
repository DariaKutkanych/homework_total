from flask import Flask, request
from flask_restful import Api, Resource
import sqlite3

from Database.sql2les.functions import get_data, post_data, get_statistics, get_comments, get_post_comments,\
    get_posts_with_data

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
        posts_query = request.args.get("query", None)
        if posts_query:
            return get_posts_with_data(posts_query)
        else:
            return get_data("Posts")

    def post(self):
        data = request.get_json()
        return post_data("Posts", data), 205


class PostsByUsers(Resource):
    def get(self, user_id):
        return get_data("Posts", user_id)


class Statistics(Resource):
    def get(self):
        return get_statistics()


class Comments(Resource):
    def get(self, user_id):
        return get_comments(user_id)


class PostComments(Resource):
    def get(self, post_id):
        return get_post_comments(post_id)


class PostsThatContain(Resource):
    def get(self, word):
        return get_posts_with_data(word)


api.add_resource(Statistics, "/posts/statistics")
api.add_resource(Comments, "/users/<int:user_id>/comments")
api.add_resource(PostComments, "/posts/<int:post_id>/comments")
api.add_resource(Posts, "/posts")

api.add_resource(Users, "/users")
api.add_resource(PostsByUsers, "/users/<int:user_id>/posts")


if __name__ == "__main__":
    app.run(debug=True)
