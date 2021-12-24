from flask_restful import Resource, reqparse
import sqlite3
from flask_jwt import jwt_required

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This feild cant be kept empty')
    @jwt_required()
    def get(self, name):
        row= self.find_by_name(name)
        if row:
            return {'item':row[1],'price':row[2]}, 200
        return {"message":"Item not found"}, 404

    @classmethod
    def find_by_name(cls,name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "select * from items where name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        return row

    def post(self, name):
        if self.find_by_name(name):
            return {'message':"itemalready exists"}, 400

        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        try:
            Item.insert_by_name(item)
        except:
            return {"message":"An error occured in inserting the item"},500
        return item, 201

    @classmethod
    def insert_by_name(cls,item):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "insert into items values (NULL,?,?)"
        cursor.execute(query, (item['name'], item['price']))
        connection.commit()
        connection.close()
    @classmethod
    def update(cls, item):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "update items set price =? where name =?"
        cursor.execute(query, (item['price'], item['name']))
        connection.commit()
        connection.close()

    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query= "delete from items where name= ?"
        cursor.execute(query,(name,))
        connection.commit()
        connection.close()
        return {'message': "item deleted"}


    def put(self, name):
        data = Item.parser.parse_args()
        # print(data['another'])
        item = Item.find_by_name(name)
        updated_item = {'name':name, 'price':data['price']}
        if not item:
            try:
                self.insert_by_name(updated_item)
            except:
                return {'message':"some error in inserting"}
        else:
            try:
                self.update(updated_item)
            except Exception as e:
                return {'message': "some error in update {}".format(e)}
        return updated_item, 200


class AllItems(Resource):

    def get(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "select * from items"
        result= cursor.execute(query)

        all_items = []
        for row in result:
            all_items.append({'name':row[1],"price":row[2]})
        connection.close()
        return {'items': all_items}
