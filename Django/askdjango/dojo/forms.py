from django import forms
from .models import Post


'''class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_3_valitator]) # 함수 자체를 validators로 넘겨준다.
    content = forms.CharField(widget=forms.Textarea) #다른 이유는 models.py 의 경우 데이터에 대한 interface 이므로.. 다름
    '''

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        #fields = '__all__'
        fields = ['title','content']




