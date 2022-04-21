# M : N

[toc]

## Intro

- 모델링은 현실 세계를 최대한 유사하게 반영하기 위한 것



### 병원 진료 기록 시스템

1. 1:N의 한계

   - Doctor(1) : Patient(N)일 경우

     - 여러 의사에게 진료받은 기록을 환자 한 명에 저장할 수 없음 
       - 한 번에  두 의사에게 진료 x
       - 하나의 외래 키에 2개의 의사 데이터를 넣을 수 없음
     - 새로운 예약을 생성하는 것이 불가능
       - 새로운 객체를 만들어야 함

     ```python
     from django.db import models
     
     
     class Doctor(models.Model):
         name = models.TextField()
     
         def __str__(self):
             return f'{self.pk}번 의사 {self.name}'
     
     
     class Patient(models.Model):
         doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
         name = models.TextField()
     
         def __str__(self):
             return f'{self.pk}번 환자 {self.name}'
     
     
     # 코드 예시
     doctor1 = Doctor.objects.create(name='justin')
     doctor2 = Doctor.objects.create(name='eric')
     patient1 = Patient.objects.create(name='tony', doctor=doctor1)
     patient2 = Patient.objects.create(name='harry', doctor=doctor2)
     patient3 = Patient.objects.create(name='tony', doctor=doctor2)
     patient4 = Patient.objects.create(name='harry', doctor=doctor1, doctor2)
     ```

     

2. 중개 모델 (Associative Table)

   - Doctor(1) : Reservation(N) / Patient(1) : Reservation(N)일 경우

     ```python
     from django.db import models
     
     
     class Doctor(models.Model):
         name = models.TextField()
     
         def __str__(self):
             return f'{self.pk}번 의사 {self.name}'
     
     
     # 외래키 삭제
     class Patient(models.Model):
         name = models.TextField()
     
         def __str__(self):
             return f'{self.pk}번 환자 {self.name}'
     
     # 중개모델 작성
     class Reservation(models.Model):
         doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
         patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
     
         def __str__(self):
             return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
     
     
     # 코드 예시
     doctor1 = Doctor.objects.create(name='justin')
     patient1 = Patient.objects.create(name='tony')
     
     Reservation.objects.create(doctor=doctor1, patient=patient1)
     
     doctor1.reservation_set.all()
     patient1.reservation_set.all()
     
     patient2 = Patient.objects.create(name='harry')
     Reservation.objects.create(doctor=doctor1, patient=patient2)
     ```

     

