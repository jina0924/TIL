# Authentication System

[toc]

## 1

### The Django Authentication System

- 장고 인증 시스템(이미 INSTALLED_APPS에 설치되어 있음)
  1. django.contrib.auth
     - 인증 프레임워크의 핵심과 기본 모델을 포함
  2. django.contrib.contenttypes
     - 사용자가 생성한 모델과 권한을 연결할 수 있음
- 장고 인증 시스템 = 인증 + 권한부여



**Authentication(인증)**

- 신원 확인
- 사용자가 자신이 누구인지 확인하는 것



**Authorization(권한, 허가)**

- 권한 부여
- 인증된 사용자가 수행할 수 있는 작업을 결정



두 번째 앱(accounts) 생성하기

- 장고 내부적으로 accounts라는 이름으로 사용되고 있기 때문에 accounts로 지정하는 것을 권장

  ```bash
  $ python manage.py startapp accounts
  ```

  ```python
  # settings.py
  
  INSTALLED_APPS = [
      'articles',
      'accounts',
      ...
  ```

  ```python
  # crud/urls.py
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('articles/', include('articles.urls')),
      path('accounts/', include('accounts.urls')),
  ]
  ```

  ```python
  # accounts/urls.py
  
  from django.urls import path
  from . import views
  
  
  app_name = 'accounts'
  urlpatterns = [
      
  ]





### 쿠키와 세션

#### HTTP

- Hyper Text Transfer Protocol
  - HTML 문서와 같은 리소스(자원, 데이터)들을 가져올 수 있도록 해주는 프로토콜



#### HTTP 특징

- **비연결지향(connectionless)**
  - 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
  - ex) 네이버 접속 시 네이버 메인페이지 응답을 주고 연결을 끊음
- **무상태(stateless)**
  - 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음
  - 클라이언트와 서버가 주고 받는 메시지들은 서로 완전히 독립적임
- 클라이언트와 서버의 지속적인 관계를 유지하기 위해 쿠키와 세션이 존재



#### 쿠키

- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
- 사용자가 웹사이트를 방문할 경우 해당 웹사이트의 서버를 통해 사용자의 컴퓨터에 설치(배치, palced-on)되는 작은 기록 정보 파일
  - 로컬에 KEY-VALUE의 데이터 형식으로 저장
  - 동일한 서버에 재요청 시 저장된 쿠키를 함께 전송
  - 로그인 했다면 클라이언트가 계속 요청과 함께 쿠키(로그인 상태)를 보냄
- HTTP 쿠키는 상태가 있는 세션을 만들어 줌
- 쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용
  - 이를 통해 로그인 상태 유지 가능
  - 상태가 없는 HTTP 프로토콜에서 상태 정보를 기억 시켜주기 때문

∴ 웹 페이지 접속 -> 요청한 웹페이지를 받으며 쿠키를 저장 -> 클라이언트가 같은 서버에 재요청시 -> 요청과 함께 쿠키도 함께 전송



#### 쿠키 사용 목적

1. 세션 관리
   - 로그인, 아이디 자동 완성, 공지 하루 안보기, 팝업 체크, 장바구니 등의 정보 관리
   - 장바구니에서 물품 삭제 -> 해당 물품 쿠키 삭제
2. 개인화
   - 사용자 선호, 테마 등의 설정
3. 트래킹
   - 사용자 행동을 기록 및 분석
   - 시크릿 모드 -> 쿠키 허용 x => 트래킹 불가



#### 세션(Session)

- 사이트와 특정 브라우저 사이의 "상태(state)"를 유지시키는 것
- 클라이언트가 서버에 접속 -> 서버가 특정 session id를 발급 -> 클라이언트는 발급받은 session id를 쿠키에 저장
- ID는 세션을 구별하기 위해 필요 / 쿠키에는 ID만 저장함
- 로그아웃 = 세션 삭제



#### 쿠키 lifetime(수명)

1. Session cookies
   - 현재 세션이 종료되면 삭제됨
     - SWEA 세션 기간이 짧기 때문에 금방 로그아웃 되는 것
   - 브라우저가 현재 세션이 종료되는 시기를 정의
     - 일부 브라우저는 다시 시작할 때 세션 복원(session restoring)을 사용해 세션 쿠키가 오래 지속 될 수 있도록 함
2. Persistent cookies(or Permanent cookies)
   - Expires속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제



#### Session in Django

- 장고의 세션은 미들웨어를 통해 구현됨
- 기본 값: database-backed sessions 저장 방식
- 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 세션을 알아냄
  - 세션 정보는 Django DB의 django_session 테이블에 저장됨



[참고] MIDDLEWARE(미들웨어)

- HTTP 요청과 응답 처리 중간에서 작동하는 시스템(hooks)
- 장고는 HTTP 요청이 들어오면 미들웨어를 거쳐 해당 URL에 등록되어 있는 view로 연결해주고, HTTP 응답 역시 미들웨어를 거쳐서 내보냄
- 데이터 관리, 애플리케이션 서비스, 메시징, 인증 및 API 관리를 담당



### 로그인

- session을 create하는 로직과 같음
- 장고는 built-in-forms를 제공



#### AuthenticationForm

- 사용자 로그인을 위한 form
- request를 첫 번재 인자로 취함

```python
# urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.url.py'))
]
```

```python
# accounts/urls.py

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
]
```

```python
# accounts/views.py

