import requests
from bs4 import BeautifulSoup

with requests.Session() as s:
    get_parmas = {'username':'ncckh','password':'3wndThvmxm!'}
    response = s.post('https://nano.ncsoft.com',data=get_parmas)

    print(response.status_code)

    post_pg = s.get('https://nano.ncsoft.com/notice/view?no=441839')
    htmlMain = post_pg.text

    soup = BeautifulSoup(htmlMain,'html.parser')
    print(soup.text)

