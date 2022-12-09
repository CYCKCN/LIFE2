
from pymongo.mongo_client import MongoClient
from utils import User, Account
    
def connection(dbname):
    addr = "mongodb+srv://LIFE2:lifeforever@life2.dwrako7.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(addr)
    db = client[dbname]
    return db