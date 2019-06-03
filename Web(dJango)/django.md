# Web Application (django)

- Dynamic web
- 프레임워크 사용

### Django - How?

``` :bash
-M(model) : 데이터를 관리
-T(Template) : 사용자가 보는 화면
-V(View) : 사용자의 요청의 오는곳
```



--- django 프로젝트를 생성하면 반드시 실행해야 하는 과정 ---

1. 장고 시작하기

```bash
$ django-admin startproject intro . # 현재 디렉토리에 intro라는 이름으로 장고를 시작해라
$ python manage.py runserver  # 서버 실행
```

2. 장고 파일 의미

```bash
urls.py : url 연결 ( 요청을 확인하고 요청이 어디로 가야하는지 / views로 넘겨줌)
wsgi.py : 배포에 필요
db.sqlite3 : 데이터베이스
---------
pages app 만들고
---------
admin.py : 관리자 페이지
apps.py : app의 정보가 담김
models.py : 데이터베이스 혹은 앱에서 사용되는 모델들이 정의되는 곳
test.py : test 코드 작성
views.py : cotroller와 같은 곳. 뭔가 구현?
```

3. app 생성

```bash
$ python manage.py startapp pages  # pages라는 app 생성
```

4. setting.py에 app 등록 (우리가 만든 app을 반드시 등록 해야함)

```bash
INSTALLED_APPS = [

	# 추가        # apps.py에 있는 class 이름
    'pages.apps.PagesConfig',  
    
--

LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'

```



1. urls.py

2. views.py

3. templates 디렉토리 만들고 여기에 views.py 에서 요청하는 html 파일 넣기



- 변수 routing

```bash
<views.py>
def greeting(request, name):
    return render(request,'greeting.html', {'name': name})

<urls.py>
path('greeting/<str:name>/', views.greeting),
```

