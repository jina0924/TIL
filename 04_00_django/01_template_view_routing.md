# Django

[toc]

## Web Framework

> 서버를 만들어주는 도구

클라이언트 -> 요청 -> 서버

- 요청 : browser(url) 또는 코드(requests)를 통해

서버 -> 응답 -> 클라이언트



### Django

- 파이썬 웹 프레임워크
- you can focus on writing your app without needing to reinvent the wheel.



### Web

- World Wide Web
- 인터넷에 연결된 컴퓨터를 통해 정보를 공유할 수 있는 전 세계적인 정보 공간



**Static web page(정적 웹 페이지)**

- 서버에 미리 저장된 파일이 사용자에게 그대로 전달되는 웹 페이지
- 요청 -> 추가적인 처리 과정 없이 응답 보냄
- 모든 상황에서 모든 사용자에게 동일한 정보를 표시
- HTML, CSS, JavaScript로 작성됨
- flat page라고도 함



**Dynamic web page(동적 웹 페이지)**

- 요청 -> 추가적인 처리 과정 이후 응답을 보냄
- 방문자와 상호작용하기 때문 => 페이지 내용은 그때그때 다름(why? DB때문)
- 서버 사이드 프로그래밍 언어(Python, Java, C++등)가 사용됨
  파일을 처리하고 데이터베이스와의 상호작용이 이루어짐



### Framework

- 프로그래밍에서 특정 운영 체제를 위한 응용 프로그램 표준 구조를 구현하는 클래스와 라이브러리 모임
- 재사용할 수 있는 수많은 코드를 프레임워크로 통합 -> 개발자가 새로운 애플리케이션을 위한 표준 코드를 다시 작성하지 않아도 같이 사용할 수 있도록 도움
- Application framework라고도 함



### Web framework

- 웹 페이지를 개발하는 과정에서 겪는 어려움을 줄이는 것이 주 목적
- 동적 웹 페이지, 웹 애플리케이션, 웹 서비스 개발 보조용으로 만들어지는 Application Framework의 일종



**Django를 사용해야 하는 이유**

- 검증된 Python 언어 기반 Web framework
- 대규모 서비스에도 안정적 & 오랫동안 세계적인 기업들에 의해 사용됨
  - Spotify, Instagram, Dropbox, Delivery Hero



**Framework Architecture**

- **MVC Design Pattern**(model-view-controller)

- 소프트웨어 공학에서 사용되는 디자인 패턴 중 하나

- 사용자 인터페이스로부터 프로그램 로직을 분리

- UI랑 별도로 시각적인 부분 이면에 실행되는 부분들을 서로 영향없이 개발 가능

- Django는 **MTV Pattern** (model-template-view)

  



### MTV Pattern

- Model
  - 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리(추가, 수정, 삭제)
- Template(view)
  - 파일의 구조나 레이아웃을 정의
  - 실제 내용을 보여주는 데 사용
- View(controller) ★
  - HTTP 요청을 수신하고 HTTP 응답을 반환
  - Model을 통해 요청을 충족시키는데 필요한 데이터에 접근
  - template에게 응답의 서식 설정을 맡김
  - model과 template 관리
  - 중간관리자
  - 함수로 이루어져 있음



### MTV Pattern ★

<img src="01_template_view_routing.assets/화면 캡처 2022-03-02 092356.jpg" alt="MTV Pattern" style="zoom: 67%;" />



## Django Intro

### Django 시작하기

```bash
$ python -m venv venv	# 가상환경 생성(한 번 만 하면 됨)
$ source venv/Scripts/activate	# 가상환경 활성화
$ pip list	# 가상환경 확인
```

※ 가상환경 비활성화 : `deactivate`

```bash
$ python -m venv venv && source venv/Scripts/activate
```

로 해도 차례대로 실행됨



- 장고 설치

```bash
$ pip install django==3.2.12
```

버전 명시하지 않으면 가장 최근 버전 설치함

현재 3.2가 LTS (Long Term Support)



- 설치한 패키지 requirements.txt파일에 저장

```bash
$ pip freeze > requirements.txt
```



- requirements.txt에 있는 내용 자동 설치

```bash
$ pip install -r requirements.txt
```



- 프로젝트 생성

  `django-admin startproject <프로젝트명> .`

