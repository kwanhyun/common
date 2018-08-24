import requests
from bs4 import BeautifulSoup as bs

LOGIN_INFO = {
    'login_name' : 'ckh6666',
    'password': 'cdh1063744!'
}

with requests.session() as s:

    #first_page = s.get('https://mlogin.plaync.com/login/signin')
    #html =  first_page.text
    #soup = bs(html,'html.parser')
    #auth = soup.find('input',{'name':'app_id'})
    #print(auth['value'])

    #LOGIN_INFO = {**LOGIN_INFO, **{'app_id':auth['value']}}
    #print(LOGIN_INFO)

    login_req = s.post('https://mlogin.plaync.com/login/signin',data=LOGIN_INFO)
    print(login_req.status_code)
    #headers = login_req.headers['Set-Cookie']
    headers = {
        'referer':'https://mlogin.plaync.com/'
    }

    response = s.get('https://id.plaync.com/account/main/intro',headers=headers)
    html = response.text
    print(html)

    