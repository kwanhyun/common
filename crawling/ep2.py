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
    }
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