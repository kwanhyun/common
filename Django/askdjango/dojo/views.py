#dojo/views.py
import os
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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
    

def post_list1(request):
    name = '공유'
    return HttpResponse('''
    <h1>AskDjango</h1>
    <p>{name}</p>
    '''.format(name=name))


def post_list2(request):
    name = '공유'
    return render(request,'dojo/post_list.html',{'name':name})


def post_list3(request):
    return JsonResponse({
        'message':'Hi Python&Django',
        'itmes':['Python','AWS','AZURE','DJANGO'],
    },json_dumps_params={'ensure_ascii':False})


def excel_download(request):
    filepath = 'D:\GitRepo\common\Django\gdplev.xlsx'
    filename = os.path.basename(filepath)
    with open(filepath,'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel') # default text/html..
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response


