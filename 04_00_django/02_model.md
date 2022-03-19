# Model

[toc]

## Model

- 단일한 데이터에 대한 정보를 가짐
  - 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함
- 저장된 데이터베이스의 구조(layout)
- 장고는 모델을 통해 데이터에 접속하고 관리
- 일반적으로 각각의 model은 하나의 뎅터베이스 테이블에 매핑 됨



## Database

- 데이터베이스(DB)
  - 체계화된 데이터의 모임
- 쿼리(Query)
  - 데이터를 조회하기 위한 명령어
  - 조건에 맞는 데이터를 추출하거나 조작하는 명령어
  - 쿼리를 날린다 = DB를 조작한다



- CRUD
  - Create
  - Read
  - Update
  - Delete



### Database의 기본 구조

- 스키마(Schema)
  - 데이터베이스에서 제약조건(자료의 구조, 표현방법, 관계 등)을 정의한 구조(structure)
- 테이블(Table)
  - 데이터 요소들의 집합
  - 열(column) : 필드(field) or 속성
  - 행(row) : 레코드(record) or 튜플. 데이터가 저장됨
- PK(기본키) : 모든 데이터베이스에서 반드시 존재
  - id
  - 각 행(레코드)의 고유값(식별 가능하도록)
  - 데이터베이스 관리 및 관계 설정시 주요하게 활용됨



∴ 데이터를 **구조화**하고 **조작**하기 위해



## ORM

- Object-Relational-Mapping
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에(Django - SQL) 데이터를 변환하는 프로그래밍 기술
- OOP 프로그래밍에서 RDBMS을 연동할 때, 데이터베이스
- 파이썬의 코드를 해석해서 SQL로 DB에 넘겨줌(?)

- 장고 : 내장된 Django ORM을 사용함



### ORM의 장점과 단점

- 장점
  - SQL을 잘 알지 못해도 DB 조작 가능
  - SQL의 절차적 접근이 아닌 객체 지향적 접근으로 인한 높은 생산성
- 단점
  - ORM만으로 완전한 서비스를 구현하기 어려운 경우 있음
- 현대 웹 프레임워크의 요점 = 웹 개발 속도를 높이는 것**(생산성**)

∴ DB를 객체로 조작하기 위해 ORM을 사용



### models.py

```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
```

- 각 모델은 django.models.Model 클래스의 서브 클래스로 표현됨
  - django.db.models 모듈의 Model 클래스를 상속받음

- models 모듈을 통해 어떠한 타입의 DB 컬럼을 정의할 것인지 정의
  - title과 content은 모델의 필드(열)을 나타냄
  - 각 필드는 클래스 속성으로 지정되어 있음
  - 각 속성은 각 데이터베이스의 열에 매핑




### 사용 모델 필드

- **CharField(max_length=None, **options)**
  - 길이의 제한이 있는 문자열을 넣을 때 사용
  - max_length는 필수 인자
  - 필드의 최대 길이(문자), 데이터베이스 레벨과 Django의 유효성 검사에서 활용
- **TextField(**options)**
  - 글자의 수가 많을 때 사용



## Migrations

- Django가 model에 생긴 변화를 반영하는 방법
- Migration 실행 및 DB 스키마를 다루기 위한 몇가지 명령어
  - makemigrations ★
  - migrate ★
  - sqlmigrate
  - showmigrations



### Migrations commands

- makemigrations

  ```bash
  $ python manage.py makemigrations
  ```

  - model을 변경한 것에 기반한 새로운 마이그레이션(설계도)을 만들 때 사용
  - 'migrations/0001_initial.py' 생성 확인
  - 추가 모델 필드 작성 후 makemigrations 진행해야 함

  

- migrate
  
  ```bash
  $ python manage.py migrate
  ```
  
  - 마이그레이션을 DB에 반영하기 위해 사용
  - 설계도를 실제 DB에 반영하는 과정
  - 모델에서의 변경 사항들과 DB의 스키마가 동기화를 이룸
  - 0001_initial.py 설계도를 실제 DB에 반영
  
  
  
