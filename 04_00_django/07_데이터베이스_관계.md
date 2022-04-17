

# 데이터베이스 관계

[toc]

## Foreign Key

- 관계형 데이터베이스에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키
- 참조하는 테이블 - 속성(필드) = 참조되는 테이블의 기본 키(Primary Key)
- 참조하는 테이블의 외래 키는 참조되는 테이블 행 1개에 대응
  - 존재하지 않은 행을 참조 x
- 참조하는 테이블의 행 여러 개가 참조되는 테이블의 동일한 행을 참조할 수 있음
- Foreign Key는 1:N에서 N이 가짐



특징

- 키를 사용하여 부모 테이블의 유일한 값을 참조(참조 무결성)
  - 참조 무결성이란?
  - 2개의 테이블 간의 일관성
- 외래 키는 반드시 부모 테이블의 유일한 값이어야함(반드시 기본 키일 필요는 x)



### ForeignKey field

- A many-to-one-relationship
- 2개의 위치 인자 반드시 필요
  1. 참조하는 model class
     - comment입장에선 article
  2. on_delete 옵션
- migrate 작업 시 필드 이름에  _id를 추가하여 데이터베이스 열 이름 만듦



- comment 모델 정의하기

  ```python
  # articles/models.py
  
  class Comment(models.Model):
      # 참조하는 테이블의 소문자 & 단수형으로 작성
      # why? 누굴 참조하는지 나타내기 위해
      # 순서는 상관 없음
      article = models.ForeignKey(Article, on_delete=models.CASCADE)
      content = models.CharField(max_length=200)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)_
  
      # 객체의 출력 방식을 지정
      # 원래는 Object(1) / Object(2)가 댓글 1 / 댓글2로 보임
      # 관리자 페이지에서도 바뀌어 보임
      def __str__(self):
          return self.content
  ```

  ※ 모델이 2개 이상일 때 모델끼리 연결고리가 있어야 할 필요는 x



- ForeignKey arguments - 'on_delete'

  - 외래 키가 참조하는 객체가 사라졌을 때 외래 키를 가진 객체를 어떻게 처리할 것인지를 정의
  - ForeignKey 필드의 필수 인자
  - on_delete 옵션에 사용 가능한 값을
    - CASCADE : 부모 객체가 삭제 됐을 때 이를 참조하는 객체도 삭제
    - PROTECT
    - SET_NULL
    - SET_DEFAULT
    - SET()
    - DO_NOTHING
    - RESTRICT



[참고] 데이터 무결성

1. 개체 무결성
2. 참조 무결성
3. 범위(도메인) 무결성



- Migration
  - 작성 순서에 상관없이 마이그레이트 하면 마지막에 생김
  - articles_comment 테이블의 외래 키 컬럼 확인 (필드 이름에 _id가 추가됨)
    - article_id



- 데이터베이스의 ForeignKey 표현
  - 만약 ForeignKey 인스턴스를 abcd로 생성했다면 abcd_id로 만들어짐
  - 명시적인 모델 관계 파악을 위해 참조하는 클래스 이름의 소문자 & 단수형으로 작성하는 것을 권장(1:N)



### 댓글 생성 연습

```bash
$ python manage.py shell_plus
```

- 댓글 생성 시도

  ```shell
  In [1]: comment = Comment()
  In [3]: comment.content = 'first comment'
  In [4]: comment.save()
  ...
  IntegrityError: NOT NULL constraint failed: articles_comment.article_id
  
  In [5]: article = Article.objects.create(title='title', content='content')
  
  In [6]: article.pk
  Out[6]: 1
  # comment.article_id = article.pk
  # comment.article = article <- 권장
  In [8]: comment.article = article
  In [9]: comment.save()
  
  In [11]: comment.content
  Out[11]: 'first comment'
  
  In [12]: comment.article	# 참조하는 대상을 바로 알 수 있음
  Out[12]: <Article: title>
  
  In [13]: comment.article.pk
  Out[13]: 1
  
  In [14]: comment.article.content
  Out[14]: 'content'
  
  In [15]: comment = Comment(content='second comment', article=article)
  In [16]: comment.save()
  
  In [18]: comment.article.pk		# 객체 위주로 찾아보기
  Out[18]: 1
  
  In [19]: comment.article_id		# 테이블에 직접 접근
  Out[19]: 1
  ```

  ```python
  # articles/admin.py
  from .models import Article, Comment
  
  admin.site.register(Comment)
  ```



