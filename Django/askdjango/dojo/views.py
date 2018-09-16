#dojo/views.py
import os
from django.shortcuts import get_object_or_404, redirect,render
from django.http import HttpResponse, JsonResponse
from .forms import PostForm
from .models import Post
# Create your views here.

#def mysum(request,x,y=0,z=0):
#    #request: HttpRequset <<- 함수 정의 할 때 무조건 선언한다.
#    return HttpResponse(int(x)+100+int(y)+int(z))

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            #방법1)
            #post = Post()
            #post.title= form.cleaned_data['title']
            #post.Content= form.cleaned_data['content']
            #post.save()
            #return redirect('/dojo/')
            
            #방법2)
            #post = Post(title= form.cleaned_data['title'],
            #Content= form.cleaned_data['content'])
            #post.save()
            #return redirect('/dojo/')
            
            #방법3)
            #post = Post.objects.create(title= form.cleaned_data['title'],
            #Content= form.cleaned_data['content'])
            
            #방법4)
            form.cleaned_data
            post = Post.objects.create(**form.cleaned_data) #DB에 저장하기
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/success.url/')
        else:
            form.errors
    else:
        form = PostForm()
    return render(request,'dojo/post_form.html',{
        'form': form
    })

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES,instance=post)
        if form.is_valid():
            #방법1)
            #post = Post()
            #post.title= form.cleaned_data['title']
            #post.Content= form.cleaned_data['content']
            #post.save()
            #return redirect('/dojo/')
            
            #방법2)
            #post = Post(title= form.cleaned_data['title'],
            #Content= form.cleaned_data['content'])
            #post.save()
            #return redirect('/dojo/')
            
            #방법3)
            #post = Post.objects.create(title= form.cleaned_data['title'],
            #Content= form.cleaned_data['content'])
            
            #방법4)
            form.cleaned_data
            post = Post.objects.create(**form.cleaned_data) #DB에 저장하기
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/success.url/')
        else:
            form.errors
    else:
        form = PostForm(instance=post)
    return render(request,'dojo/post_form.html',{
        'form': form
    })


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


