from flask_restful import Resource, reqparse
import sqlite3
from flask_jwt import jwt_required
from models.item_model import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This feild cant be kept empty')
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help='This feild cant be kept empty')
    @jwt_required()
    def get(self, name):
        row= ItemModel.find_by_name(name)
        if row:
            return row.json(), 200
        return {"message":"Item not found"}, 404


    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message':"itemalready exists"}, 400

        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'], data['store_id'])
        try:
            item.upsert()
        except:
            return {"message":"An error occured in inserting the item"},500
        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_db()
        return {'message': "item deleted"}


    def put(self, name):
        data = Item.parser.parse_args()
        # print(data['another'])
        item = ItemModel.find_by_name(name)

        if not item:
            try:
                item = ItemModel(name,data['price'],data['store_id'])
            except:
                return {'message':"some error in inserting"}
        else:
            try:
                item.price = data['price']
            except Exception as e:
                return {'message': "some error in update {}".format(e)}
        return item.json(), 200


class AllItems(Resource):

    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}
