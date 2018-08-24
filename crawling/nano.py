import requests
import mechanicalsoup
from bs4 import BeautifulSoup

browser = mechanicalsoup.StatefulBrowser()

browser.open('https://member.ssg.com/member/popup/popupLogin.ssg?originSite=http%3A//emart.ssg.com&t=&gnb=login') # request.get
browser.select_form('form#loginForm')
browser['mbrLoginId'] = 'ckh6666'
browser['password'] = 'sky019293'
browser.submit_selected()


response = requests.get('https://pay.ssg.com/myssg/orderInfo.ssg?viewType=Ssg')
html = response.text
print(html)


   #get_parmas = {'username':'kwanhyun','password':'sky019293'}
   #response = s.post('https://github.com/login',data=get_parmas)
   #
   #redirect_cookie = response.headers['Set-Cookie']
   #headers = {'referer':'https://github.com/session'}
   ##print(redirect_cookie)
   ##print(response.status_code)

   #post_pg = s.get('https://github.com/settings/emails',headers=headers)
   #htmlMain = post_pg.text
   #print(htmlMain)
   #soup = BeautifulSoup(htmlMain,'html.parser')
   #print(soup.text)