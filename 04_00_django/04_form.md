# Form / ModelForm

[toc]

## 복습

### Model

- 데이터베이스의 구조
- 데이터 베이스
  - 체계화된 데이터의 모임
- 쿼리
  - 데이터를 조회하기 위한 명령어
- 스키마
  - 데이터베이스에서 자료의 구조, 표현방법, 관계 등을 정의한 구조
- 테이블
  - 열 : 필드
  - 행 : 레코드



### ORM

- Object-Relational-Mapping
- 파이썬은 SQL을 호환x -> ORM을 통해 소통
- 요청 보내기
  - Queryset API
- 응답
  - Obejct, queryset
- 생산성을 위해 ORM 사용



### Migrations

- 장고가 model에 생긴 변화를 반영하는 방법
  - makemigrations
    - 모델에 변경사항이 생기면 반드시 새로운 마이그레이션(설계도) 만들어야함
  - migrate
    - 마이그레이션을 DB에 반영하기 위해 사용
    - 설계도를 실제 DB에 반영하는 과정
  - sqlmigrate
    - SQL문 확인
  - showmigrations
    - 마이그레이션 상태를 확인하기 위해 사용
- migration 3단계
  1. mdels.py
     1. model 변경사항 발생 시
  2. `$ python manage.py makemigrations`
  3. `$ python manage.py migrate`



### Database API

#### DB API

- DB를 조작하기 위한 도구
  - `Article.objects.all()` : Class Name / Manager / QuerySet API
- Manager
  - 장고 모델 클래스에 objects라는 Manager를 추가
- QuerySet
  - 데이터베이스로부터 전달받은 객체 목록
  - queryset 안의 객체는 0개, 1개 혹은 여러 개일 수 있음



### CRUD

#### Create

```sqlite
# 1.
article = Article()
article.title = 'first'
article.content = 'django!'
article.save()

# 2. 
article = Article(title='second', content='django!!')
article.save()

# 3. 사용자에게 '무언가 입력 받을 양식' 제공 => html => new
Article.objects.create(title='third', content='django!!!')
```

- save() method
  - 데이터 생성 시 save()를 호출하기 전에는 객체의 ID 값은 존재하지 않음
  - 사용자가 입력한 데이터 받아서 DB 저장 => create



#### Read

- `Article.objects.all()`
  - 전체 article 객체 조회

- all()
  - 현재 QuerySet 전체를 반환
- get()
  - QuerySet을 주지 않음
  - 주어진 매개변수와 일치하는 객체를 반환
  - 객체를 찾을 수 없다면 DoesNotExist
  - 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생
  - 고유성을 보장하는 조회에서 사용해야 함(ex. pk)
- filter()
  - QuerySet 반환
  - 검색이 안 되어도 오류나지 않고 빈 QuerySet을 줌



#### Update

```sqlite
article = Article.objects.get(pk=1)
article.title = 'byebye'
article.save()
```



#### Delete

```sqlite
article = Article.objects.get(pk=1)
article.delete()
# 삭제된 딕셔너리? 반환
```



- Field lookups
  - 조회 시 특정 검색 조건을 지정
  - __ : double underbar(dunder?)
  - ex)
    - Article.objects.filter(pk__gt=2)
    - Article.objects.filter(content__contains='ja')



- POST
  - get 할 때 조회 키는 어디서 왔나? -> input의 name



## Form Class

- 지금까지 form, input을 통해 사용자로부터 데이터 받음
- 데이터를 입력받으면 입력된 데이터의 유효성을 검증해야 함 & 필요시에 입력된 데이터를 검증 결과와 함께 다시 표시해야 함
  - 사용자가 입력한 데이터는 개발자가 요구한 형식이 아닐 수 있음을 항상 생각해야 함
- 유효성 검증
  - 사용자가 입력한 데이터를 검증
- Django Form : 과중한 작업과 반복 코드를 줄여줌



### Django's forms

