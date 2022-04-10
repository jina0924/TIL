# HTTP request & Image

[toc]

## Handling HTTP requests

- 장고에서 HTTP 요청을 처리하는 방법
  1. Django shortcut functions
  2. View decorators



### 1. Django shortcuts functions

- shortcuts functions 종류
  - `render()`
  - `redirect()`
  - `get_object_or_404()`
  - `get_list_or_404()`



#### get_object_or_404()

- 해당 객체가 없을 경우 DoesNotExist 예외 대신 Http 404를 raise
- 코드 실행 단계에서 발생한 예외 및 에러에 대해서 브라우저는 http status code 500으로 인식함
- 상황에 따라 적절한 예외처리
- 클라이언트에게 올바른 에러 상황을 전달



HTTP 응답 코드

- 100번대 : 정보 제공 응답
- 200번대 : 성공
- 300번대 : 리다이렉트
- 400번대 : 클라이언트 오류
- 500번대 : 서버 오류



- get_object_or_404 사용

  ```python
  # articles/views.py
  
  from django.shortcuts import render, redirect, get_object_or_404
  
  def detail(request, pk):
      # article = Article.objects.get(pk=pk)
      article = get_object_or_404(Article, pk=pk)
      context = {
          'article': article,
      }
      return render(request, 'articles/detail.html', context)
  ```

- get_list_or_404는 API로 서버를 쓸 때 사용

  - 현재 만드는 게시판 형태에서는 적합하지 않음(글이 없을 때 빈 게시판이 아닌 404를 보여줌)





### 2. Django View decorators

- 다양한 HTTP 기능을 지원하기 위해 view 함수에 적용할 수 있는 여러 데코레이터 제공

- 원본 함수를 수정하지 않으면서 추가 기능만을 구현할 때 사용

- Allowed HTTP methods

  - 요청 메서드에 따라 view 함수에 대한 엑세스를 제한
  - 요청이 조건을 충족시키지 못하면 HttpResponseNotAllowedd을 return(405 Method Not Allowed)
    - ex) 삭제 시 get 요청이면 redirect인데 왜 redirect됐는지 알려줌

  1. require_http_methods()
     - 괄호 안에 받을 수 있는 요청 리스트 형태로 나열
  2. require_POST()
     - view 함수가 POST method 요청만 승인하도록 하는 데코레이터 -> delete에서 필요
  3. require_safe()
     - view 함수가 GET 및 HEAD method만 허용하도록 요구하는 데코레이터 -> index, detail

  ```python
  # articles/views.py
  
  from django.views.decorators.http import require_http_methods, require_POST, require_safe
  
  @require_http_methods(['GET', 'POST'])		# GET, POST 이외의 요청에서 405
  def create(request):
      if request.method == 'POST':
          ...
          
  @require_http_methods(['GET', 'POST'])
  def update(request, pk):
      # article = Article.objects.get(pk=pk)
      article = get_object_or_404(Article, pk=pk)
      ...
      
  @require_POST
  def delete(request, pk):
      # article = Article.objects.get(pk=pk)
      article = get_object_or_404(Article, pk=pk)
      # if request.method == 'POST':
      article.delete()
      return redirect('articles:index')
      # else:
          # return redirect('articles:detail', article.pk)
  ```





## Media files

- 사용자가 웹에서 업로드하는 정적 파일(user-uploaded)
- 유저가 업로드 한 모든 정적 파일



- ImageField()
  - 이미지 업로드에 사용하는 모델 필드
  - FileField를 상속받는 서브 클래스이기 때문에 FileField의 모든 속성 및 메서드를 사용 가능
  - 업로드 된 객체가 유효한 이미지인지 검사함
  - ImageField 인스턴스는 최대 길이가 100자인 문자열로 DB에 생성됨
    - DB에 파일 올라감x. 경로값 저장됨
  - max_length 인자를 사용하여 최대 길이 변경 가능
  - Pillow 라이브러리 필요

- FileField()
  - 파일 업로드에 사용하는 모델 필드
  - 2개의 선택 인자
    1. upload_to
    2. storage



- ImageField 작성
  - upload_to='images/'
    - 실제 이미지가 저장되는 경로를 지정
  - blank=True
    - 이미지 필드에 빈 값(빈 문자열)이 허용되도록 설정(이미지를 선택적으로 업로드 할 수 있도록)



- 'upload_to' argument

  - 업로드 디렉토리와 파일 이름을 설정하는 2가지 방법을 제공
    1. 문자열 값이나 경로 지정
    2. 함수 호출

  ```python
  # articles/models.py
  
  from django.db import models
  
  # Create your models here.
  class Article(models.Model):
      title = models.CharField(max_length=10)
      content = models.TextField()
      image = models.ImageField(upload_to='images/', blank=True)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```



- ''upload_to' argument - 1. 문자열 경로 지정 방식
  - 파이썬의 strftime()형식이 포함될 수 있음
- 'upload_to' argument - 2. 함수 호출 방식(오늘 사용x)