```bash
$ django-admin startproject firstpjt .
```

firstpjt란 이름으로 프로젝트 생성

※ `.`을 안찍으면 해당 이름으로 폴더 만들고 그 안에 프로젝트 폴더 만듦

※ 프로젝트 이름에는 Python이나 Django에서 사용중인 키워드는 피해야함

하이픈도 사용 금지

ex) Django, text, class, django-test 등



- Django 서버 시작하기(활성화)

```bash
$ python manage.py runserver
```

-> ctrl 누른 상태로 url 클릭 = 메인 페이지 확인



- 순서
  1. 가상환경 생성 및 활성화
  2. django 설치
  3. 프로젝트 생성
  4. 서버켜서 로켓 확인
  4. 앱 생성
  4. 앱 등록



**[참고] LTS**

- Long Term Support (장기 지원 버전)
- 일반적인 경우보다 장기간에 걸쳐 지원하도록 고안된 소프트웨어의 버전
- 컴퓨터 소프트웨어의 제품 수명주기 관리 정책
- 배포자는 LTS 확정을 통해 장기적이고 안정적인 지원을 보장함



### 프로젝트 구조

- `__init__.py`  ❌
- asgi.py ❌
  - Django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움

- settings.py ★(수업시간에 자주 쓰게 됨)
  - 애플리케이션의 모든 설정을 포함
- urls.py ★
  - 사이트의 url과 적절한 views의 연결을 지정

- wsgi.py ❌
  - Web Server Gateway Interface
  - Django 애플리케이션이 웹서버와 연결 및 소통하는 것을 도움
- manage.py ❌
  - Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티



### Application 생성

- 일반적으로 Application명은 **복수형**으로 하는 것을 권장

  ```bash
  $ python manage.py startapp articles
  ```



#### Application 구조

- admin.py
  - 관리자용 페이지를 설정하는 곳
- apps.py ❌
  - 앱의 정보가 작성된 곳
- models.py
  - 앱에서 사용하는 Model을 정의하는 곳
- tests.py ❌
  - 프로젝트의 테스트 코드를 작성하는 곳
- views.py
  - view 함수들이 정의되는 곳



### Project & Application

- Project
  - application의 집합(collection of apps)
  - 프로젝트에는 여러 앱이 포함될 수 있음
  - 앱은 여러 프로젝트에 있을 수 있음
- Application
  - 앱을 실제 요청을 처리하고 페이지를 보여주고 하는 등의 역할을 담당
  - 하나의 프로젝트는 여러 앱을 가짐
  - 일반적으로 앱은 하나의 역할 및 기능 단위로 작성함
- 장고는 1 project, n개의 application



### 앱 등록 ★

- 프로젝트에서 앱을 사용하기 위해서는 **반드시 INSTALLED_APPS 리스트에 추가해야 함**
- **INSTALLED_APPS**     ※ 모두 대문자 -> 상수
  - Django installation에 활성화 된 모든 앱을 지정하는 문자열 목록

```python
# settings.py

INSTALLED_APPS = [
    'articles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

6개 : 장고 설치하면 자동적으로 등록되는 앱

'articles' 제일 위에 등록



**앱 생성 시 주의 사항**

- **반드시 생성 후 등록!**
- INSTALLED_APPS에 먼저 작성(등록)하고 생성하려면 앱이 생성되지 않음



**앱 등록 시 주의 사항**

- 장고가 권장하는 앱 등록 순서
  1. Local apps
  2. Third party apps
  3. Django apps



## 요청과 응답

### URLs(프로젝트 내부)

```python
# urls.py

from django.contrib import admin
from django.urls import path
from articles import views		# 가져오기 위해 import해야함

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
]	# 함수 요청이 왔을 때, 뒤에 있는 함수 호출한단 의미
```

admin/ : url 주소의 일부분

trailing comma : 리스트 끝에 , 붙임 why? 이후에 바로 작성할 수 있도록 생산성을 높이기 위해



### View(애플리케이션 내부)

```python
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')	# 필수 인자, 템플릿 경로
```

view 함수는 반드시 request를 인자로 받아와야함(이름은 상관없지만 self처럼 관례로 따를 것)



### Templates(애플리케이션 내부 폴더)

```html
<!-- articles/templates/index.html-->
<h1>
    만나서 반가워요!