- Form : Django의 유효성 검사 도구 중 하나
  - 외부의 악의적 공격 및 데이터 손상에 대한 중요한 방어 수단
- Form과 관련된 유효성 검사를 단순화
- 자동화 할 수 있는 기능 제공
- 직접 작성하는 코드보다 더 안전하고 빠르게 수행하는 코드를 작성할 수 있게 함
  1. 렌더링을 위한 데이터 준비 및 재구성
  2. 데이터에 대한 HTML forms 생성
  3. 클라이언트로부터 받은 데이터 수신 및 처리



### The Django 'Form Class'

- Form Class를 상속받아 사용
  - Form 내 field
  - field 배치
  - 디스플레이 widget
  - label
  - 초기값
  - 유효하지 않는 field에 관련된 에러 메세지




### Form 선언

```bash
$ python -m venv venv
# ctrl + shift + p -> interpreter -> venv 선택
$ pip list
$ pip install -r requirements.txt
```

```python
# articles/forms.py -> 직접 생성

from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()
```

- form 태그와 input 태그를 대체함
- Form 클래스 상속받음

```python
# articles/viesw.py
from .forms import ArticleForm

def new(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

```django
{# articles/new.html #}

  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ form }}
    {% comment %} <label for="title">Title: </label>
    <input type="text" id="title" name="title"><br>
    <label for="content">Content: </label>
    <textarea name="content" id="content" cols="30" rows="10"></textarea> {% endcomment %}
    <input type="submit">
  </form>
```

- input태그는 inline속성이라 title이랑content가 한 줄에 나타나게 됨



- Form rendering options
- label & input 쌍에 대한 3가지 출력 옵션
  1. as_p()
     - 각 필드가 p태그로 감싸짐
  2. as_ul()
     - 각 필드가 목록 항목(li 태그)으로 감싸져서 렌더링 됨
     - ul 태그는 직접 작성해야 함
  3. as_table()
     - 각 필드가 테이블(tr태그) 행으로 감싸짐
     - table 태그는 직접 작성해야 함

```django
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
```



#### Django의 HTML input 요소 표현 방법 2가지

1. Form fields
2. Widgets
   - 웹 페이지의 HTML input 요소 렌더링
   - GET/POST 딕셔너리에서 데이터 추출
   - widgets은 반드시 Form fields에 할당 됨
   - 단독적으로 사용x. 필드에 속해 있음 -> 필드에서 제공할 수 없는 것들을 위젯으로 추가적으로 작성

```python
# forms.py

from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
```



#### Widgets

- Django의 HTML input element 표현
- HTML 렌더링 처리

- 주의사항
  - Form Fields와 혼동되어서는 안됨
  - Form Fields는 input 유효성 검사를 처리
  - Widgets은 웹페이지에서 input element의 단순 raw한 렌더링 처리



#### Form field 및 widget 응용

```python
# forms.py

from django import forms

class ArticleForm(forms.Form):
    REGION_A = "sl"
    REGION_B = "dj"
    REGION_C = "gj"
    REGIONS_CHOICES = [
        (REGION_A, '서울'),		# 사용자한테는 두 번째 인자가 보여짐
        (REGION_B, '대전'),		# 첫 번째 인자는 value
        (REGION_C, '광주'),
    ]
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
    region = forms.ChoiceField(widget=forms.Select, choices=REGIONS_CHOICES)
```

- django coding style 참고



## ModelForm

- Form에서 Model 필드를 재정의하는 행위가 중복 될 수 있음
- Django는 Model을 통해 Form Class를 만들 수 있는 ModelForm이라는 Helper를 제공
- ModelForm이 쉽게 해주는 것
  1. 모델 필드 속성에 맞는 html element를 만들어줌
  2. 이를 통해 받은 데이터를 view함수에서 유효성 검사를 할 수 있도록 함



### ModelForm Class

- Model을 통해 Form Class를 만들 수 있는 Helper

```python
# forms.py

