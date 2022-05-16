# Vue + Api 서버 활용

[toc]

## Server & Client

Server

- 리소스(정보, 서비스) 를 제공하는 컴퓨터 시스템
- 정보 & 서비스
  - html
  - json



Client

- 서버에게 그 서버가 맡는 서비스를 요청
- 서버가 요구하는 방식에 맞게 제공
- 서버로부터 반환되는 응답을 사용자에게 적절한 방식으로 표현하는 기능을 가진 시스템
  - 브라우저
  - 포스트맨
  - 파이썬 - request
  - axios : 브라우저라는 클라이언트를 조작하기 위한 라이브러라
  - vue



Client - 서버에 올바른 요청

- 올바른 요청 : URL에 맞게 보낼 것
  - url 규칙 이미 서버에서 정해놓음
  - 메서드도 포함됨



정리

- 서버 : 정보 제공
  - 데이터 베이스가 서버의 존재 이유
- 클라이언트 : 정보 요청 & 표현



## Start Project Model + Serializer





## CORS

**Same-origin policy (SOP)**

- 동일 출처에서 온 문서
- scheme/protocol, host, port가 같을 때만 응답을 받아서 응답을 해줌
- 특정 출처(origin)에서 불러온 문서나 스크립트가 다른 출처에서 가져온 리소스와 상호작용 하는 것을 제한하는 보안 방식
  - 누가 제한? -> 브라우저가



Origin(출처)

- 동일 출처



Cross-Origin Resource Sharing(CORS)

- 추가 HTTP header를 사용
  - 다른 출처의 자원에 접근할 수 있는 권한을 부여하도록 브라우저에 알려주는 체제
- 다른 출처의 리소스를 불러오려면 그 출처에서 올바른 CORS header를 포함한 응답을 반환해야 함



Cross-Origin Resource Sharing Policy (CORS Policy )

- CORS를 사용해 교차 출처 접근을 허용하기
- 서버에 지정할 수 있는 방법



Why CORS?

1. 브라우저 & 웹 애플리케이션 보호
2. Server의 자원 관리
   - 누가 해당 리소스에 접근할 수 있는지 관리 가능



Access-Control-Allow-Origin 응답 헤더

- 예시
  - Access-Control-Allow-Origin : *



django-cor-headers 라이브러리



미들웨어는 순서 중요함

```python
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    ...
]
...
# 특정 origin에게만 교차 출처 허용
CORS_ALLOWED_ORIGINS = [
    'http://localhost:8080',
]

# 모두에게 교차출저 허용(*)
# CORS_ALLOWED_ALL_ORIGINS = True
```







```tex
GET 요청은 상관 없음
AJAX 요청이 문제가 됨
sop에 어긋나는 애들을 금지시킴
예외처리를 하고 싶다면 서버에서 처리해줘야 함
헤더에 적어주면 됨
막는건 브라우저가 막는데 설정은 서버에서 해야 함

node.js
- 프레임워크가 아님
- pip같은 개발 환경임
- 브라우저에만 있는 자바스크립트를 브라우저 이외의 환경에서 쓸 수 있도록 함
- 그 안에 있는 프레임워크가 express.js

Mongo DB, Express React Node.js -> Mern

포트 번호 기본은 80
번호가 다른 것은 한 컴퓨터에서 여러 프로그램인 셈
장고 포트번호는 8000, vue.js는 8080
★ 서버 단에서 해결해야 함
HOW? Access-Control-Allow-Origin response header

클라우드로 통신하려면 프록시 사용

클라이언트가 요청하면 서버는 무조건 요청에 응답함
-> 응답 받기 전에 브라우저가 막아서 안전한지 판단함

문제는 클라이언트가 보고 해결은 서버가 함
```



## Authentication & Authorization

**Authentication**

- 인증, 입증
- 내가 누구인지 확인하는 과정





**Authorization**

- 권한 부여, 허가
- 액세스 권한을 부여하는 과정(절차)
- 권한 부여는 항상 인증을 따라야 함
- 인증이 되었어도 모든 권한을 부여 받는 것은 아님



### DRF Authentication

다양한 인증 방식

1. Session Based
2. Token Based
   - Basic Token
   - JWT
3. Oauth
   - google



Basic Token Authentication

- 토큰 값 넣어서 보낼 때 띄어쓰기 유의할 것



### JWT

- JSON 포맷을 활용하여 요소 간 안전하게 정보를 교환하기 위한 표준 포맷



**JWT 특징**

- 데이터베이스에서 유효성 검사가 필요 없음

- JWT 자체가 인증에 필요한 정보를 모두 갖기 때문

  

- 토큰 탈취 시 서버 측에서 토큰 무효화가 불가능(블랙리스팅 테이블 활용)

- 매우 짧은 유효기간(5min)과 Refresh 토큰을 활용하여 구현
- One Source (JWT) Multi User 가능



로그인 : 토큰 발행

로그아웃 : 토큰 삭제

```python
# settings.py

INSTALLED_APPS = [
    # local
    'accounts',
    'articles',

    # 3rd party apps
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken', # token 기반 auth
    
    # DRF auth
    'dj_rest_auth', # signup 제외 auth 관련 담당

    'corsheaders',
    ...
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}	# 무조건 해줘야 하는 설정
```

```python
# project/urls.py

urlpatterns = [
    ...
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
]
```

↓ url 수정

```python
urlpatterns = [
    ...
    path('api/v1/accounts/', include('accounts.urls')),
    # path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/accounts/', include('dj_rest_auth.urls')),
]
```

- 통일성을 위해 url 수정
- 겹쳐도 상관없음 ->  첫 줄 찾아보고 없으면 아랫줄 url로 감

postman으로 로그인

- post요청
- body -> raw + JSON에 username, password 적어서 요청 보냄
- 토큰값 반환 => authtoken_toekn에 코튼 키 생김

create => login

delete => logout

- Headers에
  - key: Authorization
  - value: Token 발급받은토큰값

read => 토큰 검증



signup

```python
# settings.py

INSTALLED_APPS = [
    # local
    'accounts',
    'articles',

    # 3rd party apps
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken', # token 기반 auth
    
    # DRF auth
    'dj_rest_auth', # signup 제외 auth 관련 담당
    'dj_rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'corsheaders',

    # native apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.siteds',    # dj-rest-auth signup 필요
]

SITE_ID = 1
```

```python
# project/urls.py

urlpatterns = [
    ...
    path('api/v1/accounts/signup', include('dj_rest_auth.registration.urls')),
]
```





- 인증된 사용자에게만 열여줌

- 비인증된 사용자에게는 login, signup만

  ```python
  # settings.py
  
  REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': [
          'rest_framework.authentication.TokenAuthentication',
      ],
      'DEFAULT_PERMISSION_CLASSES': [
          # 모두에게 허용
          # 'rest_framework.permissions.AllowAny',
          # 인증된 사용자만 모든 일이 가능
          'rest_framework.permissions.IsAuthenticated'
      ]
  }
  ```

  

```tex
JWT 자체 알고리즘을 통해 토큰 어쩌고...
JWT 
```

