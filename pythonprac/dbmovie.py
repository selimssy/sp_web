from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.dhof2yp.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta




# mongoDB 연습



# 영화제목 '가버나움'의 평점을 가져오기
movie1 = db.movies.find_one({'title':'가버나움'})
print(movie1['star'])



# '가버나움'의 평점과 같은 평점의 영화 제목들을 가져오기
movies = list(db.movies.find({'star': movie1['star']}))

for movie in movies:
    print(movie['title'])



'''  (해답에는 이렇게)
target_movie = db.movies.find_one({'title':'가버나움'})
target_star = target_movie['star']

movies = list(db.movies.find({'star':target_star}))
'''






# '가버나움' 영화의 평점을 0으로 만들기
db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})   # 평점도 문자다ㅠ
print(movie1['star'])