# REST API

[toc]

## HTTP

- HyperText Transfer Protocol
- HTML 문서와 같은 리소스들을 가져올 수 있도록 하는 프로토콜(규칙, 약속)
  - 요청(request)
  - 응답(response)
- 기본 특성
  - Stateless
  - Connectionless
- 쿠키와 세션을 통해 서버 상태를 요청과 연결하도록 함



**HTTP request methods**

- 자원에 대한 행위(수행하고자 하는 동작)을 정의
- 주어진 리소스(자원)에 수행하길 원하는 행동을 나타냄
  - GET - 조회
  - POST - 작성
  - PUT - 수정
  - DELETE - 삭제



**HTTP response status codes**

- 특정 HTTP 요청이 성공적으로 완료되었는지 여부를 나타냄
  1. Informational responses
  2. Successful responses
  3. Redirection messages
  4. Client error responses
  5. Server error responses



**웹에서의 리소스 식별**

- HTTP 요청의 대상 = resource, 자원
- 리소스는 문서, 사진 또는 기타 어떤 것이든 될 수 있음
- 각 리소스는 리소스 식별을 위해 HTTP 전체에서 사용되는URI(Uniform Resource Identifier)로 식별됨



**URL, URN**

- **URL**(Uniform Resource Locator)
  - 파일 식별자
  - 통합 자원 위치
  - 네트워크 상에 자원이 어디 있는지 알려주기 위한 약속
  - 과거에는 실제 자원의 위치를 나타냄
  - 현재는 추상화된 의미론적인 구성
  - 웹주소, 링크라고도 불림
- **URN**(Uniform Resource Name)
  - 통합 자원 이름
  - URL과 달리 자원의 위치에 영향을 받지 않는 유일한 이름 역할을 함
  - ex)
    - ISBN(국제표준도서번호)



### URI

- Uniform Resource Identifier
  - 통합 자원 식별자
  - 인터넷의 자원을 식별하는 유일한 주소(쩡보의 자원을 표현)
  - 인터넷에서 자원을 식별하거나 이름을 지정하는데 사용되는 간단한 문자열
  - URL, URN ⊂  URI
- URN 사용 비중↓ => 일반적으로 URL은 URI와 같은 의미처럼 사용



**URI의 구조**

- Scheme(protocol)
  - 브라우저가 사용해야 하는 프로토콜
  - http(s), data, file, ftp, mailto
  - `https://`
- Host(Domain name)
  - 요청을 받는 웹 서버의 이름
  - IP address를 직접 사용할 수도 있지만, 실 사용시 불편하므로 웹에서 그리 자주 사용되지는 않음
  - ex) google - 142.251.42.142
  - `www.example.com`
- Port
  - 웹 서버 상의 리소스에 접근하는데 사용되는 기술적인 '문 (gate)'
  - HTTP 프로토콜의 표준 포트
    - HTTP 80
    - HTTPS 443
  - 일반적으론 생략되어 표현됨
  - `:80/`
- Path
  - 웹 서버 상의 리소스 경로
  - 초기에는 실제 파일이 위치한 물리적 위치를 나타냄
  - 현재는 물리적인 위치가 아닌 추상화 형태의 구조로 표현
  - `path/to/myfile.html/`
- Query(Identifier)
  - Query String Parameters
  - 웹 서버에 제공되는 추가적인 매개 변수
  - `&`로 구분되는 key-value 목록
  - `?key=value`
- Fragment
  - Anchor
  - 자원 안에서의 북마크의 한 종류를 나타냄
  - 브라우저에서 해당 문서(HTML)의 특정 부분을 보여주기 위한 방법
  - 브라우저에게 알려주는 요소 -> fragment identifier(부분 식별자)라고 부름
  - `#` 뒤의 부분은 요청이 서버에 보내지지 않음
  - `#quick-start`





## RESTful API

### API

- Application Programming Interface
- 프로그래밍 언어가 제공하는 기능을 수행할 수 있게 만든 인터페이스
  - 애플리케이션과 프로그래밍으로 소통하는 방법
  - CLI는 명령줄
  - GUI는 그래픽(아이콘)
  - API는 프로그래밍을 통해 특정한 기능 수행
