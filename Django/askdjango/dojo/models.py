from django.db import models
from django import forms

# Create your models here.

#validator은 모델에 정의한다.

def min_length_3_valitator(value):
    if len(value) <3:
        raise forms.ValidationError('3글자 이상 입력해주세요.')

class Post(models.Model):
    title = models.CharField(max_length=100, validators=[min_length_3_valitator])
    content = models.TextField()
    ip = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)