3. ManyToManyField

   - 다대다 관계 설정 시 사용하는 모델 필드

   - 하나의 필수 위치인자(M:N 관계로 설정할 모델 클래스가 필요

   - ManyToManyField 작성

     - 중개 모델 삭제

     ```python
     # models.py
     
     from django.db import models
     
     
     class Doctor(models.Model):
         name = models.TextField()
     
         def __str__(self):
             return f'{self.pk}번 의사 {self.name}'
     
     
     class Patient(models.Model):
         # ManyToManyField 작성
         # 1:N과 구분하기 위해 복수형으로 인스턴스명 작성
         # related_name 써서 _set 대체할 용어 설정
         doctors = models.ManyToManyField(Doctor)
         name = models.TextField()
     
         def __str__(self):
             return f'{self.pk}번 환자 {self.name}'
         
     # 코드 예시
     doctor1 = Doctor.objects.create(name='justin')
     patient1 = Patient.objects.create(name='tony')
     patient2 = Patient.objects.create(name='harry')
     
     # create대신 add
     patient1.doctors.add(doctor1)
     patient1.doctors.all()
     doctor1.patient_set.all()
     
     # patient에 ManyToManyField있으므로 doctor는 patient에 역참조
     doctor1.patient_set.add(patient2)
     doctor1.patient_set.all()	# Out[10]: <QuerySet [<Patient: 1번 환자 tony>, <Patient: 2번 환자 harry>]>
     patient2.doctors.all()
     patient1.doctors.all()
     
     doctor1.patient_set.remove(patient1)
     doctor1.patient_set.all()
     patient1.doctors.all()	# Out[13]: <QuerySet []>
     
     patient2.doctors.remove(doctor1)
     patient2.doctors.all()
     doctor1.patient_set.all()
     ```

     - Doctor, Patient 테이블에 변화x
     - hospital_patient_doctor라는 중개 테이블이 자동 생성

4. related_name

   - target model(관계 필드를 가지지 않은 모델, Doctor)이 source model(관계 필드를 가진 모델, Patient)을 참조할 때(역참조) 사용할 manager의 이름을 설정

   - ForeignKey의 related_name과 동일

     ```python
     class Patient(models.Model):
         # ManyToManyField 작성
         doctors = models.ManyToManyField(Doctor, related_name='patients')
         name = models.TextField()
     ```



### 중개 모델(테이블) in Django

- django는 ManyToManyField를 통해 중개 테이블을 자동으로 생성
  - 외래키 2개로 만들어짐
  - 추가적인 컬럼 작성 불가
- 중개 테이블을 직접 작성하는 경우
  - 외래 키 2개 이외에 컬럼 필요한 경우



## ManyToManyField

- 다대다 (M:N, many-to-many)관계 설정 시 사용하는 모델 필드
- 모델 필드의 RelatedManager를 사용해 관련 개체를 추가, 제거 또는 만들 수 있음
  - add(), remove(), create(), clear(), ...



### Arguments

1. related_name
   - target model이 
2. through
   - 중개 테이블을 직접 작성하는 경우
   - 중개 테이블에 추가 데이터를 사용하는 다대다 관계와 연결하려는 경우(extra data with a many-to-many relationship)
3. symmetrical



### Related Manager

- 1:N 또는 M:N 관련 컨텍스트에서 사용되는 매니저
- 같은 이름의 메서드여도 각 관계에 따라 다르게 사용 및 독장
  - 1:N에서는 target 모델 인스턴스만 사용 가능
  - M:N 관계에서는 관련된 두 객체에서 모두 사용 가능
- 메서드 종류
  - add(), remove(), create(), clear(), set() 등



#### add()

- 지정된 객체를 관련 객체 집합에 추가

- 이미 존재하는 관계에 사용하면 관계가 복제되지 않음
- 모델 인스턴스, 필드 값(PK)를 인자로 허용



#### remove()

- 관련 객체 집합에서 지정된 모델 객체를 제거

- 내부적으로 QuerySet.delete()를 사용하여 관계가 삭제됨
- 모델 인스턴스, 필드 값(PK)를 인자로 허용



#### through 예시

- 어쩌고

  ```python
  class Patient(models.Model):
      doctors = models.ManyToManyField(Doctor, through='Reservation')
      name = models.TextField()
  
      def __str__(self):
          return f'{self.pk}번 환자 {self.name}'
  
  
  class Reservation(models.Model):
      doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
      patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
      symptom = models.TextField()
      reserved_at = models.DateTimeField(auto_now_add=True)
  
      def __str__(self):
          return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
  ```

  ```python
  doctor1 = Doctor.objects.create(name='justin')
  patient1 = Patient.objects.create(name='tony')
  patient2 = Patient.objects.create(name='harry')
  
  reservation1 = Reservation(doctor=doctor1, patient=patient1, symptom='headache')
  reservation1.save()
  doctor1.patient_set.all()
  patient1.doctors.all()
  
  patient2.doctors.add(doctor1, through_defaults={'symptom': 'flu'})
  doctor1.patient_set.all()
  patient2.doctors.all()
  ```

  - add() 사용 가능



#### 중개 테이블의 필드 생성 규칙

1. source model 및 target model 모델이 다른 경우
   - id
   - `<containing_model>_id` ex) patiend_id
   - `<other_model>_id`
2. ManyToManyField가 동일한 모델을 가리키는 경우
   - id
   - `from_<model>_id`
   - `to_<model>_id`



### 좋아요 기능 (Like)

