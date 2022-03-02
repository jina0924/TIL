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



#### Static web page(정적 웹 페이지)

- 서버에 미리 저장된 파일이 사용자에게 그대로 전달되는 웹 페이지
- 요청 -> 추가적인 처리 과정 없이 응답 보냄
- 모든 상황에서 모든 사용자에게 동일한 정보를 표시
- HTML, CSS, JavaScript로 작성됨
- flat page라고도 함



#### Dynamic web page(동적 웹 페이지)

- 요청 -> 추가적인 처리 과정 이후 응답을 보냄
- 방문자와 상호작용하기 때문 => 페이지 내용은 그때그때 다름(why? DB때문)
- 서버 사이드 프로그래밍 언어(Python, Java, C++등)가 사용됨
  파일을 처리하고 데이터베이스와의 상호작용이 이루어짐



### Framework

- 프로그래밍에서 특정 운영 체제를 위한 응용 프로그램 표준 구조를 구현하는 클래스와 라이브러리 모임
- Application framework라고도 함



### Web framework

- 웹 페이지를 개발하는 과정에서 겪는 어려움을 줄이는 것이 주 목적
- 동적 웹 페이지, 웹 애플리케이션, 웹 서비스 개발 보조용으로 만들어지는 Application Framework의 일종



### Django를 사용해야 하는 이유

- 검증된 Python 언어 기반 Web framework
- 대규모 서비스에도 안정적 & 오랫동안 세계적인 기업들에 의해 사용됨



### Framework Architecture

- **MVC Design Pattern**(model-view-controller)
- 소프트웨어 공학에서 사용되는 디자인 패턴 중 하나
- UI랑 별도로 시각적인 부분 이면에 실행되는 부분들을 서로 영향없이 개발 가능
- Django는 **MTV Pattern** (model-template-view)이라고 함



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

순서

1. HTTP : client의 요청(정확히는 URI)
2. URLS
3. View
4. HTTP Response



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
  2. djaogo 설치
  3. 프로젝트 생성
  4. 서버켜서 로켓 확인
  4. 앱 생성
  4. 앱 등록



#### [참고] LTS

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



#### 앱 생성 시 주의 사항

- **반드시 생성 후 등록!**
- INSTALLED_APPS에 먼저 작성(등록)하고 생성하려면 앱이 생성되지 않음



#### 앱 등록 시 주의 사항

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
  프로그래밍적 로직이 아니라 프레젠테이션을 포현하기 위한 것
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





## HTML Form







## URL

