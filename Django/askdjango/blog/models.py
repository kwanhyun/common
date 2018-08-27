#blog/models.py
import re
from django.db import models
from django.forms import ValidationError


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')


class Post(models.Model):
#    title = models.CharField(max_length=100,
#    choices=(
#        ('제목1','제목 1레이블'), #('저장될 값','UI에 보여질 레이블')
#        ('제목2','제목 2레이블'),
#        ('제목3','제목 3레이블'),
#    ))#길이 제한이 있는 문자열
    STATUS_CHOICES = (
        ('d','Draft'),
        ('p','Published'),
        ('w','Withdrawn'),
    )
    title = models.CharField(max_length=100, help_text='제목 입력..100내')#, verbose_name='제목')
    content = models.TextField() # 길이 제한이 없는 문자열
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=100, blank=True,validators=[lnglat_validator],help_text='경도/위도 포맷으로 입력')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True) #최초 저장될 때 시간
    update_at = models.DateTimeField(auto_now=True) # 해당 레코드가 갱신이 될때 마다 일시 저장
# Create your models here.
    def __str__(self):
        return self.title

"""
makemigrations: 마에그레이션 파일 생성
migrate: 실제 마이그레이션 진행
이미 진행된 Migrate 파일은 지우지 않는다.!!!
"""