- sqlmigrate
  
  ```bash
  $ python manage.py sqlmigrate app_name 0001
  ```
  
  - SQL 명령어 보여줌
  - 마이그레이션에 대한 SQL 구문을 보기 위해 사용
  
  
  
- showmigrations
  
  ```bash
  $ python manage.py showmigrations
  ```
  
  - DB 반영 여부
  - 마이그레이션 상태 정보를 확인하기 위해 사용
  - `[X]` : 데이터베이스에 반영되어있다는 의미



### DateField's options

> DateTimeField는 DateField의 서브 클래스

- auto_now_add
  - 최초 생성 일자
  - Django ORM이 최초 insert할 때만 현재 날짜와 시간으로 갱신
- auto_now
  - 최종 수정 일자
  - Django ORM이 save 할 때마다 현재 날짜와 시간으로 갱신




### 반드시 기억해야 할 migration 3단계

1. models.py
   - model 변경사항 발생 시
2. python manage.py makemigrations
   - migrations 파일 생성
3. python manage.py migrate
   - DB 반영 (모델과 DB의 동기화)



## Database API

### DB API

- "DB를 조작하기 위한 도구"
- Django가 기본적으로 ORM을 제공함에 따른 것으로 DB를 편하게 조작할 수 있도록 도움
- Model을 만듦 -> Django는 객체들을 만들고 읽고 수정하고 지울 수 있는 database-abstract API를 자동으로 만듦
- database-abstract API 혹은 database-access API라고도 함



### DB API 구문 - Making Queries

`ClassName.Manager.QuerySetAPI`

ex) `Article.objects.all()`



### DB API

- Manager
  - Django모델에 데이터베이스 query 작업이 제공되는 인터페이스
  - 기본적으로 모든 Django 모델 클래스에 objects라는 Manager를 추가
- QuerySet
  - 유사리스트 : 인덱스접근, 정렬 가능
  - 데이터베이스로부터 전달받은 객체 목록
  - queryset 안의 객체는 0개, 1개 혹은 여러 개일 수 있음
  - 데이터베이스로부터 조회, 필터, 정렬 등을 수행할 수 있음



### Django shell

- 일반 Python shell을 통해서는 장고 프로젝트 환경에 접근할 수 없음
  -> 장고 프로젝트 설정이 load된 Python shell을 활용해 DB API 구문 테스트 진행

- 기본 Django shell보다 더 많은 기능을 제공하는 shell_plus 사용해서 진행

  - Django-extensions 라이브러리의 기능 중 하나

    ```bash
    $ pip install ipython
    $ pip install django-extensions
    ```

    앱 등록(thrid party)

    ```python
    # settings.py
    
    INSTALLED_APPS = [
        ...,
        'django_extensions',
        ...,
    ]
    ```

    shell_plus 실행

    ```bash
    $ python manage.py shell_plus
    ```

    끄는 법 : Ctrl + D -> y






## CRUD

### Create

1. 인스턴스 만들고 변수에 값들 넣기

   ```shell
   >>> article = Article()
   >>> article.title = 'first'
   >>> article.content = 'django'
   >>> article.save()
   >>> Article.objects.all()
   <QuerySet [Article: Article object (1)]>
   ```

2. 클래스에 변수 넣어서 만들기

   ```shell
   >>> article = Article(title='second', content='django')
   >>> article
<Article: Article object (2)>
   ```

3. 클래스에 바로 값 넣어서 만들기 -> save 없어도 바로 저장

   ```shell
   >>> Article.objects.create(title='third', content='django')
   <Article: Article object (3)>
   ```



#### CREATE 관련 메서드

- **save()** method

  - Saving objects
  - 객체를 데이터베이스에 저장

- str method

  ```python
  from django.db import models
  
  class Article(models.Model):
      title = models.CharField(max_length=10)
      content = models.TextField()
  
      def __str__(self):
          return f'<게시글 제목: {self.title} / 게시글 내용: {self.content}'
  ```

  각각의 object가 사람이 읽을 수 있는 문자열을 반환하도록 함

  ※ 작성 후 반드시 shell_plus 재시작해야 반영됨

  

