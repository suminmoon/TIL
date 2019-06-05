# DB modeling

#### models.py

``` bash
- DB 관련한 작업을 수행
- class 생성하기

# 클래스 변수 = DB의 필드를 나타냄
- title = models.CharField(max_length=10)
- content = models.TextField() # text 가 길 때 사용
- created_at = models.DateTimeField(auto_now_add=True)  
                                # auto_new_add : 객체 최초 1회 생성 시점의 시간을 담겠다.
- updated_at = models.DateTimeField(auto_now=True)  
                                 # auto_new : 지금 작업을 할 때 시점
```



- settings.py

```bash
USE_TZ = False  # True : templates 나 form 에서만 위에서 정의한 타임존이 적용/ False 는 DB 등 모든 작업에 적용이 됨
```



#### models.py 만들고 반드시 해야할 것!

```bash
migrations : DB의 '설계도' 가 저장이 되는 곳
=> 설계도 : models.py가 작성이 되었고 이걸 토대로 DB를 만들라 하는 것 

$ python manage.py makemigrations 
=> models.py 작성이 끝났으면 이 모델들을 사용할 것이고 이 모델을 DB에 저장할거니 설계도를 그려줘!
```