</h1>
```

- 실제 내용을 보여주는데 사용되는 파일
- 파일의 구조나 레이아웃을 정의 ex) HTML
- 반드시 **app/templates/**로 만들어야 함



### 추가 설정

- LANGUAGE_CODE
  - 모든 사용자에게 제공되는 번역을 결정
  - ko-KR이지만 대문자보단 소문자로 작성
- TIME_ZONE
  - 출력을 서울 시간으로 바꿔서
  - list of tz
- USE_I18N
- USE_L10N
- USE_TZ

```python
# settings.py

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```



## Template

### Django Template

- 데이터 표현을 제어하는 도구이자 표현에 관련된 로직
- 사용하는 built-in system
  - Django template language
  - 장고 템플릿 위에서 쓸 수 있는 별도의 문법 존재



### Django Template Language(DTL)

- 조건, 반복, 변수 치환, 필터 등의 기능을 제공
- 단순히 Python이 HTML에 포함 된 것 x
  프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것
- Python처럼 일부 프로그래밍 구조(if, for 등)를 사용할 수 있지만, 해당 python코드로 실행되는 것이 아님



### DTL Syntax

1. Variable
2. Filters
3. Tags
4. Comments



#### DTL Syntax - Variable

```django
{{ variable }}
```

- render()를 사용하여 views.py에서 정의한 변수를 template 파일로 넘겨 사용하는 것
- 변수명 숫자와 밑줄(_) 조합으로 구성 & 밑줄로는 시작 x
  - 공백이나 구두점 문자 사용 x

- dot(.)를 사용하여 변수 속성에 접근할 수 있음
- render()의 세 번째 인자로 {'key': value}와 같이 딕셔너리 형태로 넘겨줌
  여기서 정의한 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨



변수명 context 바꿔도 상관없지만 굳이?

context에서 key와 value 똑같이 씀(접근할 때는 key로 접근)



#### DTL Syntax - Filters

```django
{{ variable|filter }}
```

- 표시할 변수를 수정할 때 사용

- 예시

  - name 변수를 모두 소문자로 출력

    ```django
    {{ name|lower }}
    ```


- 60개의 built-in template filters를 제공

- chained가 가능하며 일부 필터는 인자를 받기도 함

  ```django
  {{ variable|truncatewords:30 }}



#### DTL Syntax - Tags ★

```django
{% tag %}
```

- 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행

- 일부 태그는 시작과 종료 태그가 필요

  ```django
  {% if %}{% endif %}
  ```

  ex) for + enter => 닫는태그 자동완성

- 약 24개의 built-in template tags를 제공



#### DTL Syntax - Comments

```django
{# 주석내용 #}
```

```django
{% comment %}
  주석
  주석
{% endcomment %}
```

- Django template에서 라인의 주석을 표현하기 위해 사용

- 단축키 : ctrl+/



### 코드 작성 순서

1. urls.py
2. views.py
3. TEMPLATE 순으로 작성(데이터의 흐름 순)



### Template inheritance(템플릿 상속)

- 코드 재사용성에 초점을 맞춤
- 템플릿 상속을 사용하면 사이트의 모든 공통 요소를 포함, 하위 템플릿이 재정의할 수 있는 블록을 정의하는 기본 "skeleton" 템플릿을 만들 수 있음



#### Template inheritance - tags

```django
{% extends '부모템플릿 이름' %}
```

- 자식 (하위) 템플릿이 부모 템플릿을 확장한다는 것을 알림
- 반드시 템플릿 최상단에 작성 되어야 함



```django
{% block content %} {% endblock %}
```

- 하위 템플릿에서 재지정할 수 있는 블록을 정의
- 하위 템플릿이 채울 수 있는 공간



#### [실습] Template inheritance