### Read

- all()

  - 현재 QuerySet의 복사본을 반환

    ```shell
    >>> Article.objects.all()
    ```

- get()

  - 객체를 찾을 수 없으면 DoesNotExist 예외 발생

  - 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생 시킴

    ∴ 고유성을 보장하는 조회에서 사용해야 함

    ```shell
    >>> article = Article.objects.get(pk=100)
    ```

- filter()

  ```shell
  >>> Article.objects.filter(content='django')
  ```

  



### Update

- 값을 변경하고 저장하면 됨

  ```shell
  >>> article = Article.objects.get(pk=1)
  >>> article.title
  'first'
  >>> article.title = 'bye'
  >>> article.save()
  >>> article.title
  'bye'



### Delete

- delete()
  - 모든 행에 대해 SQL 삭제 쿼리 수행하고, 삭제된 객체 수와 객체 유형당 삭제 수가 포함된 딕셔너리를 반환
  
  ```python
  # articles/urls.py
  
  from django.urls import path
  from . import views
  
  app_name = 'articles'
  
  urlpatterns = [
      # articles/
      path('', views.index, name='index'),
      # articles/new/ -> throw
      path('new/', views.new, name='new'),
      # articles/create/ -> catch
      path('create/', views.create, name='create'),
      # articles/2/ & articles/3/ & articles/4/....
      path('<int:article_pk>/', views.detail, name='detail'),
      # delete
      path('<int:article_pk>/delete/', views.delete, name='delete'),
  ]
  ```
  
  ```python
  # articles/views.py
  
  def delete(request, article_pk):
      # 1. DB에서 삭제하고자 하는 글 가져옴
      article = Article.objects.get(pk=article_pk)
      # 2. 글을 삭제한다
      article.delete()
      # 3. 삭제 이후 index 페이지로
      return redirect('articles:index')
  ```
  
  ```django
  {% comment %} articles/templates/articles/detail.html {% endcomment %}
  
  {% extends 'base.html' %}
  {% load humanize %}
  
  {% block content %}
    <h2>여기는 DETAIL 페이지입니다.</h2>
    <p>게시글 내용: {{ article.content }}</p>
    <p>게시글 작성 시각: {{ article.created_at|naturaltime }}</p>
    <p>게시글 수정 시각: {{ article.updated_at|naturaltime }}</p>
    <a href="{% url 'articles:delete' article.pk %}">[글 삭제]</a>
    <a href="{% url 'articles:index' %}">[인덱스 페이지로 가자]</a>
  {% endblock content %}
  ```
  
  but. a 태그는 GET 요청밖에 못함 -> 주소창을 통해서도 게시글이 삭제 됨
  
  ↓ 해결 방법(HTTP Method POST 시에만 삭제될 수 있도록)
  
  ```python
  # articles/views.py
  
  def delete(request, article_pk):
      # 요청이 POST인지 검증
      if request.method == 'POST':
          # 1. DB에서 삭제하고자 하는 글 가져옴
          article = Article.objects.get(pk=article_pk)
          # 2. 글을 삭제한다
          article.delete()
          # 3. 삭제 이후 index 페이지로
          return redirect('articles:index')
      # 요청이 POST가 아니라면 현재 페이지에 머물게 함
      return redirect('articles:detail', article_pk)
  ```
  
  ```django
    <form action="{% url 'articles:delete' article.pk %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="글 삭제">
    </form>
  ```
  
  




### Field lookups

- 조회 시 특정 검색 조건을 지정

- filter(), exclude(), get()에 대한 키워드 인수로 지정됨

  ex)

  - Article.objects.filter(pk__gt=2)	# gt = greater than
  - Article.objects.filter(content__contains='ja')



### QuerySet API

https://docs.djangoproject.com/en/4.0/ref/models/querysets/#queryset-api-reference



## Admin Site

### Automatic admin interface

- 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지
- Model class를 admin.py에 등록하고 관리
- django.contrib.auth 모듈에서 제공됨
- record 생성 여부 확인에 유용
- 직접 record를 삽입할 수 있음



### admin 생성

```bash
$ python manage.py createsuperuser
```

- 관리자 계정 생성 후 서버를 실행 -> '/admin'으로 가서 관리자 페이지 로그인
- 내가 만든 Model을 보기 위해서는 admin.py에 작성하여 Django 서버에 등록



### admin 등록

```python
# articles/admin.py

