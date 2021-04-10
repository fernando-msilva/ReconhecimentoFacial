from pymongo import MongoClient

def conexao():
    try:
        client = MongoClient("localhost", 27017)
        db = client.spyface
        print("conexão realizada com sucesso")
        return db
    except Exception as e:
        print(e)