```python
# 프로젝트명/settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

- 'DIRS': [BASE_DIR / 'templates',], 추가
- 시작점을 최상단 폴더에 잡아줌
- BASE_DIR : 제일 상단 폴더



```django
{# templates/base.html #}

<body>
  {% include '_nav.html' %}
  <div class="container">
    {% block content %}
    {% endblock %}
  </div>
</body>
```

- block: 상속받을 html이 내용을 변경할 수 있는 영역



```django
{# 애플리케이션/templates/index.html #}

{% extends 'base.html' %}

{% block content %}
  <h1>안녕하세요ㅎㅎ</h1>
{% endblock content %}
```

- extends에 상속받을 html적어둠
- endblock에는 content라는 이름 안적어도 되지만 구분을 위해 적어둘 것



### Template Tag - include

```django
{% include '' %}
```

- 템플릿을 로드하고 현재 페이지로 렌더링
- 템플릿 내에 다른 템플릿을 포함하는 방법



```django
<-- 애플리케이션/templates/_nav.html -->

<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Features</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
```

- _nav로 쓰는 이유 : `_`안붙여도 되지만 include되는 template란 의미



```django
{# templates/base.html #}

<body>
  {% include '_nav.html' %}
  <div class="container">
    {% block content %}
    {% endblock %}
  </div>
</body>
```



#### Django template system(feat. Django 설계 철학)

- 표현과 로직을 분리
  - 템플릿 시스템은 표현을 제어하는 도구이자 표현에 관련된 로직일 뿐
  - 템플릿 시스템은 이러한 기본 목표를 넘어서는 기능을 지원하지 말아야함
- 중복을 배제
  - 대다수의 동적 웹사이트는 공통 디자인을 가짐
  - 공통 디자인 요소를 한 곳에 저장하기 쉽게 하여 중복 코드 제거
  - 상속의 기초가 되는 철학





## HTML Form ★

### HTML "form" element

- 웹에서 사용자 정보를 입력하는 여러 방식
  - text, button, checkbox, file, hidden, image, password, radio, reset, submit

- 핵심 속성(attribute)
  - action : 입력 데이터가 전송될 URL 지정(어디로 보낼건지)
  - method : 입력 데이터 전달 방식 지정
    - 기본값 : GET

```django
{% comment %} 
  action -> 어디로 공을 던질지!
  method -> 어떤 방식으로 던질지(단순 조회가 GET)
{% endcomment %}
<form action="/articles/catch/" method="GET">
  <input type="text" name="ball">
  <input type="submit" value="공을 던지자!">
</form>
```



### HTML "input" element

- 사용자로부터 데이터를 입력 받기 위해 사용
- type 속성에 따라 동작 방식이 달라짐
- 핵심 속성
  - **name**
  - 중복 가능, 양식을 제출했을 때 name이라는 이름에 설정된 값을 넘겨서 값을 가져올 수 있음
  - 주요 용도는 GET/POST 방식 -> 서버에 전달하는 파라미터(name은 key, value는 value)로 매핑하는 것
  - GET 방식에서는 URL에서 `?key=value&key=value` 형식으로 데이터 전달

```django
<form action="/articles/catch/" method="GET">
  {% comment %} 
    name -> 어떤 박스에 담아서 던지지 결정!
    name의 값은 박스의 이름을 의미한다!  
  {% endcomment %}
  <input type="text" name="ball">
  <input type="submit" value="공을 던지자!">
</form>
```



### HTML "label" element

- 사용자 인터페이스 항목에 대한 설명(caption)을 나타냄

- label을 input 요소와 연결하기
  1. input에 id 속성 부여
  2. label에는 input의 id와 동일한 값의 for 속성이 필요
- label과 input 요소 연결의 주요 이점
  - 시각적인 기능 뿐만 아니라 화면 리더기에서 label을 읽어 사용자가 입력해야 하는 텍스트가 무엇인지 더 쉽게 이해할 수 있도록 돕는 프로그래밍적 이점도 있음
  - label을 클릭해서 input에 초점(focus)를 맞추거나 활성화(activate)시킬 수 있음



### HTML "for" attribute

- for 속성의 값과 일치하는 id를 가진 문서의 첫 번째 요소를 제어
  - 연결된 요소가 labelable elements인 경우 이 요소에 대한 labeled control이 됨
- labelable elements
  - label 요소와 연결할 수 있는 요소
  - button, input(not hidden type), select, textarea, ...

```django
{% block content %}
  <h1>Throw</h1>
  <form action="#" method="#">
      <label for="message">Throw</label>
      <input type="text" id="message" name="message">
      <input type="submit">      
  </form>
```



### HTML "id" attribute

- 전체 문서에서 고유해야 하는 식별자를 정의
- 사용 목적
  - linking, scripting, styling 시 요소를 식별



### HTTP

- HpyerText Transfer Protocol
  - 하이퍼 텍스트를 주고받는 규약

- 웹에서 이루어지는 모든 데이터 교환의 기초
- 주어진 리소스가 수행할 작업을 나타내는 request methods를 정의
- HTTP request method 종류
  - GET, POST, PUL, DELETE, ... => CRUD



#### HTTP request method - 'GET'

- 서버로부터 정보를 조회하는데 사용
- 데이터를 가져올 때만 사용해야함
- 데이터를 서버로 전송할 때 Query String Parameters를 통해 전송



## URL

### Variable Routing

- URL 주소를 변수로 사용하는 것

- URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음

- 변수 값에 따라 하나의 path()에 여러 페이지 연결 가능

  ex) `path('accounts/user/<int:user_pk>/', ...)`

  		- accounts/user/1
  		- accounts/user/2



### URL Path converters

- str

  - `/`를 제외하고 비어 있지 않은 모든 문자열과 매치
  - 작성하지 않을 경우 기본 값

- int

  - 0 또는 양의 정수와 매치

- slug

  - ASCII 문자 또는 숫자, 하이픈 및 밑줄 문자로 구성된 모든 슬러그 문자열과 매치

    ex) 'building-your-1st-django-site'

- uuid
- path

```python
    path('hello/<str:name>/<name2>/', views.hello, name='hello'),    
    path('food/<name>/<int:num>/', views.food, name='food'),
```



### App URL mapping

- 유지보수를 위해 각 app에 urls.py를 작성

  ```python
  # 프로젝트이름/urls.py
  
  from django.contrib import admin
  from django.urls import path, include
  
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('articles/', include('articles.urls')),
  ]
  ```

  ```python
  # 앱 이름/urls.py
  
  from django.urls import path
  from . import views
  
  urlpatterns = [
      path('index/', views.index),
      path('greeting/', views.greeting),
      path('dinner/', views.dinner),
      path('throw/', views.throw),
      path('catch/', views.catch),
      path('hello/<name>/', views.hello),
  ]
  ```

  - 각각의 앱 안에 urls.py를 생성 -> 프로젝트 urls.py에서 각 앱의 urls.py 파일로 URL 매핑 위탁



#### Including other URLconfs

- **include()**
  - 다른 URLconf(app1/urls.py)들을 참조할 수 있도록 도움
  - 함수 include()를 만나게 되면, URL의 그 시점까지 일치하는 부분 잘라냄 -> 남은 문자열 부분을 후속처리를 위해 include된 URLconf로 전달



## Namespace

> 개체를 구분할 수 있는 범위를 나타내는 namespace

- 위에서 제시된 대로 만들었을 때 문제점

1. articles 앱의 index 페이지에서 두번째 앱 pages의 index로 이동하는 하이퍼링크를 클릭 시 현재 페이지로 이동됨
   - URL namespace

2. pages 앱 index url로 이동해도 articles 앱의 index페이지가 출력됨
   - Template namespace




↓ 해결방법

### URL namespace(이름공간)

1. 서로 다른 app의 같은 이름을 가진 url name은 이름공간을 설정해서 구분
2. templages, static 등 django는 정해진 경로 하나로 모아서 보기 때문에 중간에 폴더를 임의로 만들어 줌으로써 이름공간을 설정

```python
# pages/urls.py

from . import views

app_name = 'pages'
urlpatterns = [
    path('index/', views.index, name='index'),
]
```



### URL namespace

**app_name attribute 작성**

```python
# pages/urls.py

app_name = 'pages'
urlpatterns = [
    path('index/', views.index, name='index'),
]
```

```python
# articles/urls.py

app_name = 'articles'
urlpatterns = [
    ...,
]
```



**url template tag**

```django
{% url '' %}
```

- 주어진 URL 패턴 이름 및 선택적 매개 변수와 일치하는 절대 경로 주소 반환



**`app_name` attribute**

- URL namespace를 사용하면 서로 다른 앱에서 동일한 URL 이름을 사용하는 경우에도 이름이 지정된 URL을 고유하게 사용 할 수 있음
- urls.py에 `app_name` attribute 값 작성



- 참조
  - `:` 연산자를 사용하여 지정
    - app_name이 `articles`이고 URL name이 `index`인 주소 참조는 `url 'articles:index'`

```django
<!-- articles/templates/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>INDEX</h1>
  <!-- app_name이 articles이고 URL name이 greeting인 주소 참조 -->
  <a href="{% url 'articles:greeting' %}">greeting</a>
  <a href="{% url 'articles:dinner' %}">dinner</a>
  <a href="{% url 'articles:throw' %}">throw</a>
  <a href="{% url 'articles:dtl_practice' %}">dtl_practice</a>

  <a href="{% url 'pages:index' %}">두번째 앱의 메인페이지</a>
{% endblock content %}
```





### Tmeplate namespace

- Django는 기본적으로 `app_name/templates/` 경로에 있는 templates 파일들만 찾을 수 있음

- INSTALLED_APPS에 작성한 app순서대로 template을 검색 후 렌더링

- 임의로 templates의 폴더 구조를 `app_name/templates/app_name` 형태로 변경해 임의로 이름 공간 생성 후 변경된 추가 경로 작성

  ```python
  # articles/views.py
  
  return render(request, 'articles/index.html')
  ```

  ```python
  # pages/view.py
  
  return render(request, 'pages/index.html')
  ```

  



## Static files

### 웹 서버와 정적 파일

- 웹 서버는 특정 위치(url)에 있는 자원을 요청을 받아서 제공하는 응답을 처리하는 것을 기본 동작으로 함
- 자원과 접근 가능한 주소가 정적으로 연결된 관계
  - ex) 사진파일 - 자원, 파일 경로 - 웹 주소
- 웹 서버는 요청 받은 url로 서버에 존재하는 정적 자원을 제공



### static files

- 정적 파일

- 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일

  ex) 이미지, 자바 스크립트, CSS

- 파일 자체가 고정되어 있고, 서비스 중에도 추가되거나 변경되지 않고 고정되어 있음

- 장고에서 관련 기능 제공



### static files 구성

1. django

2. settings.py에서 static_url을 정의

3. 템플릿에서 static 템플릿 태그를 사용하여 지정된 상대 경로에 대한 url을 빌드

   ```django
   {% load static %}
   
   <img scr="{% static 'my_app/example.jpg' %}" alt="My image">
   ```

4. 앱의 static 디렉토리에 정적 파일을 저장

   ex) my_app/static/my_app/example.jpg



- staticfiles_dirs(새로 만들어야함)

  ```python
  STATICFILES_DIRS = [
      BASE_DIR / 'static',
  ]
  ```

  - app/static/ 디렉토리 경로를 사용하는 것(기본 경로) 외에 추가적인 정적 파일 경로 목록을 정의하는 리스트
  - 추가 파일 디렉토리에 대한 전체 경로를 포함하는 문자열 목록으로 작성되어야 함

- static_url(이미 setting.py에 있었음)

  ```python
  STATIC_URL = '/static/'
  ```

  - STATIC_ROOT에 있는 정적 파일을 참조 할 때 사용할 URL 
  - 개발 단계에서는 실제 정적 파일들이 저장되어 있는 app/static/ 경로 (기본 경로) 및STATICFILES_DIRS에 정의된 추가 경로들을 탐색함 
  - 실제 파일이나 디렉토리가 아니며, URL로만 존재 비어 있지 않은 값으로 설정 한다면 반드시 slash(/)로 끝나야 함

- static_root -> 개발 단계에선 동작하지 않음

  - collectstatic이 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로
  - 장고 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아 넣는 경로
  - 개발 과정에서 settings.py의 DEBUG 값이 True로 설정되어 있으면 해당 값은 작용되지 않음

- 실 서비스 환경(배포 환경)에서 django의 모든 정적 파일을 다른 웹 서버가 직접 제공하기 위함



### Django template tag

- load
  - 사용자 정의 템플릿 태그 세트를 로드(load)
  - 로드하는 라이브러리, 패키지에 등록된 모든 태그와 필터를 불러옴
  - 빌트인 x (파이썬에서 import같은 역할)
- static
  - static_root에 저장된 정적 파일에 연결
