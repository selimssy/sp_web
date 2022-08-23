################ 웹크롤링 기본 셋팅 ###################


import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작
#print(soup)    # 전체 html 출력

# 해당 요소 개발자모드 -> copy -> copy selector


#################### 하나만 가져올 때(select_one) ########################
title = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
print(title)  #해당 태그 출력  # <a href="/movie/bi/mi/basic.naver?code=195758" title="헌트">헌트</a>

# 해당 텍스트만 출력하고 싶으면 .text 붙인다
print(title.text)  # 헌트


# 만약 href값 가져오고 싶으면
print(title['href'])    # /movie/bi/mi/basic.naver?code=195758




#################### 여러 개 다 가져올 때(select) ########################
#old_content > table > tbody > tr:nth-child(2) > td.title > div > a
#old_content > table > tbody > tr:nth-child(3) > td.title > div > a

# 공통 태그까지 긁어서 select에 넣는다!
movies = soup.select('#old_content > table > tbody > tr')
#<tr></tr>   (다음줄)   <tr></tr>   (다음줄)   <tr></tr>  .... 에서  <tr></tr> 얘네들을 다 배열에 넣어 가져오는 것!

print(movies)   # 배열 형태로 출력



# 이제 각각의 tr 태그 안에 있는 최종 태그 a 태그를 가져와야

'''
for movie in movies:
    a = movie.select_one('td.title > div > a')
    print(a)   # a 태그들 모두 출력(가로 선에 해당하는 None 포함해서)
'''


for movie in movies:
    a = movie.select_one('td.title > div > a')
    if a != None:
        print(a.text)


