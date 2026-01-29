from pymongo import MongoClient
from .account import Account

class MongoAccountsRepository:
    def __init__(self, uri="mongodb://localhost:27017", db="bank", collection="accounts"):
        self.client = MongoClient(uri)
        self.collection = self.client[db][collection]
    def save_all(self, accounts):
        self.collection.delete_many({})
        for acc in accounts:
            self.collection.update_one(
                {"pesel": acc.pesel},
                {"$set": acc.to_dict()},
                upsert=True,
            )
    def load_all(self):
        docs = self.collection.find({})
        return [Account.from_dict(doc) for doc in docs]