### 1:N 관계 related manager

- 역참조('comment_set')
  - `article.comment_set`
    - comment_set : API
    - comment의 모든 정보를 가져옴

  - Article(1) → Comment(N)
  - Article에선 겉으로 바뀐 점이 아무것도 없음
    - Article 클래스에는 Comment 와의 어떠한 관계도 작성되어 있지 않음

- 참조('article')
  - `comment.article`
  - Comment(N) → Article(1)
  - 실제 ForeignKey는 Comment 클래스에서 작성됨


```shell
In [1]: article = Article.objects.get(pk=1)
In [3]: dir(article)
Out[3]: 
['DoesNotExist',
...
 'comment_set',
 ...]
In [5]: article.comment_set.all()
Out[5]: <QuerySet [<Comment: first comment>, <Comment: second comment>]>

In [7]: comments = article.comment_set.all()
In [9]: for comment in comments:
   ...:     print(comment.content)
   ...: 
first comment
second comment

In [10]: comment = Comment.objects.get(pk=1)
In [12]: comment.article_id
Out[12]: 1
In [13]: comment.article.content
Out[13]: 'content'
```

- ForeignKey arguments - `'related_name'`

  - 역참조 시 사용할 이름('model_set' manager)을 변경할 수 있는 옵션

  ```python
  # articles/models.py
  
  class Comment(models.Model):
      article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
  ```

  - 이렇게 변경하면 article.comment_set 사용 불가 → article.comments
  - but, 1:N 에서는 권장 x



## Comment CREATE

### CommentForm 작성

```python
# articles/forms.py
from .models import Article, Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'
```

- 이렇게 하면 댓글 작성시 작성할 게시글 선택요소도 나타나게 됨

  ↓ 해결 방법

```python
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)
```



```python
# articles/views.py
from .forms import ArticleForm, CommentForm


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)
```

```django
{# articles/detail.html #}

{% block content %}
  ...
  <a href="{% url 'articles:index' %}">back</a>
  <hr>
  <form action="" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit" value="댓글 작성">
  </form>
{% endblock content %}
```



### 댓글 작성 로직

```python
# articles/urls.py

app_name = 'articles'
urlpatterns = [
    ...
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
]
```

```python
# articles/views.py

@require_POST
def comment_create(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # comment_form.save()       # 이렇게 하면 어디 게시글에 작성하는 댓글안지 알 수 없음(IntegrityError...NOT NULL...articles_comment.article_id)
            comment = comment_form.save(commit=False)       # commit=False: DB에 저장x but. 인스턴스는 만들어줌
            comment.article = article       # DB에 저장하기 전에 몇 번 게시글인지 제시
            comment.save()
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')
```

```django
{# articles/detail.html #}

{% block content %}
  ...
  <a href="{% url 'articles:index' %}">back</a>
  <hr>
  <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
    ...
  </form>
{% endblock content %}
```



### save(commit=False)

- 기본값은 True

- Create, but don't save the new instance
- 아직 데이터베이스에 저장되지 않은 인스턴스를 반환
- 저장하기 전에 객체에 대한 사용자 지정 처리를 수행할 때 유용하게 사용



## Comment READ

```python
# articles.views.py

@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    # 조회한 article의 모든 댓글을 조회(역참조)
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments
    }
    return render(request, 'articles/detail.html', context)
```