from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        pass
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
```

```django
{% extends 'base.html' %}

{% block content %}
  <h1>LOGIN</h1>
  <hr>
  <form action="{% url 'accounts:login' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  <a href="{% url 'articles:index' %}">back</a>
{% endblock content %}
```



#### login 함수

`login(request, user, backend=None)`

- 현재 세션에 연결하려는 인증된 사용자(`form.is_valid()`를 통과한 사용자)가 있는 경우 login() 함수가 필요
- 사용자를 로그인함. view 함수에서 사용 됨
- HttpRequest 객체와 User 객체가 필요
- 장고의 session framework를 사용하여 세션에 user의 ID를 저장 ( = 로그인)

```python
# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        # ModelForm이 아닌 Form을 상속받음
        # why? 아이디랑 비밀번호 DB에 저장x
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 실제 로그인
            # DB에 저장할 필요x
            # login 이름 같기 때문에 auth_login으로 바꿔줌
            auth_login(request, form.get_user())
            return redirect('articles:index')

    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
```

- get_user()
  - AuthenticationForm의 인스턴스 메서드
  - 인스턴스의 유효성을 먼저 확인하고, 인스턴스가 유효할 때만 user를 제공하려는 구조



### Authentication data in tempaltes

- context processors
  - 템플릿이 렌더링 될 때 자동으로 호출 가능한 컨텍스트 데이터 목록
  - 작성된 프로세서는 RequestContext에서 사용 가능한 변수로 포함됨
- Users
  - 현재 로그인한 사용자를 나타내는 auth.User 인스턴스는 템플릿 변수 `{{ user }}`에 저장됨
  - 비로그인 사용자는 AnonymousUser 인스턴스



### 로그아웃

> 세션을 삭제하는 로직과 같음

로그아웃 함수

- `logout(request)`
  - HttpRequest 객체를 인자로 받고 반환 값이 없음
  - 사용자가 로그인하지 않은 경우 오류를 발생시키지 않음
  - 현재 요청에 대한 session data를 DB에서 완전히 삭제
  - 클라이언트 쿠키에서도 sessionid가 삭제됨
    - 다른 사람이 동일한 웹 브라우저를 사용하여 로그인하여 이전 사용자의 세션 데이터에 액세스하는 것을 방지하기 위함

```python
# accounts/urls.py

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
```

```python
# accounts/views.py
from django.contrib.auth import logout as auth_logout

@require_POST
def logout(request):
    auth_logout(request)
    return redirect('articles:index')
