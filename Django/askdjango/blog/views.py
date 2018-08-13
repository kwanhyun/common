from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html') #view 에서 template 지정하는 형식
# blog/templates/blog/post_list.html
