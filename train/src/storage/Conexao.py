from pymongo import MongoClient
import os

def conexao():
    try:
        client = MongoClient(os.environ["MONGO_HOST"], 27017)
        db = client.spyface
        return db
    except Exception as e:
        print(e)