- Web API
  - 웹 애플리케이션 개발에서 다른 서비스에 요청을 보내고 응답을 받기 위해 정의된 명세
  - 모든 것을 직접 개발하기보다 여러 Open API를 활용하는 추세
- 응답 데이터 타입
  - HTML, XML, JSON 등
- 대표적인 API 서비스 목록
  - Youtube API
  - Naver Papago API
  - Kakao Map API



### REST

- REpresentational State Transfer
- API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론
  - 규약이나 약속 x -> 반드시 해야되는 것 x
- 네트워크 구조 원리의 모음
  - 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법
- REST 원리를 따르는 시스템을 RESTful이란 용어로 지칭함
- 자원을 정의하는 방법에 대한 고민



- REST의 자원과 주소의 지정 방법
  1. 자원
     - URI
  2. 행위
     - HTTP Method
  3. 표현
     - 자원과 행위를 통해 궁극적으로 표현되는 (추상화된) 결과물
     - JSON으로 표현된 데이터를 제공



### JSON

- JSON(JavaScript Object Notation)
  - JSON is a lightweight data-interchange format
  - JavaScript의 표기법을 따른 단순 문자열
- 특징
  - 사람이 읽거나 쓰기 쉽고 기계가 파싱(해석, 분석)하고 만들어내기 쉬움
    - 영화 API를 딕셔너리 형태로 변환해서 사용
  - 파이썬의 dictionary, 자바스크립트의 object처럼 C 계열의 언어가 갖고 있는 자료구조로 쉽게 변화할 수 있는 key-value 형태의 구조를 갖고 있음



- REST의 핵심 규칙
  1. 정보는 URI로 표현
  2. 자원에 대한 행위는 HTTP Method로 표현
     - GET, POST, PUT, DELETE (R, C, U, D)
- 설계 방법론은 지키지 않았을 때 잃는 것보다 지켰을 때 얻는 것이 훨씬 많음
  - 단, 설계 방법론을 지키지 않더라도 동작 여부에 큰 영향을 미치지 않음



**RESTful API**

- REST 원리에 따라 설계한 API
- RESTful services, 혹은 simply REST services라고도 부름
- 프로그래밍을 통해 클라이언트의 요청에 JSON을 응답하는 서버를 구성



## Response

- 실습

  ```bash
  $ python manage.py migrate
  $ python manage.py seed articles --number=20	# 자동으로 20개의 게시글 랜덤 작성
  ```

  - django_seed

    - 모델 구조에 맞는 더미 데이터 생성
    - `python manage.py seed <클래스명> --number=<원하는 갯수>`
    - INSTALLED_APPS에 등록해줘야 함

    

- Content-Type entity header
  - 데이터의 media type(MIME type, content type)을 나타내기 위해 사용됨
  - 응답 내에 있는 컨텐츠의 컨텐츠 유형이 실제로 무엇인지 클라이언트에게 알려줌



- JsonResponse objects

  - JSON-encoded response를 만드는 HttpResponse의 서브 클래스
  - "safe" parameter
    - True(기본값)
    - dict이외의 객체를 직렬화(Serialization)하려면 False로 설정해야 함

  ```python
  # articles/views.py
  
  def article_json_1(request):
      ...
      return JsonResponse(articles_json, safe=False)
  ```

  



### Serialization

- 직렬화

- 데이터 구조나 객체 상태를 동일하거나 다른 컴퓨터 환경에 저장하고, 나중에 재구성할 수 있는 포맷으로 변환하는 과정

- Serializers in Django

  - Queryset 및 Model Instance와 같은 복잡한 데이터를 JSON, XML 등의 유형으로 쉽게 변환할 수 있는 Python 데이터 타입으로 만들어 줌

  ```python
  def article_json_2(request):
      articles = Article.objects.all()
      # data: 파이썬으로 직렬화된 데이터
      data = serializers.serialize('json', articles)
      # 컨텐트 타입은 json
      return HttpResponse(data, content_type='application/json')
  ```



