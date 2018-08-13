#blog/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list), #시작과 끝이라는 뜻(최상위 주소) # 함수 자체를 넘겨준 것
]
