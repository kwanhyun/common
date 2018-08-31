#Email
import smtplib
from email.message import EmailMessage
from email.mime.application import MIMEApplication
import os

import getpass
password = getpass.getpass('Password : ')

message = EmailMessage()
message['Subject'] = '이메일 제목'
message['From'] = 'ckh6666@naver.com'
message['To'] = 'ckh6666@hanmail.net'
message.set_content(
'''
테스트 Email 입니다.
'''
)

message.add_alternative('''
    <h1>AskDjango VOD</h1>

    <img src="cid:test.jpg" />

    <ul>
        <li>test test</li>
    </ul>

''',subtype='html')

#filepath = './test.jpg'
#이미지 첨부

filepath_list = ['./test.jpg','./test1.jpg','./test2.jpg']
for filepath in filepath_list:
    with open(filepath,'rb') as f:
        filename = os.path.basename(filepath)
        cid = filename
        img_date = f.read()
        part = MIMEApplication(img_date,name=filename)
        part.add_header('Content-ID','<'+cid+'>')
        message.attach(part)


with smtplib.SMTP_SSL('smtp.naver.com',465) as server:
    server.ehlo()
    server.login('ckh6666',password)
    server.send_message(message)

print('Send Email..')