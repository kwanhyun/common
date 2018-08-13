'''
GET:엽서/파일업로드 불가 (BODY가 없음)
POST:소포/파일 업로드 지원
주로 사용
User-Agent / Referer를 커스텀하게 설정할 필요가 있다/ 잘못 설정할 경우 응답을 거부하기도 함.
'''
 
 
import requests

response = requests.get('https://askdjango.github.io/lv1/')
print(response)
html = response.text

print(html)

'''요청시
GET /lv1 HTTP/1.1
Host: askdjango.github.io
Connection: Keep-alive
Accept:  */*
User-Agent: Python-requests /2.14.2
accept-Encoding: gzip, deflate
(빈줄)
(Body없음)
'''

''' 응답시
HTTP/1.1 200OK
~~
~~
(빈줄)
<!doctype html>
(중략)
</htlm>
'''

print('naver webtoon')
import os
import requests
# URL 소스 : http://comic.naver.com/webtoon/detail.nhn?titleId=119874&no=1015&weekday=tue
# - 덴마. 3-12화 1. 다이크(12)

image_urls = [
    'https://image-comic.pstatic.net/webtoon/119874/1199/20180807175320_2520007e43f520197317e1ddef8028cf_IMAG01_1.jpg',
    'https://image-comic.pstatic.net/webtoon/119874/1199/20180807175320_2520007e43f520197317e1ddef8028cf_IMAG01_2.jpg',
    'https://image-comic.pstatic.net/webtoon/119874/1199/20180807175320_2520007e43f520197317e1ddef8028cf_IMAG01_3.jpg',
]
for image_url in image_urls:
    headers = {
        'Referer':'https://comic.naver.com/webtoon/detail.nhn?titleId=119874&no=1199&weekday=tue',
    } # get 인자 지정 하였으며, Dictionary 방식
    response = requests.get(image_url,headers=headers)
    image_data = response.content
    filename = os.path.basename(image_url)
    with open(filename, 'wb') as f:
        print('writing to {} ({} bytes)'.format(filename, len(image_data)))
        f.write(image_data)

print('차이점')

image_urls = [
    'https://image-comic.pstatic.net/webtoon/119874/1199/20180807175320_2520007e43f520197317e1ddef8028cf_IMAG01_1.jpg',
    'https://image-comic.pstatic.net/webtoon/119874/1199/20180807175320_2520007e43f520197317e1ddef8028cf_IMAG01_2.jpg',
    'https://image-comic.pstatic.net/webtoon/119874/1199/20180807175320_2520007e43f520197317e1ddef8028cf_IMAG01_3.jpg',
]
for image_url in image_urls:
    response = requests.get(image_url)
    image_data = response.content
    filename = os.path.basename(image_url)
    with open(filename, 'wb') as f:
        print('writing to {} ({} bytes)'.format(filename, len(image_data)))
        f.write(image_data)


'''
text 와 content의 차이

r.text is the content of the response in unicode, and r.content is the content of the response in bytes.
Presumably r.text would be preferred for textual responses, such as an HTML or XML document, and r.content would be preferred for "binary" filetypes, such as an image or PDF file.

'''


'''
HTTP 요청 Request 라이브러가 좋음

'''
import requests

#단순 GET요청
response = requests.get('https://news.naver.com/main/home.nhn')
print(response.status_code)
print(response.headers)
#html = response.text
#print(html)
print(response.headers['Content-Encoding']) #대소문자 구분이 없다
print(response.encoding)
print(response.headers['Content-Type'])

# response.content bytes형식으로 받을 경우 response.encoding으로 디코딩한다. 유니코드 형식
# 문자일 경우... html = response.text or response.content.decode('utf8')
#print(response.json()) json 형식이 아닐 경우 jsondecodeError 가 발생한다. text 형식을 json 형식으로 변환하는 것을 시리얼라즈라고 한다.
'''
response.encoding 시 'iso-8859-01' 혹은 none 으로 나올 경우 <- 캐릭터셋 지정안하여,,
이럴 경우에는 response.encoding = 'euc-kr' 식으로 직정 인코딩을 지정할 수 있다.
그리고. contents.text로 decode 하여 사용한다.
'''

#POST 요청!!!!
#Get 요청 시에는 Get인자만 가능하지만, Post요청 시에도 Get인자 요청이 가능한다.

# Get 요청은 Params / Post요청은 data or files

data = {'k1':'v1','k2':'v2'}
response = requests.post('http://httpbin.org/post',data=data)
print(response.json()) # 이건 args

get_parmas = {'k1':'v1','k2':'v2'}
response = requests.get('http://httpbin.org/get',params=get_parmas)
print(response.json()) # 이건 form

import json
json_data = {'k1':'v2','k2':[1,2,3],'name':'Ask 장고'}

json_string = json.dumps (json_data) # 사전 형식을 문자열로 변환하는 방식
response = requests.post('http://httpbin.org/post', data=json_string)

print(response.json())
print('=============')
json_string = json.dumps (json_data) # 내부적으로 문자열 변환 json.dumps를 호출한다.
response = requests.post('http://httpbin.org/post', json=json_data)
print(response.json())

print('멜론 크롤링 시작')
#import requests
#
#response12 = requests.get('http://www.genie.co.kr/chart/top200')
#result = response12.text
#
#print(result)
#셀레늄은 브라우저를 통한 자동화 이므로 개발자 도구의 Dom Tree 형태의 정보를 참고하고
#request의 경우에는 기본 html 응답에서 확인해야 하므로 페이지 소스 보기에서 정보를 확인한다.
#BeatifulSoup4가 lxml 보다 사용이 간편하다.

from bs4 import BeautifulSoup

html = '''
<ol>
<li>Never - 국민의 아들</li>
<li>New Face - Psy</li>
<ol>
....
'''
soup = BeautifulSoup(html,'html.parser')
for tag in soup.select('li'):
    print(tag.text)

# 파서 종류 : html.parser(BeatifulSoup4에서만..) / lxml (lxml을 따로 설치해야함))
# Css Selector를 사용한 크롤링이 효율적이다.


#import requests
#from bs4 import BeautifulSoup
#html = requests.get('http://www.melon.com/chart/index.htm').text
#soup = BeautifulSoup(html, 'html.parser')
#
#tag_list = soup.select('#tb_list tr .wrap_song_info a[href*=playSong]')
#for idx, tag in enumerate(tag_list, 1):
#    print(idx, tag.text)


#import requests
#from bs4 import BeautifulSoup
#html = requests.get('http://www.genie.co.kr/chart/top200').text
##print(html)
#
#soup = BeautifulSoup(html, 'html.parser')
#tag_list = soup.select('#body-content .music-list-wrap a[onclick*=fnViewArtist]')
#for id,tag in enumerate(tag_list,1):
#    print(id,tag.text)

#html parser는 닫는 테크가 없으면 잘 못 읽어온다. 그래서 lxml을 사용한다.

#이미지
#썸네일 처리: 경우에 따라서 용량을 줄이는 경우
#이미지 다운받기

import os
from PIL import Image #pillow
import requests

image_url = ('https://ee5817f8e2e9a2e34042-3365e7f0719651e5b'
             '8d0979bce83c558.ssl.cf5.rackcdn.com/python.png')
image = requests.get(image_url).content
filename = os.path.basename(image_url)
with open(filename, 'wb') as f:
    f.write(image)


from IPython.display import Image
Image(filename='python.png')




#이미지 품질 낮추기 / 다른 포맷으로 변경하기
#resize / thumbnail 차이 (비율 유지의 차이/원본 변경의 차이)
