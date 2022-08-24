import requests
from bs4 import BeautifulSoup


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')


#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis (제목)
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number (순위)
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis (가수)


# strip() 함수 : 좌우 공백 제거 함수

# strip() 함수 : 양 끝의 공백 모두 제거
# lstrip() 함수 : 왼쪽 공백 제거
# rstrip() : 오른쪽 공백을 제거



# 문자열[a:b] : a 부터 b 직전까지(a ~ b-1)


songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for song in songs:
    title = song.select_one('td.info > a.title.ellipsis').text.strip()
    rank = song.select_one('td.number').text[0:2].strip()
    artist = song.select_one('td.info > a.artist.ellipsis').text
    print(rank, title, artist)


# for song in songs:
#     a = song.select_one('td.info > a.title.ellipsis')
#     if a.span == None:
#         title = a.select_one('td.info > a.title.ellipsis').text.strip()
#     else:
#         title = a