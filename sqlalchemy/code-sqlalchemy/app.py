from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from resources.user import UserRegister
from resources.items import Item,AllItems
from resources.store import Store, StoreList
from alchemy import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resources/data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key = 'xmen'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, "/item/<string:name>")
api.add_resource(AllItems, "/items")
api.add_resource(UserRegister, "/register")
api.add_resource(Store, "/store/<string:storename>")
api.add_resource(StoreList, "/stores")


if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)