from django.contrib import admin
from .models import Article

admin.site.register(Article, ArticleAdmin)
```

- admin.py : 관리자 사이트에 Article 객체가 관리자 인터페이스를 가지고 있다는 것을 알려줌
- models.py에 정의한 `__str__`의 형태로 객체가 표현됨



### ModelAdmin options

```python
# articles/admin.py

from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)

admin.site.register(Article, ArticleAdmin)
```

- list_display
  - models.py 정의한 각각의 속성들의 값을 admin 페이지에 출력하도록 설정
  - https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#modeladmin-options



## CRUD with views

### HTTP method

- GET
  - 특정 리소스를 가져오도록 요청할 때 사용
  - 데이터를 가져올 때만 사용해야 함
  - DB에 변화주지 x
  - CRUD에서 R 담당
- POST
  - 서버로 데이터를 전송할 때 사용
  - 리소스를 생성/변경하기 위해 데이터를 HTTP body에 담아 전송
  - 서버에 변경사항을 만듦
  - CRUD에서 C/U/D 담당



### 사이트 간 요청 위조(Cross-site request forgery, CSRF)

- 웹 애플리케이션 취약점 중 하나
  - 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법



### CSRF 공격 방어

- Security Token 사용 방식 (CSRF Token)
  - 사용자의 데이터에 임의의 난수 값을 부여 -> 매 요청마다 해당 난수 값을 포함시켜 전송시키도록 함
  - 이후 서버에서 요청을 받을 때마다 전달된 token 값이 유효한지 검증
- GET 제외 메서드에 적용
- Django는 CSRF token 템플릿 태그 제공



### csrf_token telmpate tag

```django
{% csrf_token %}
```

- input type이 hidden으로 작성됨

- value는 Django에서 생성한 hash 값으로 설정됨

- 해당 태그 없이 요청 보낸다면 Django 서버는 403 forbidden을 응답

  ```django
  {% extends 'base.html' %}
  
  {% block content %}
    <h2>여기는 NEW 페이지입니다.</h2>
    <form action="{% url 'articles:create' %}" method="POST">
      {% csrf_token %}
      <label for="title">게시글 제목: </label>
      <input type="text" id="title" name="title">
        ...
  ```



### Django shortcut function - "redirect()"

- 새 URL로 요청 다시 보냄
- 인자에 따라 HttpResponseRedirect를 반환
- 브라우저는 현재 경로에 따라 전체 URL 자체를 재구성(reconstruct)
- 사용 가능한 인자
  1. model
  2. view name: viewname can be URL pattern name or callable view object.
  3. absolute or relative URL

```python
# articles/views.py

from django.shortcuts import render, redirect

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    article = Article(title=title, content=content)
    article.save()
    return redirect('articles:index')
```



### DETAIL

```python
# articles/urls.py
    ...
    # Variable Routing
    path('<int:article_pk>/', views.detail, name='detail'),
```

```python
# articles/views.py

# 매개변수로 pk를 넘겨줌
def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
```

```django
<!-- articles/templates/articles/detail.html -->
{% extends 'base.html' %}

{% block content %}
  <div class="container m-2">
    <h1 class='fw-bold'>DETAIL</h1>
    <br>
    <h3>{{ article.title }}</h3>
    <p>{{ article.content }}</p>
    <p>작성일: {{ article.created_at }}</p>
    <p>수정일: {{ article.updated_at }}</p>
    <a href="{% url 'articles:edit' article.pk %}">EDIT</a>
    <form action="{% url 'articles:delete' article.pk %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="DELETE">
    </form>
    <br>
    <a href="{% url 'articles:index' %}">BACK</a>
  </div>
{% endblock content %}
```



