#dojo/views.py
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#def mysum(request,x,y=0,z=0):
#    #request: HttpRequset <<- 함수 정의 할 때 무조건 선언한다.
#    return HttpResponse(int(x)+100+int(y)+int(z))

def mysum(request,numbers):
    #request: HttpRequset <<- 함수 정의 할 때 무조건 선언한다.
    #result = sum(map(int,numbers.split("/"))) #빈문자열이 들어 올 경우 int 변환 에러 발생
    #return HttpResponse(result)
    result = sum(map(lambda s: int(s or 0), numbers.split("/"))) #빈문자열이 들어 올 경우 int 변환 에러 발생
    # 빈물자열은 거짓
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse ('안녕하세요. {}. {} 살이네요'.format(name,age))
    