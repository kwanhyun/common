import requests
import mechanicalsoup
from bs4 import BeautifulSoup

browser = mechanicalsoup.StatefulBrowser()

browser.open('https://mlogin.plaync.com/login/signin') # request.get
browser.select_form('form#loginForm')
browser['login_name'] = 'ckh6666'
browser['password'] = 'cdh1063744!'
browser.submit_selected()
#print(res.status_code)

browser.launch_browser()

#response = requests.get('https://github.com/settings/emails')
#html = response.text
#print(html)


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