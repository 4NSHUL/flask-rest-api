from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from user import UserRegister
from items import Item,AllItems
app = Flask(__name__)
app.secret_key = 'xmen'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, "/items/<string:name>")
api.add_resource(AllItems, "/items")
api.add_resource(UserRegister, "/register")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
