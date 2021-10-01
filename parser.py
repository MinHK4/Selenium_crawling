## parser.py
import requests
from bs4 import BeautifulSoup
import json
import os

## HTTP GET Request
req = requests.get('https://beomi.github.io/beomi.github.io_old/')

## HTML 소스 가져와서 Soup 객체에 parsing 처리 후에
## 원하는 정보(글 제목 = h3 > a)들만 따로 저장
html = req.text
soup = BeautifulSoup(html, 'html.parser')
my_titles = soup.select(
  'h3 > a' 
  )

# 받아온 html 소스 데이터를 바탕으로
# 글 이름: key, 글 주소: value 형식으로 딕셔너리 저장
data = {}
for title in my_titles:
  data[title.text] = title.get('href')

# 원하는 위치, 파일명으로 저장
with open(os.path.join('.', 'result.json'), 'w+') as json_file:
  json.dump(data, json_file)