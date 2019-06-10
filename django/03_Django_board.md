#### GET 요청과 POST 의 차이는?

```
- 서버에 무언가를 전달할 때 사용하는 방식
- GET 은 주소줄에 ?값 뒤에 쌍으로 이어붙고 POST 는 숨겨진다.
- GET은 가져오는 것이고, POST 는 수행(작성, 수정 등) 하는 것이다.
- GET은 select 적인 성향, 서버의 값이나 상태 등을 바꾸지 않음
- POST 는 서버의 값이나 상태 등을 바꾸기 위해 사용


<django-board/new.html>
    <form action="/boards/create/" method="post">

```



#### GET 과 POST 를 나누는 것이 'RESTFUL' 하게 나누는 것?

```bash
- REST의 정의
“Representational State Transfer” 의 약자
자원을 이름(자원의 표현)으로 구분하여 해당 자원의 상태(정보)를 주고 받는 모든 것을 의미한다.
즉, 자원(resource)의 표현(representation) 에 의한 상태 전달

- 자원(resource)의 표현(representation)
자원: 해당 소프트웨어가 관리하는 모든 것
-> Ex) 문서, 그림, 데이터, 해당 소프트웨어 자체 등
자원의 표현: 그 자원을 표현하기 위한 이름
-> Ex) DB의 학생 정보가 자원일 때, ‘students’를 자원의 표현으로 정한다.

- 상태(정보) 전달
데이터가 요청되어지는 시점에서 자원의 상태(정보)를 전달한다.
JSON 혹은 XML를 통해 데이터를 주고 받는 것이 일반적이다.

```





#### CSRF 토큰?

``` bash
CSRF 공격(Cross Site Request Forgery)은 웹 어플리케이션 취약점 중 하나로 인터넷 사용자(희생자)가 자신의 의지와는 무관하게 공격자가 의도한 행위(수정, 삭제, 등록 등)를 특정 웹사이트에 요청하게 만드는 공격입니다.

게시글을 작성할 때 게시자에게 특정 값 (토큰)을 가지고 있게 해서, 그 사람이 토큰 값을 보여주면 글을 쓸 수 있는 권한을 줌
=> django가 해줌
	<setting.py - MIDDLEWARE 부분에서>
    'django.middleware.csrf.CsrfViewMiddleware', 이 로직이 수행

---
<django-board/new.html>
	<form action="/boards/create/" method="post">
	{% csrf_token %} 추가

```