```python
# articles/models.py

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # related_name이 없으면 이미 User:Article = 1:N으로 위에서 이미 썼으므로 오류 뜸
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

- 현재 User - Articles간 사용 가능한 DB API
  - article.user
    - 게시글을 작성한 유저
  - article.like_users
    - 게시글을 좋아요한 유저
  - user.article_set
    - 유저가 작성한 게시글(역참조)
  - user.like_articles
    - 유저가 좋아요한 게시글(역참조)



#### 좋아요 기능 구현

- urls.py

  ```python
      path('<int:article_pk>/likes', views.likes, name='likes'),
  
  ```

- views.py

  ```python
  @require_POST
  def likes(request, article_pk):
      # 로그인된 사용자만 좋아요 누를 수 있음
      if request.user.is_authenticated:
          article = get_object_or_404(Article, pk=article_pk)
          # 이 게시글에 좋아요를 누른 유저 목록에 현재 요청 유저가 있다면 -> 좋아요 취소
          # if request.user in article.like_users.all():
          # get 대신 filter쓰는 이유 -> filter는 없을 경우 빈 쿼리셋 반환하므로(get은 오류남)
          if article.like_users.filter(pk=request.user.pk).exists():
              article.like_users.remove(request.user)
          else:
              article.like_users.add(request.user)
          return redirect('articles:index')
      return redirect('accounts:login')
  ```

- QuerySet API - 'exists()'

  - QuerySet 에 결과가 포함되어 있으면 Ture를 반환, 그렇지 않으면 False를 반환
  - 특히 규모가 큰 쿼리셋의 컨텍스트에서 특정 개체의 존재 여부와 관련된 검색에 유용
    - in 연산자보다 유용함

- index.html

  ```django
    {% for article in articles %}
      <p>작성자: {{ article.user }}</p>
      <p>글 번호: {{ article.pk }}</p>  
      <p>글 제목: {{ article.title }}</p>
      <p>글 내용: {{ article.content }}</p>
      <div>
        <form action="{% url 'articles:likes' article.pk %}" method="POST">
          {% csrf_token %}
          {% if user in article.like_users.all  %}
            <input type="submit" value="Unlike">
          {% else %}
            <input type="submit" value="Like">
          {% endif %}
        </form>
      </div>
      <a href="{% url 'articles:detail' article.pk %}">DETAIL</a>
      <hr>
    {% endfor %}
  ```

- 이렇게 하면 작성시 Like_users 필드 뜸 -> forms.py 수정

  ```python
  class ArticleForm(forms.ModelForm):
  
      class Meta:
          model = Article
          exclude = ('user', 'like_users',)
  ```

  



### Profile Page

> 팔로우 기능이 있을 페이지

- urls.py

  ```python
  # accounts/urls.py
  
      path('<username>/', views.profile, name='profile'),
  ```

  ※ variable routing이 맨 위에 오면 str인 경우 계속 이쪽에만 걸리므로 순서 잘 정해줄 것

- views.py

  ```python
  # accounts/views.py
  from django.shortcuts import render, redirect, get_object_or_404
  from django.contrib.auth import get_user_model
  
  
  def profile(request, username):
      # username도 unique한 값이므로 pk대신 사용 가능
      person = get_object_or_404(get_user_model(), username=username)
      context = {
          'person': person,
      }
      return render(request, 'accounts/profile.html', context)
  ```

- profile.html

  ```django
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>{{ person.username }}님의 프로필</h1>
    <hr>
    {% comment %} 이 사람이 작성한 게시글 목록 {% endcomment %}
    <h2>{{ person.username }}이 작성한 게시글</h2>
    {% for article in person.article_set.all %}
      <p>{{ article.title }}</p>
    {% endfor %}
  
    {% comment %} 이 사람이 작성한 댓글 목록 {% endcomment %}
    <h2>{{ person.username }}이 작성한 댓글</h2>
    {% for comment in person.comment_set.all %}
      <p>{{ comment.content }}</p>
    {% endfor %}
    {% comment %} 이 사람이 좋아요 누른 게시글 목록 {% endcomment %}
    <h2>{{ person.username }}이 좋아요를 누른 게시글</h2>
    {% for article in person.like_articles.all %}
      <p>{{ article.title }}</p>
    {% endfor %}
  
  {% endblock content %}
  ```

  

### 팔로우 기능(Follow)

- ManyToManyField 작성 후 마이그레이션

  ```python
  # accounts/models.py
  
  class User(AbstractUser):
      followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
  ```

  - symmetrical
    - ManyToManyField가 동일한 모델(on self)을 가리키는 정의에서만 사용
    - symmetrical=True(기본값)일 경우 Django는 person_set 매니저를 추가하지 않음
      - 팔로우 하면 자동으로 맞팔되는 것

  - 중개 테이블
    - from_user_id
    - to_user_id

- urls.py

  ```python
      path('<int:user_pk>/follow/', views.follow, name='follow'),
  ```

- views.py

  ```python
  @require_POST
  def follow(request, user_pk):
      if request.user.is_authenticated:
          # you: 팔로우 대상 사람
          you = get_object_or_404(get_user_model(), pk=user_pk)
          me = request.user
          if me != you:
              if you.followers.filter(pk=me.pk).exists():
              # if me in  you.followers.all():
                  # 언팔로우
                  you.followers.remove(me)
              else:
                  # 팔로우
                  you.followers.add(me)
          return redirect('accounts:profile', you.username)
      return redirect('accounts:login')
  ```

- profile.html

  ```django
  {% block content %}
    <h1>{{ person.username }}님의 프로필</h1>
    
    <div>
      {% if user != person %}
        <form action="{% url 'accounts:follow' person.pk %}" method="POST">
          {% csrf_token %}
          {% if user in person.followers.all %}
          <input type="submit" value="Unfollow">
          {% else %}
          <input type="submit" value="Follow">
          {% endif %}
        </form>
      {% endif %}
    </div>
    <hr>
  ```

  - 반복적인 부분 with 태그로 정리

    ```django
    {% block content %}
      <h1>{{ person.username }}님의 프로필</h1>
    
      {% with  followers=person.followers.all followings=person.followings.all  %}
        <div>
          팔로워: {{ followers.all|length }}  팔로우: {{ followings.count }}
        </div>
        <div>
          {% if user != person %}
            <form action="{% url 'accounts:follow' person.pk %}" method="POST">
              {% csrf_token %}
              {% if user in followers %}
              <input type="submit" value="Unfollow">
              {% else %}
              <input type="submit" value="Follow">
              {% endif %}
            </form>
            {% endif %}
          </div>
        {% endwith %}
    ```



- 작성자의 프로필로 이동할 수 있도록 index.html 수정

  ```django
    {% for article in articles %}
      <p>작성자: <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a></p>
      <p>글 번호: {{ article.pk }}</p>  
      <p>글 제목: {{ article.title }}</p>
      <p>글 내용: {{ article.content }}</p>
  ...
  ```




### 검색 기능

- url

  ```python
  app_name = 'articles'
  urlpatterns = [
      ...
      path('search/', views.search, name='search'),
  ```

- views

  ```python
  def search(request):
      #1. 사용자가 입력한 검색어 받아와야 함
      keyword = request.GET.get('keyword')
      #2. 해당 검색어를 통해 DB에 일치하는 데이터가 있는지 확인하고 불러옴
      # 게시글의 제목 혹은 내용에 'keyword'가 있는지를 확인
      results = Article.objects.filter(
          Q(title__icontains=keyword) | Q(content__icontains=keyword)
      )
      context = {
          'results': results,
      }
      return render(request, 'articles/search_result.html', context)
  ```

- template

  ```django
  {# articles/index.html #}
  
    <form action="{% url 'articles:search' %}" method="GET">
      <label for="search">검색어: </label>
      <input type="text" name="keyword" id="search">
      <input type="submit" value="검색해주세요.">
    </form>
  ```

  