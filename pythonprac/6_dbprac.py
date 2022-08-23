# ############## pymongo 기본 코드 ####################


from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.dhof2yp.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta



# 1. 삽입

'''
doc = {
    'name' : 'jenny',
    'age' : 20
}


db.users.insert_one(doc)    # 통상적으로 이렇게 쓴다
'''






'''
db.users.insert_one({'name':'bobby', 'age' : 27})
db.users.insert_one({'name':'john', 'age' : 20})
db.users.insert_one({'name':'ann', 'age' : 20})
'''








# 2.조회


# 2-1) 다보기(find)
all_users = list(db.users.find({}, {'_id':False}))   # 조건은 없고, '_id'는 출력 안하겠다

for user in all_users:
    print(user)


print() #줄바꿈




# 2_2) 'name'이 'bobby'인 유저를 찾아 'age'를 출력  (find_one)
user = db.users.find_one({'name':'bobby'}, {'_id':False})
print(user['age'])  # 27






# 3)수정(업데이트)

'''
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
'''





# 4) 삭제
'''
db.users.delete_one({'name':'jenny'})
'''







# ################### 요약 ###################(실행금지...!!)


# 저장 - 예시
doc = {'name':'kimmy','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
all_users = list(db.users.find({},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})