- Model field option - "blank"
  - 기본 값: False
  - True인 경우 필드를 비워 둘 수 있음
  - 유효성 검사에서 사용 됨(is_valid)
    - 모델 필드에 blank=True를 작성하면 form 유효성 검사에서 빈 값을 입력할 수 있음



- Model field option - "null"
  - 기본 값: False
  - True인 경우 django는 빈 값에 대해 DB에 NULL로 저장
    - NULL은 빈 값이라는 데이터 타입
    - ''는 비어있음(?)
  - 주의사항
    - 문자열 기반 필드(CharField, TextField)에는 사용하는 것 피해야 함
- blank & null 비교
  - blank
    - validation-related
  - null
    - database-related
    - form에서 빈 값을 허용하려면 blank=True를 설정해야 함



- ImageField를 사용하기 위한 몇 가지 단계
  1. settings.py에 MEDIA_ROOT, MEDIA_URL 설정
  2. upload_to 속성을 정의하여 업로드 된 파일에 사용할 MEDIA_ROOT의 하위 경로를 지정
  3. 업로드 된 파일의 경로는 django가 제공하는 'url' 속성을 통해 얻을 수 있음



#### MEDIA_ROOT

- 사용자가 업로드 한 파일들을 보관할 디렉토리의 절대 경로

- 장고는 성능을 위해 업로드 파일은 데이터베이스에 저장하지 않음

  - 실제 데이터베이스에 저장되는 것은 파일의 경로(문자열)

  ```python
  # settings.py
  
  MEDIA_ROOT = BASE_DIR / 'media'
  ```

  

#### MEDIA_URL

- 업로드 된 파일의 주소(url)을 만들어 주는 역할
- 비어있지 않은 값으로 설정 한다면 반드시 slash(/)로 끝나야 함



```python
# crud/settings.py

MEDIA_ROOT = BASE_DIR / 'media'

MEDIA_URL = '/media/'
```

```python
# crud/urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```



### Image Upload

```django
{# articles/create.html #}
  <h1>CREATE</h1>
  <hr>
  <form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">
```

- multipart / form-data
  - 파일/이미지 업로드 시에 반드시 사용해야 함(전송되는 데이터의 형식을 지정)
  - `<input type="file">`을 사용할 경우에 사용
    - ImageField를 썼기 때문에 input type와 accept를 알아서 지정해줌



- input 요소 - accept 속성
  - 입력 허용할 파일 유형을 나타내는 문자열
  - 파일을 검증하는 것은 아님
  - 파일 업로드 시 허용할 파일 형식에 대해 자동으로 필터링



- 이미지 파일은 POST가 아닌 FILES 메서드에 담겨서 옴

  - data=request.POST, file=request.FILES

  ```python
  # articles/views.py
  
  def create(request):
      if request.method == 'POST':
          form = ArticleForm(request.POST, request.FILES)
          ...
  ```

- 이미지 업로드하면 media 폴더 자동 생성됨
  - why? settings.py 에서 MEDIA_ROOT = BASE_DIR / 'media/'로 지정해놨기 때문

```django
{# articles/detail.html #}

{% extends 'base.html' %}

{% block content %}
  <h1>DETAIL</h1>
  <h3>{{ article.pk }}번째 글</h3>
  <img src="{{ article.image.url }}" alt="{{ article.image }}">
```

- {{ article.image }}로 하면 파일명으로 제시됨



### 이미지 수정

- 이미지는 바이너리 데이터(하나의 덩어리)이기 때문에 텍스트처럼 일부만 수정하는 것은 불가능

- -> 새로운 사진으로 덮어 씌우는 방식을 사용

  ```django
  {# articles/update.html #}
  
  {% block content %}
    <h1>UPDATE</h1>
    <hr>
    <form action="{% url 'articles:update' article.pk %}" method="POST" enctype="multipart/form-data">
  ```

  ```python
  # articles/views.py
  
  def update(request, pk):
      article = Article.objects.get(pk=pk)
      if request.method == 'POST':
          form = ArticleForm(request.POST, request.FILES, instance=article)
          ...
  ```

  ```django
  {# articles/detail.html #}
  
    {% if article.image %}
      <img src="{{ article.image.url }}" alt="{{ article.image }}">
    {% endif %}
  ```

  

### Image Resizing

- css로 직접 사이즈를 조정할 수도 있지만(원본 수정x. 출력만 바꿈)
- 업로드 될 때 이미지 자체를 resizing 하는 것을 고려하기

- django-imagekit 라이브러리 활용

  ```bash
  $ pip install django-imagekit
  ```

  ```python
  # crud/settings.py
  
  INSTALLED_APPS = [
      'articles',
      'django_extensions',
      'imagekit',
  ```



- 원본 이미지를 재가공하여 저장(원본x, 썸네일o)

```python
# articles/models.py

from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # image = models.ImageField(upload_to='images/', blank=True)
    image = ProcessedImageField(
        blank=True,
        upload_to='thumbnails/',
        processors=[Thumbnail(200, 300)],
        format='JPEG',
        options={'quality': 90})
```