```django
{# articles/detail.html #}

...
  <a href="{% url 'articles:index' %}">back</a>
  <hr>
  <h4>댓글 목록</h4>
  <ul>
    {% for comment in comments %}
      <li>{{ comments.content }}</li>
    {% endfor %}
  </ul>
```





## Comment DELETE

```python
# articles/urls.py

app_name = 'articles'
urlpatterns = [
    ...
    # path('<int:comment_pk>/comment/delete/', views.comment_delete, name='comment_delete'),
    path('<int:article_pk>/comment/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
    # 이렇게 적는 이유: 다른 url과 통일성을 위해
]
```

```python
# articles/views.py

# def comment_delete(request, comment_pk):
#     comment = Comment.objects.get(pk=comment_pk)
#     article = comment.article.pk
#     comment.delete()
#     return redirect('articles:detail', article)


@require_POST
def comment_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()
    return redirect('articles:detail', article_pk)
```

```django
{# articles/detail.html #}

  <h4>댓글 목록</h4>
  <ul>
    {% for comment in comments %}
      <li>
        {{ comment.content }}
        <form action="{% url 'articles:comment_delete' article.pk comment.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="삭제">
        </form>
      </li>
    {% endfor %}
  </ul>
```

:question:



## Customizing authentication in Django

### Substituting a custom User model

User 모델 대체하기

- 일부 프로젝트에서는 Django의 내장 User 모델이 제공하는 인증 요구사항이 적절하지 않을 수 있음
  - ex) username 대신 email을 식별 토큰으로 사용하는 사이트
- AUTH_USER_MODEL값을 제공 -> default user model을 재정의할 수 있도록 함

- 기본 사용자 모델이 충분하더라도 커스텀 유저 모델을 설정하는 것을 강력히 권장
  - 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야 함



**AUTH_USER_MODEL**

- User를 나타내는데 사용하는 모델
- 프로젝트가 진행되는 동안 변경할 수 없음
- 기본 값: `'auth.User'`(auth 앱의 User 모델)



Custom User 모델 정의하기 -> 장고 시작할 때 마다 할 것

```python
# accounts/models.py

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass		# 나중에 바꿀 여지를 만들어 두는 것
```

```python
# 프로젝트명/settings.py

AUTH_USER_MODEL = 'accounts.User'
```

```python
# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
admin.site.register(User, UserAdmin)
```



- 초기화 방법
  1. db.sqlite3 파일 삭제
  2. migrations 파일 모두 삭제(파일명에 숫자가 붙은 파일만 삭제)



### Custom user & Built-in auth forms

회원가입 시도 후 AttributeError 발생

- 회원가입시 사용하는 폼: UserCreationForm
- UserCreationForm과 UserChangeForm은 기존 내용 User 모델을 사용한 ModelForm 이기 때문에 커스텀 User 모델로 대체해야 함

```python
# accounts/forms.py

from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model      # 현재 장고 프로젝트에 활성화된 user모델 호출함(User는 직접 참조하지x)


class CustomUserChangeForm(UserChangeForm):

    # password = None

    class Meta:
        model = get_user_model() # User
        fields = ('email', 'first_name', 'last_name',)


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()	# 현재 활성화된 accounts.user모델을 return
        fields = UserCreationForm.Meta.fields + ('email',)       # 기존엔 id, pwd1, pwd2였는데 거기에 이메일 추가
```

```python
# accounts/views.py
from .forms import CustomUserChangeForm, CustomUserCreationForm


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
```



`get_user_model()`

- **현재 프로젝트에서 활성화된 사용자 모델**(active user model)을 반환
  - settings.py의 AUTH_USER_MODEL
  - User 모델을 커스터마이징한 상황에서는 Custom User 모델을 반환
- -> Django는 User 클래스를 직접 참조하는 대신 django.contrib.auth.get_user_model()을 사용하여 참조해야 한다고 강조



## Model Relationship Ⅱ

### USER - Article (1 : N)

> Foreign Key -> Article이 들고 있어야 함

