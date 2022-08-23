import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.dhof2yp.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작

# 순위, 제목, 별점 가져오기

#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img (순위)
#old_content > table > tbody > tr:nth-child(2) > td.title > div > a (제목)
#old_content > table > tbody > tr:nth-child(2) > td.point (별점)




movies = soup.select('#old_content > table > tbody > tr')

for movie in movies:
    a = movie.select_one('td.title > div > a')
    if a != None:   # 이거 미리 안잡아주면 에러난다ㅠ
        title = a.text
        rank = movie.select_one('td:nth-child(1) > img')['alt']
        star = movie.select_one('td.point').text
        doc = {
            'title':title,
            'rank':rank,
            'star':star
        }
        # db.movies.insert_one(doc)    # 이거 실행할 때마다 계속 db에 삽입된다...







