from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, storename):
        store = StoreModel.find_by_name(storename)
        if store:
            return store.json()
        return {"message":"Store not found"}, 404
    def post(self, storename):
        if StoreModel.find_by_name(storename):
            return {"message":"Store already exists"}, 400
        store = StoreModel(storename)
        try:
            store.upsert()
        except:
            return {"message":"An error in store.post"}, 500

        return store.json(), 201

    def delete(self, storename):
        store =  StoreModel.find_by_name(storename)
        if store:
            store.delete_db()
        return {"message":"store deleted if it was there"}

class StoreList(Resource):
    def get(self):
        return {"stores":[store.json() for store in StoreModel.query.all()]}