3. Response - Django Serializer

   - Django의 내장 HttpResponse를 활용한 JSON 응답 객체

   - 주어진 모델 정보를 활용하기 때문에 이전과 달리 필드를 개별적으로 직접 만들어 줄 필요 없음

4. Response - Django REST Framework ★

   - Django REST frameworkd(DRF) 라이브러리를 사용한 JSON 응답

   ```bash
   $ pip install djangorestframework
   ```

   ```python
   # settings.py
   
   INSTALLED_APPS = [
       ...
       'rest_framework',
   ]
   ```

   ```python
   # articles/views.py
   
   # @api_view(['GET'])
   @api_view()
   def article_json_3(request):
       articles = Article.objects.all()
       # many: 단일 객체가 아닐 때 True
       serializer = ArticleSerializer(articles, many=True)
       return Response(serializer.data)
   ```

   ```python
   # articles/serializers.py
   
   from rest_framework import serializers
   from .models import Article
   
   
   class ArticleSerializer(serializers.ModelSerializer):
   
       class Meta:
           model = Article
           fields = '__all__'
   ```

   - 장고가 모델폼과 구조를 동일하게 제공해줌
   - 시리얼라이즈 해주는 도구



### Django REST Framework (DRF)

- Web API 구축을 위한 강력한 Toolkit을 제공하는 라이브러리
- DFR의 Serializer는 Django의 Form 및 ModelForm 클래스와 매우 유사하게 구성되고 작동함



- Web API
  - 웹 애플리케이션 개발에서 다른 서비스에 요청을 보내고 응답을 받기 위해 정의된 명세

|          | Django    | DRF        |
| -------- | --------- | ---------- |
| Response | HTML      | JSON       |
| Model    | ModelForm | Serializer |





## Single Model

### DRF with Single Model