```

- 로그아웃 페이지가 따로 필요 없음 = GET 요청 x(GET요청 = form)

```django
{# base.html #}
	...
    <form action="{% url 'accounts:logout' %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="Logout">
    </form>
	...
```



### 로그인 사용자에 대한 접근 제한

- 로그인 사용자에 대한 엑세스 제한 2가지 방법
  1. The raw way
     - is_authenticated attribute -> T/F
  2. The login_required decotrator



#### 1. is_authenticated 속성

- User model의 속성 중 하나
- 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성
  - AnonymousUser에 대해서는 항상 False
- 사용자가 인증 되었는지 여부를 알 수 있는 방법
- 권한(permission)과 관련 x -> 사용자가 활성화 상태이거나 유효한 세션을 가지고 있는지도 확인x

```django
{# base.html #}

  <div class="container">
    {% if request.user.is_authenticated %}
      <h3>Hello, {{ user }}</h3>
      <form action="{% url 'accounts:logout' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="Logout">
      </form>
    {% else %}
      <a href="{% url 'accounts:login' %}">Login</a>
    {% endif %}
    {% block content %}
    {% endblock content %}
  </div>
```

- but. 현재 상태로는 로그인 상태임에도 로그인 페이지로 다시 접근 가능



- 로그인한 상태라면 로그인 로직을 수행할 수 없도록 처리

```python
# accounts/views.py

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    ...
```

- 로그인한 사람만 로그아웃 할 수 있도록 수정

```python
# accounts/views.py

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('articles:index')
```

- 인증된 사용자만 게시글 작성할 수 있도록 수정

```django
{# accounts/index.html #}

  {% if request.user.is_authenticated %}
    <a href="{% url 'articles:create' %}">CREATE</a>
  {% else %}
    <a href="{% url 'accounts:login' %}">[새 글을 작성하려면 로그인 하세요</a>
  {% endif %}
```

- but. create 주소만 알면 로그인하지 않은 사용자도 접근 가능 -> view함수 수정해야함



#### 2. login_required decorator

- 사용자가 로그인되어 있지 않으면, settings.LOGIN_URL에 설정된 문자열 기반 절대 경로로 redirect 함
  - LOGIN_URL의 기본 값은 `/accounts/login/`
  - 두 번째 app 이름을 accounts로 했던 이유 중 하나
- 사용자가 로그인되어 있으면 정상적으로 view함수를 실행
- 인증 성공 시 사용자가 redirect 되어야 하는 경로는 "next"라는 쿼리 문자열 매개 변수에 저장됨
  - ex) 아직 로그인 안된 상태에서 create에 접근
  - /accounts/login/?next=/articles/create/

```python
# articles/views.py
from django.contrib.auth.decorators import login_required

@login_required				# 데코레이터 여러 개 사용 가능(위에 있는 것부터 실행)
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        ...
        
@login_required
@require_POST
def delete(request, pk):
    ...
    

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    ...
```



#### next

- query string parameter

- 로그인이 정상적으로 진행되면 갈 주소 keep 해줌
- 별도로 처리해주지 않으면 view에 설정한 redirect 경로로 이동

```python
# accounts/views.py

@require_http_methods(['GET', 'POST'])
def login(request):
    # data = request.GET.get('next')      # 'articles/create/'
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        # ModelForm이 아닌 Form을 상속받음
        # why? 아이디랑 비밀번호 DB에 저장x
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 실제 로그인
            # login 이름 같기 때문에 auth_login으로 바꿔줌
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
        ...
```

- 현재 url로 요청을 보내기 위해 action값 비우기

```django
{# accounts/login.html #}

{% extends 'base.html' %}

{% block content %}
  <h1>LOGIN</h1>
  <hr>
  <form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  <a href="{% url 'articles:index' %}">back</a>
{% endblock content %}

```



#### 데코레이터 충돌

- 비로그인 상태에서 게시글 삭제 시도

```python
# articles/views.py

# @login_required     # 로그인 성공 이후로 redirect는 GET방식이라 아래 데코레이터와 충돌
@require_POST
def delete(request, pk):
    if request.user.is_authenticated:		# GET메서드를 처리하기 위해
        article = get_object_or_404(Article, pk=pk)
        article.delete()
    	return redirect('articles:index')
    return redirect('articles:detail', article.pk)
```







## 2

### 회원 가입

#### UserCreationForm

- 주어진 username과 password로 권한이 없는 새 user를 생성하는 ModelForm

- 3개의 필드
  - username
  - password1
  - password2(비밀번호 확인)

```python
# accounts/urls.py

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
]
```

```python
# accounts/views.py

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)           # 회원가입 완료 후 로그인 상태로 redirect
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    # 빌트인 폼을 쓰고 있으므로 forms.py 따로 만들지 x
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
```





## 회원 탈퇴

> DB에서 사용자를 삭제하는 것과 같음

```python
# acounts/urls.py

...
path('delete/', views.delete, name='delete'),
```

```python
# accounts/views.py

@require_POST
def delete(request):
    request.user.delete()       # 주의! 반드시 화원탈퇴 후 로그아웃 함수 호출
    auth_logout(request)        # 유저 삭제 후 세션 삭제를 위해 logout(필수는 x)
    return redirect('articles:index')
```

```django
{# base.html #}

      <form action="{% url 'accounts:delete' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="회원탈퇴">
      </form>
```





## 회원 정보 수정

#### UserChangeForm

- 사용자의 정보 및 권한을 변경하기 위해 admin 인터페이서에서 사용되는 ModelForm

```python
# accounts/urls.py

path('update/', views.update, name='update'),
```

```python
# accounts/views.py

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

def update(request):
    if request.method == 'POST':
        pass
    else:
        form = UserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)
```

- 이렇게 하면 일반 사용자도 모든 정보를 수정할 수 있음(권한 너무 많음)

  ↓ 해결 방안

```python
# accounts/forms.py

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()        # User 클래스 리턴
        fields = ('email', 'first_name', 'last_name',)
```

or

```python
# accounts/forms.py

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User    # 현재 활성화된 유저 정보를 반환
        fields = ('email', 'first_name', 'last_name',)
```



```python
# accounts/views.py

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# UserChangeForm 대신 CustomUserChangeForm
from .forms import CustomUserChangeForm


def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)
```

```django
{# base.html #}

<a href="{% url 'accounts:update' %}">회원 정보 수정</a>
```





## 비밀번호 변경

#### PasswordChangeForm

- 사용자가 비밀번호를 변경할 수 있도록 하는 Form
- 이전 비밀번호를 입력하여 비밀번호를 변경할 수 있도록 함
- 이전 비밀번호를 입력하지 않고 비밀번호를 설정할 수 있는 SetPasswordForm을 상속받는 서브 클래스
- 회원정보 수정 페이지에서 /accounts/password/ 제시됨

```python
# accounts/urls.py

    path('password/', views.change_password, name='change_password'),
```

```python
# accounts/views.py

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
```



#### 암호 변경 시 세션 무효화 방지

> 비밀번호 변경해도 로그아웃 되지 않도록

- update_session_auth_hash(request, user)
  - 현재 요청과 새 session hash가 파생 될 업데이트 된 사용자 객체를 가져오고, session hash를 적절하게 업데이트
  - 비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치하지 않게 되어 로그인 상태를 유지할 수 없음
  - 암호가 변경되어도 로그아웃되지 않도록 새로운 password hash로 session을 업데이트 함

```python
# accunts/views.py

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
```







