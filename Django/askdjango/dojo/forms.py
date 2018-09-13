from django import forms


def min_length_3_valitator(value):
    if len(value) <3:
        raise forms.validators('3글자 이상 입력해주세요.')

class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_3_valitator]) # 함수 자체를 validators로 넘겨준다.
    content = forms.CharField(widget=forms.Textarea) #다른 이유는 models.py 의 경우 데이터에 대한 interface 이므로.. 다름




