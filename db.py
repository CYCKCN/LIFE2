
from pymongo.mongo_client import MongoClient
from utils import User, Account
    
def connection(dbname):
    addr = "mongodb+srv://LIFE2:lifeforever@life2.dwrako7.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(addr)
    db = client[dbname]
    return db

class AccountDB():
    def __init__(self, db):
        self.db = db["account"]
    
    def findUser(self, accountEmail):
        return self.db.find_one({"accountEmail": accountEmail})

class ItemDB():
    def __init__(self, db):
        self.db = db["item"]

class OrderDB():
    def __init__(self, db):
        self.db = db["order"]

db = connection("LIFE2")
accountdb = AccountDB(db)
itemdb = ItemDB(db)
orderdb = OrderDB(db)