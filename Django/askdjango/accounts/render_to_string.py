from django.template.loader import render_to_string


message=render_to_string('accounts/signup_welcome.txt')
print(message)

'''
In [1]: from django.template.loader import render_to_string

In [2]: message=render_to_string('accounts/signup_welcome.txt',{'name':'ckh','when':'2017년 2월 28일'
   ...: })

In [3]: print(message)
안녕하세요. ckh님. ckh님께서는 2017년 2월 28일에 가입하였습니다.
감사합니다. -AskDjango

In [4]:
'''