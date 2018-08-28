import requests
from bs4 import BeautifulSoup as bs

LOGIN_INFO = {
    'srchDvNm' : '1795177911',
    'hmpgPwdCphd': '292513hyo!'
}

RESERVE_INFO = {
    '':'', 
    '':'',
    '':'',
    '':'',
    '':''
}

with requests.session() as s:

    login_req = s.post('https://etk.srail.co.kr/cmc/01/selectLoginForm.do',data=LOGIN_INFO)
    print(login_req.status_code)
    
    response = s.get('https://etk.srail.co.kr/main.do')
    html = response.text
    print(html)