- 단일 모델의 data를 직렬화하여 JSON으로 변환하는 방법에 대한 학습
- 단일 모델을 두고 CRUD로직을 수행 가능하도록 설계
- API 개발을 위한 핵심 기능을 제공하는 도구 활용
  - DRF built-in form
  - Postman(https://www.postman.com/)



**[참고] Postman**

- API를 구축하고 사용하기 위해 여러 도구를 제공하는 API 플랫폼
- 설계, 테스트, 문서화 등의 도구를 제공함으로써 API를 더 빠르게 개발 및 생성할 수 있도록 도움



**ModelSerializer**

- 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut

- 아래 핵심 기능을 제공

  1. 모델 정보에 맞춰 자동으로 필드 생성
  2. serializer에 대한 유효성 검사기를 자동으로 생성
  3. `.create()` & `.update()`의 간단한 기본 구현이 포함됨

- Model의 필드를 어떻게 직렬화 할 지 설정하는 것이 핵심

- 이 과정은 Django에서 Model의 필드를 설정하는 것과 동일함

  ```python
  from rest_framework import serializers
  from .models import Article
  
  
  class ArticleSerializer(serializers.ModelSerializer):
  
      class Meta:
          model = Article
          fields = '__all__'
  ```

  

※ shell_plus

serializer는 직접 import 해줘야 함



'many' argument

- many=Ture
  - Serializing multiple objects
  - 단일 인스턴스 대신 QuerySet 등을 직렬화하기 위해서는 serializer를 인스턴스화 할 때 many-True를 키워드 인자로 전달해야 함



1. GET - Article List

   ```python
   # articles/urls.py
   
   from django.urls import path
   from . import views
   
   
   # 템플릿이 없으니 앱 이름 필요 x
   urlpatterns = [
       path('articles/', views.article_list),
   ]
   ```

   ```python
   # articles/views.py
   
   from rest_framework.response import Response
   from rest_framework.decorators import api_view
   from django.shortcuts import get_list_or_404
   from django.shortcuts import render
   from .models import Article
   from .serializers import ArticleListSerializer
   
   
   # @api_view()
   @api_view(['GET'])
   def article_list(request):
       # articles = Article.objects.all()
       articles = get_list_or_404(Article)
       serializer = ArticleListSerializer(articles, many=True)
       return Response(serializer.data)
   ```

   - api_view decorator
     - **필수적으로 작성**해야 view 함수가 정상적으로 동작함
     - 기본적으로 GET 메서드만 허용됨. 다른 메서드 요청에 대해서는 405 Method Not Allowed로 응답
     - View 함수가 응답해야 하는 HTTP 메서드의 목록을 리스트의 인자로 받음

2. GET - Article Detail

   ```python
   # articles/serializers.py
   
   from rest_framework import serializers
   from .models import Article
   
   
   class ArticleListSerializer(serializers.ModelSerializer):
       
       class Meta:
           model = Article
           fields = ('id', 'title',)
   
   
   # 단일 객체 조회시
   class ArticleSerializer(serializers.ModelSerializer):
       
       class Meta:
           model = Article
           fields = '__all__'
   ```

   ```python
   # articles/urls.py
   
   urlpatterns = [
       path('articles/', views.article_list),
       path('articles/<int:article_pk>/', views.article_detail),
   ]
   ```

   ```python
   # articles/views.py
   
   @api_view(['GET'])
   def article_detail(request, article_pk):
       article = get_object_or_404(Article, pk=article_pk)
       serializer = ArticleSerializer(article)
       return Response(serializer.data)
   ```

3. POST - Create Article

   - 201 Created 상태 코드 및 메시지 응답
   - RESTful 구조에 맞게 작성
     1. URI는 자원을 표현
     2. 자원을 조작하는 행위는 HTTP Method
   - article_list 함수로 게시글을 조회하거나 생성하는 행위를 모두 처리 가능

   ```python
   # articles/views.py
   
   @api_view(['GET', 'POST'])
   def article_list(request):
       if request.method == "GET":
           # articles = Article.objects.all()
           articles = get_list_or_404(Article)
           serializer = ArticleListSerializer(articles, many=True)
           return Response(serializer.data)
       # 명확하게 구분하기 위해 else대신 elif 쓸 것
       elif request.method == "POST":
           serializer = ArticleSerializer(data=request.data)
           if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
           return Response(serializer.errors)
   ```



**Status Codes in DRF**

- DRF에는 status code를 보다 명확하고 읽기 쉽게 만드는 데 사용할 수 있는 정의된 상수 집합을 제공
- status 모듈에 HTTP status code 집합이 모두 포함되어 있음
- 단순히 status=201 같은 표현으로도 사용할 수 있지만 DRF는 권장하지 않음



**'raise_exception' argument**

- raise_exception 작성

  ```python
  @api_view(['GET', 'POST'])
  def article_list(request):
      if request.method == "GET":
          # articles = Article.objects.all()
          articles = get_list_or_404(Article)
          serializer = ArticleListSerializer(articles, many=True)
          return Response(serializer.data)
      # 명확하게 구분하기 위해 else대신 elif 쓸 것
      elif request.method == "POST":
          serializer = ArticleSerializer(data=request.data)
          if serializer.is_valid(raise_exception=True):
              serializer.save()
              return Response(serializer.data, status=status.HTTP_201_CREATED)
          # raise_exception인자를 사용하면 굳이 에러를 다시 리턴하지 않아도 됨
          # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  ```

- Raising an exception on invalid data

- `is_valid()`는 유효성 검사 오류가 있는 경우 serializers.ValidationError 예외를 발생시키는 선택적 raise_exception 인자를 사용할 수 있음

- DRF에서 제공하는 기본 예외 처리기에 의해 자동으로 처리됨
- 기본적으로 HTTP status code 400을 응답으로 반환함



4. DELETE - Delete Article

   - 204 No Content 상태 코드 및 메시지 응답

   - article_detail 함수로 상세 게시글을 조회하거나 삭제하는 행위 모두 처리 가능

     ```python
     # articles/views.py
     
     @api_view(['GET', 'DELETE'])
     def article_detail(request, article_pk):
         article = get_object_or_404(Article, pk=article_pk)
         if request.method == 'GET':
             serializer = ArticleSerializer(article)
             return Response(serializer.data)
         elif request.method == 'DELETE':
             article.delete()
             data = {
                 'delete': f'데이터 {article_pk}번이 삭제되었습니다.',
             }
             return Response(data, status=status.HTTP_204_NO_CONTENT)
     ```

     

5. PUT - Update Article

   ```python
   # articles/views.py
   
   @api_view(['GET', 'DELETE', 'PUT'])
   def article_detail(request, article_pk):
       ...
       elif request.method == 'PUT':
           # serializer = ArticleSerializer(article, data=request.data)
           serializer = ArticleSerializer(article, request.data)
           if serializer.is_valid(raise_exception=True):
               serializer.save()
               return Response(serializer.data)
   ```

   

## 1:N Relation

### DRF with 1:N Relation

데이터베이스 초기화 후 Comment 모델 작성

```python
# articles/models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

```python
# articles/serializers.py

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
```

```python
# articles/urls.py

urlpatterns = [
    ...
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
]
```

```python
# articles/views.py

@api_view(['GET'])
def comment_list(request):
    comments = get_list_or_404(Comment)
    serializers = CommentSerializer(comments, many=True)
    return Response(serializers.data)
```



#### Read Only Field(읽기 전용 필드)

- 어떤 게시글에 작성하는 댓글인지에 대한 정보를 form-data로 넘겨주지 않았기 때문에 직렬화하는 과정에서 article 필드가 유효성 검사(is_valid)를 통과하지 못함

- 읽기 전용 필드(read_only_fields)설정을 통해 직렬화하지 않고 반환 값에만 해당 필드가 포함되도록 설정할 수 있음

  ```python
  # articles/serializers.py
  
  class CommentSerializer(serializers.ModelSerializer):
  
      class Meta:
          model = Comment
          fields = '__all__'
          read_only_fields = ('article',)
  ```



### 1:N Serializer

1. 특정 게시글에 작성된 댓글 목록 출력하기

   - Serializer는 기존 필드를 override하거나 추가 필드를 구성할 수 있음

   - 우리가 작성한 로직에서는 크게 2가지 형태로 구성할 수 있음

     1. PrimaryKeyRelatedField

        ```python
        # articles/serializers.py
        
        class ArticleSerializer(serializers.ModelSerializer):
            comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
            
            class Meta:
                model = Article
                fields = '__all__'
        ```

        - comment_set 필드 값을 form-data로 받지 않으므로 read_only=True 설정 필요

        

     2. Nested relationships
     
        - 모델 관계상으로 참조된 대상은 참조하는 대상의 표현(응답)에 포함되거나 중첩(nested)될 수 있음
        - 이러한 중첩된 관계는 serializers를 필드로 사용하여 표현할 수 있음
     
        ```python
        # articles/serializers.py
        
        class CommentSerializer(serializers.ModelSerializer):
        
            class Meta:
                model = Comment
                fields = '__all__'
                read_only_fields = ('article',)
        
        
        # 단일 객체 조회시
        class ArticleSerializer(serializers.ModelSerializer):
            # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
            # 본인을 참조하는 시리얼라이즈를 호출할 수 있음
            comment_set = CommentSerializer(many=True, read_only=True)
            
            class Meta:
                model = Article
                fields = '__all__'
        ```

2. 특정 게시글에 작성된 댓글의 개수 구하기

   - comment_set 매니저는 모델 관계로 인해 자동으로 구성됨
     - 커스텀 필드 구성하지 않아도 comment_set이라는 필드명을 fields 옵션에 작성만 해도 사용 가능
   - comment_count와 같이 별도의 값을 위한 필드를 사용하려는 경우
     - 자동으로 구성되는 매니저 아님 -> 직접 필드 작성해야 함
   
   ```python
   # articles/serializers.py
   
   class ArticleSerializer(serializers.ModelSerializer):
       comment_set = CommentSerializer(many=True, read_only=True)
       # comment_set은 정해져 있는 이름 -> 그냥 직관적으로 보이기 위해 comment_count로 작명
       comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
   
       class Meta:
           model = Article
           fields = '__all__'
   ```
   
   - **'source'** arguments
     - 필드를 채우는 데 사용할 속성의 이름
     - 점 표기법(dot notation)을 사용하여 속성을 탐색 할 수 있음
       - comment_set 이라는 필드에 .(dot)을 통해 전체 댓글의 개수 확인 가능
