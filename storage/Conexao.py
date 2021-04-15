from pymongo import MongoClient

def conexao():
    try:
        client = MongoClient("100.26.142.187", 27017)
        db = client.spyface
        return db
    except Exception as e:
        print(e)