from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title',)		출력에서 title을 빼고 싶다면
```

- forms 라이브러리에서 파생된 ModelForm 클래스를 상속받음
- 정의한 클래스 안에 Meta 클래스를 선언
- 어떤 모델을 기반으로 Form을 작성할 것인지에 대한 정보를 Meta클래스에 지정
- modelform은 db에 저장되는 데이터일 때
- form은 db에 저장하지 않는 데이터일 때 ex) 로그인 정보
  - 모델에서 정보를 가져오지 않기 때문에 field 하나하나 지정해야 함



### Meta class

- Model의 정보를 작성하는 곳
- ModelForm을 사용할 경우 사용할 모델이 있어야 하는데 Meta Class가 이를 구성함

- Meta 데이터
  - 데이터에 대한 데이터
  - ex) 사진의 메타 데이터(촬영 시각, 조리개값 등)



- create view 수정

```python
# views.py

def create(request):
    form = ArticleForm(request.POST)
    # 유효성 검사
    if form.is_valid():
        article = form.save()			# save한 객체 반환하므로 article에 담아줌
        return redirect('articles:detail', article.pk)
    return redirect('articles:new')
```



- is_valid() method
  - 유효성 검사
  - 에러 메시지 넘겨줌

  
  
- The save() method

  - ModelForm의 save메서드
  - Form에 바인딩 된 데이터에서 데이터베이스 객체를 만들고 저장
  - ModelForm의 하위(sub)클래스는 기존 모델 인스턴스를 키워드 인자 instance로 받아들일 수 있음
    - 인스턴스 넘겨줌 : UPDATE
    - 인스턴스 x : CREATE

  - Form의 유효성이 확인되지 않는 경우 save()를 호출하면 form.errors를 확인하여 에러 확인 가능

  ```python
  form = ArticleForm(request.POST)
  new_article = form.save()
  article = Article.objects.get(pk=1)
  # 인스턴스 유무로 저장인지 수정인지 판단함(?)
  form = ArticleForm(request.POST, instance=article)
  form.save()
  ```

  

- create view 함수 구조 변경

  - new : GET
  - create : POST

  ```python
  def create(request):
      if request.method == 'POST':
          # create
          form = ArticleForm(request.POST)
          # 유효성 검사
          if form.is_valid():
              article = form.save()
              return redirect('articles:detail', article.pk)
          # print(form.errors)
      else:
          # new
          form = ArticleForm()
      # form.is_valid() 통과하지 않았을 때에도 return에서 context넘겨줘야 하므로 들여쓰기 할 것(에러메시지를 담은 상태로 넘어옴)
      context = {
          'form': form,
      }
      return render(request, 'articles/create.html', context)
  ```

  - create.html에서 action없으면 현재 url로 요청 보냄 but 명시적으로 적어두는 걸 권장
  - POST 먼저 본 이유
    - else는 POST가 아닌 모든 메서드일 때



- update view 함수 구조 변경

  ```python
  def update(request, pk):
      # update
      if request.method == 'POST':
          article = Article.objects.get(pk=pk)
          # instance를 넘기지 않으면 save()할 때 새로운 글로 판단함 -> instance에 과거 데이터를 넘겨야 함
          form = ArticleForm(request.POST, instance=article)
          # 유효성 검사
          if form.is_valid():
              article = form.save()
              return redirect('articles:detail', article.pk)
  
      # edit
      else:
          article = Article.objects.get(pk=pk)
          # 전에 작성한 내용 보여주기 위해 instanc=article 필요
          form = ArticleForm(instance=article)
      context = {
          'article': article,
          'form': form,
      }
      return render(request, 'articles/update.html', context)
  ```

  

- forms.py 파일 위치
  - models.py에 같이 적어도 상관은 없으나 app폴더/forms.py에 작성하는 것이 일반적인 구조



#### [참고] Form & ModelForm 비교

- Form
  - 어떤 Model에 저장해야 하는지 알 수 없으므로 유효성 검사 이후 cleaned_data 딕셔너리 생성
  - cleaned_data 딕셔너리에서 데이터를 가져온 후 .save() 호출해야 함
  - Model 에 연관되지 않은 데이터를 받을 때 사용
- ModelForm
  - Django가 해당 model에서 양식에 필요한 대부분의 정보를 이미 정의
  - 어떤 레코드를 만들어야 할 지 알고 있으므로 바로 .save() 호출 가능






### Widgets 활용하기

- Django의 HTML input element표현
- HTML 렌더링을 처리
- 2가지 작성 방식을 가짐
- 유효성 검사와 관련 x



- widgets으로 커스텀 하려면 ModelForm이어도 위에 다시 작성해야 함

  ```python
  # forms.py
  
  from django import forms
  from .models import Article
  
  class ArticleForm(forms.ModelForm):
      title = forms.CharField(
          widget=forms.TextInput(
              # input 태그에 속성값 넣을 수 있음
              attrs={
                  'class': 'my-title second-class',
                  'placeholder': 'Enter the title',
              }
          )
      )
      content = forms.CharField(
          widget=forms.Textarea(
              attrs={
                  'class': 'my-content',
              }
          )
          error_messages={
              'required': 'Please enter your content!!',
          }
      )
  
      class Meta:
          model = Article
          fields = '__all__'
          # exclude = ('title',)
  ```



## Rendering fields manually

### 수동으로 Form 작성하기

1. Rendering fields manually

   ```django
   {# create.html #}
   
     <hr>
     <h2>1. Rndering fields manully</h2>
     <form action="{% url 'articles:create' %}" method="POST">
       {% csrf_token %}
       <div>
         {{ form.title.errors }}
         {{ form.title.label_tag }}
         {{ form.title }}
       </div>
       <div>
         {{ form.content.errors }}
         {{ form.content.label_tag }}
         {{ form.content }}
       </div>
       <input type="submit">
     </form>
   ```



2. Looping over the form's fields

   ```django
     <hr>
     <h2>2. Looping over the form's fields</h2>
     <form action="{% url 'articles:create' %}" method="POST">
       {% csrf_token %}
       {% for field in form %}
         {{ field.errors }}
         {{ field.label_tag }}
         {{ field }}
       {% endfor %}
       <input type="submit">
     </form>
   ```

   

#### Bootstrap과 함께 사용하기

1. Boostrap class with widgets

   ```python
   # forms.py
   
   class ArticleForm(forms.ModelForm):
       title = forms.CharField(
           widget=forms.TextInput(
               # input 태그에 속성값 넣을 수 있음
               attrs={
                   'class': 'my-title form-control',
                   'placeholder': 'Enter the title',
               }
           )
       )
   ```

   ```django
   {# create.html #}
   
    <h2>2. Looping over the form's fields</h2>
     <form action="{% url 'articles:create' %}" method="POST">
       {% csrf_token %}
       {% for field in form %}
         {% if field.errors %}
           {% for error in field.errors %}
             <div class="alert alert-danger">{{ error }}</div>
           {% endfor %}
         {% endif %}
         {{ field.label_tag }}
         {{ field }}
       {% endfor %}
   ```

   

2. Django Boostrap 5 Library

   - django-bootstrap v5

     ```bash
     $ pip install django-bootstrap-v5
     $ pip freeze > requirements.txt
     ```

     ```python
     # settings.py
     
     INSTALLED_APPS = [
         ...
         'bootstrap5',
         ...
     ]
     ```

     ```django
     {# update.html #}
     
     {% extends 'base.html' %}
     {% load bootstrap5 %}
     
     {% block content %}
       <h1>UPDATE</h1>
       <hr>
       <form action="{% url 'articles:update' article.pk %}" method="POST">
         {% csrf_token %}
         {% bootstrap_form form %}
           ...
     ```

     