#Email
import smtplib
from email.message import EmailMessage

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

    <ul>
        <li>test test</li>
    </ul>

''',subtype='html')

with smtplib.SMTP_SSL('smtp.naver.com',465) as server:
    server.ehlo()
    server.login('ckh6666',password)
    server.send_message(message)

print('Send Email..')