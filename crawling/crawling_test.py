import requests
from bs4 import BeautifulSoup as bs

LOGIN_INFO = {
    'username' : 'ncckh',
    'password': '5smfskfTl!'
}

with requests.session() as s:

    #first_page = s.get('https://mlogin.plaync.com/login/signin')
    #html =  first_page.text
    #soup = bs(html,'html.parser')
    #auth = soup.find('input',{'name':'app_id'})
    #print(auth['value'])
    #LOGIN_INFO = {**LOGIN_INFO, **{'app_id':auth['value']}}
    #print(LOGIN_INFO)
    '''
    login_req = s.post('https://nano.ncsoft.com/signin',data=LOGIN_INFO)
    print(login_req.status_code)
    #headers = login_req.headers['Set-Cookie']
    #headers = {
    #    'referer':'https://nano.ncsoft.com/'
    #}

    response = s.get('https://nano.ncsoft.com/')#,headers=headers)
    html = response.text
    print(html)
    
    '''

    #nano 성공

    first_page = s.get('https://nano.ncsoft.com/signin')
    html = first_page.text
    soup = bs(html,'html.parser')
    csrf = soup.find('input',{'name':'_csrf'})

    print(csrf['value'])

    LOGIN_INFO = {**LOGIN_INFO,**{'_csrf':csrf['value']}}
    print(LOGIN_INFO)

    
    login_req = s.post('https://nano.ncsoft.com/signin',data=LOGIN_INFO)
    print(login_req.status_code)
    
    
    headers = {
        'referer':'https://nano.ncsoft.com/'
    }

    response = s.get('https://nano.ncsoft.com/notice/view?no=442255',headers=headers)
    html = response.text
    print(html)

#데스크시도
'''   
    login_req = s.post('https://servicedesk.korea.ncsoft.corp',data=LOGIN_INFO,verify=False)
    print(login_req.status_code)
    
    
    #headers = {
    #    'referer':'https://servicedesk.korea.ncsoft.corp'
    #}

    response = s.get('http://servicedesk.korea.ncsoft.corp/usr/library/librarylist.aspx')
    html = response.text
    print(html)
'''
    