#blog/models.py
from django.db import models


class Post(models.Model):
#    title = models.CharField(max_length=100,
#    choices=(
#        ('제목1','제목 1레이블'), #('저장될 값','UI에 보여질 레이블')
#        ('제목2','제목 2레이블'),
#        ('제목3','제목 3레이블'),
#    ))#길이 제한이 있는 문자열
    title = models.CharField(max_length=100, help_text='제목 입력..100내')#, verbose_name='제목')
    content = models.TextField() # 길이 제한이 없는 문자열
    created_at = models.DateTimeField(auto_now_add=True) #최초 저장될 때 시간
    update_at = models.DateTimeField(auto_now=True) # 해당 레코드가 갱신이 될때 마다 일시 저장
# Create your models here.
