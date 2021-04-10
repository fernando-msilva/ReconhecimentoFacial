from pymongo import MongoClient

def conexao():
    client = MongoClient("localhost", 27017)
    db = client.spyface
    return db