User 모델 참조하기

1. settings.AUTH_USER_MODEL

   - 문자열 반환

   - models.py에서 User 모델을 참조할 때 사용

2. get_user_model()

   - User Object 반환

   - models.py가 아닌 다른 모든 곳에서 유저 모델을 참조할 때 사용



[참고] 장고에서 app이 실행되는 순서

1. INSTALLED_APP에서 순차적으로 APP IMPORT
2. 각 앱의 models를 import



```python
# articles/models.py

from django.conf import settings


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

```bash
$ python manage.py makemigrations
You are trying to add a non-nullable field 'user' to article without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 1		#### 현재 화면에서 기본 값을 설정하겠다
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> 1				#### 기존 테이블에 추가되는 user_id필드의 값을 1로 설정하겠다
Migrations for 'articles':
  articles\migrations\0002_article_user.py
    - Add field user to article
$ python manage.py mirate
```

- 이 상태에선 create시 user 선택란 나옴(why? 1:N 관계니까)

  ↓ forms 수정할 것

```python
# articles/forms.py

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        exclude = ('user',)
```

- 글 저장 안됨(why? 작성자 정보(article.user)가 누락되었기 때문)

  ↓ create 함수 수정

```python
# articles/views.py

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```

- 삭제함수 변경
  - 자신이 작성한 게시글만 삭제 가능하도록 설정

```python
# articles/views.py

@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user.is_authticated:
        if request.user == article.user:        # 삭제 요청한 유저 == 게시글 작성 유저
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)
```

- 수정 함수 변경

```python
# articles/views.py


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                article = form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
```

- read 페이지 수정

```python
{# articles/index.html #}

{% extends 'base.html' %}

{% block content %}
  ...
  <hr>
  {% for article in articles %}
    <p>작성자: {{ article.user }}</p>
    ...
```

```django
{# articles/detail.html #}

{% block content %}
  ...
  {% if request.user == article.user %}
    <a href="{% url 'articles:update' article.pk %}">수정</a>
    <form action="{% url 'articles:delete' article.pk %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="삭제">
    </form>
  {% endif %}

```

- 해당 게시글 사용자가 아니라면 수정, 삭제 못하도록 아예 버튼을 안보이게 만듦



### User - Comment (1:N)

```python
# 프로젝트명/models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ...
```

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

- 댓글 작성 안됨

  ↓ 댓글 작성 함수 수정

```python
# articles/views.py

@require_POST
def comment_create(request, pk):
    ...
            comment = comment_form.save(commit=False)       # commit=False: DB에 저장x but. 인스턴스는 만들어줌
            comment.article = article       # DB에 저장하기 전에 몇 번 게시글인지 제시
            comment.user = request.user
            comment.save()
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')
```



- 비로그인 유저에게는 댓글 form 출력 숨김

```django
{# articles/detail.html #}
    ...
      </ul>
  {% if reuqest.user.is_authenticated %}
    <form action="{% url 'articles:comment_create' article.pk %}" method="POST">
      {% csrf_token %}
      {{ comment_form }}
      <input type="submit" value="댓글 작성">
    </form>
  {% else %}
    <a href="{% url 'accounts:login' %}">[댓글을 작성하려면 로그인하세요]</a>
  {% endif %}
	
{% endblock content %}
```

- 댓글 작성자 출력하기

```django
{# articles/detail.html #}
...
      <li>
        {{ comment.user}} - {{ comment.content }}
        <form action="{% url 'articles:comment_delete' article.pk comment.pk %}" method="POST">
          ...
```

- 자식이 작성한 댓글만 삭제 버튼을 볼 수 있도록 수정

```django
      <li>
        {{ request.user}} - {{ comment.content }}
        {% if user == comment.user %}
          <form action="{% url 'articles:comment_delete' article.pk comment.pk %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="삭제">
          </form>
        {% endif %}
```

```python
# articles/views.py

@require_POST
def comment_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)
```

