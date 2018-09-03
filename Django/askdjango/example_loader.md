app_directory.Loader

4개의 app 생성 시 setting 파일의 INSTALLED_APPS 리스트에 등록된 template을 로드 한다.
accounts/template
blog/template
dojo/template
shop/template

그리고, 
filesystem.Loader

TEMPLATES 의 DIR에 등록된 경로를 로드 한다.
askdjanog/templates/ # 프로젝트 레벨에서 쓸 템플릿 파일을 넣어두는 것

만약

render(request,"post_list.html") 을 view.py 파일에서 호출하게 되면
위의 5개의 template 순서대로 찾게 된다. app 하위에 html 파일의 이름이 중복 되면 안된다. 보통 prefix로 만든다.

그래서 Directory 개념을 만들어서 구분하게 되면 prefix를 만들 필요가 없다.

