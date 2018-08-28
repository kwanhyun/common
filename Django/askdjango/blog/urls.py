#blog/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list), #시작과 끝이라는 뜻(최상위 주소) # 함수 자체를 넘겨준 것 //빈문자열을 뜻함
    #url(r'^(?P<id>\d+)/$') <id> 변수고.. 그 변수가 \d+ <--[0-9] 사이라면?
    # 패턴이 없다면.. localhost:8000/blog/
    url(r'^(?P<id>\d+)/$', views.post_detail),


]

## urls 요청이 들어올 때마다 처음부터 끝까지 순차적으로 url 패턴 검사 한다.