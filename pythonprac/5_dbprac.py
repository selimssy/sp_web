# ############## pymongo 기본 코드 + 보안강화 ####################

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.dhof2yp.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

doc = {
    'name':'bob',
    'age': 27
}

db.users.insert_one(doc)