[TOC]

# SQL with django ORM

## 기본 준비 사항

* django app

  * 가상환경 세팅

  * 패키지 설치

    ```bash
    $ pip install ipython
    $ pip install django-extensions
    ```
  
  * migrate
  
    ```bash
    $ python manage.py migrate
    ```
  
* 제공 받은 `users.csv` 파일은 db.sqlite3와 같은 곳에 위치하도록 이동

* `db.sqlite3` 활용

  * `sqlite3`  실행

    ```bash
    $ sqlite3 db.sqlite3
    ```

  * 테이블 확인

    ```sqlite
    sqlite > .tables
    auth_group                  django_admin_log
    auth_group_permissions      django_content_type
    auth_permission             django_migrations
    auth_user                   django_session
    auth_user_groups            auth_user_user_permissions  
    users_user
    ```
    
  * csv 파일 data 로드 및 확인

    ```sqlite
    sqlite > .mode csv
    sqlite > .import users.csv users_user
    
    sqlite > SELECT COUNT(*) FROM users_user;
    100
    ```

- shell_plus 활용

  - shell_plus 실행

    ```bash
    $ python manage.py shell_plus
    ```

    

---



## 문제

> ORM은 django extensions의 shell_plus에서,
>
> SQL은 수업에서 진행한 [SQLite 확장프로그램](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite) 사용 방식으로 진행

### 1. 기본 CRUD 로직

1. 모든 user 레코드 조회

   ```python
   # orm
   
   In [1]: User.objects.all()
   Out[1]: <QuerySet [<User: 정호>, <User:  
   경희>, <User: 정자>, <User: 미경>, <User: 영환>, <User: 서준>, <User: 주원>, <User: 예진>, <User: 서현>, <User: 서윤>, <User: 서영>, <User: 미정>, <User: 하은>, <User: 영일>, <User: 지원>, <User: 옥자>, <User: 병철>, <User: 광수>, <User: 성민>, <User: 정수>, '...(remaining elements truncated)...']>
   ```

      ```sql
   -- sql
   
   sqlite> SELECT * FROM users_user;
      ```

2. user 레코드 생성

   ```python
   # orm
   
   In [3]: User.objects.create(first_name=' 
      ...: 길동',
      ...: last_name='홍',
      ...: age=100,
      ...: country='서울',
      ...: phone='010-1234-1234',
      ...: balance=10000000,)
   Out[3]: <User: 길동>
           
   # 생성 확인
   In [5]: User.objects.all()[100]
   Out[5]: <User: 길동>
   
   In [6]: User.objects.get(pk=101)
   Out[6]: <User: 길동>
   
   In [7]: User.objects.last()
   Out[7]: <User: 길동>
   ```

   ```sql
   -- sql
   
   sqlite> INSERT INTO users_user VALUES (102, '길동', '홍', 200, '제주도', '010-1234-5678', 2000); 
   ```

   * 하나의 레코드를 빼고 작성 후 `NOT NULL` constraint 오류를 orm과 sql에서 모두 확인 해보세요.

3. 해당 user 레코드 조회

   - `102` 번 id의 전체 레코드 조회

   ```python
   # orm
   
   In [5]: User.objects.get(pk=102)
   ```

   ```sql
   -- sql
   
   sqlite> SELECT * FROM users_user WHERE id=102;
   ```

4. 해당 user 레코드 수정

   - ORM: `102` 번 글의 `last_name` 을 '김' 으로 수정
   - SQL: `102` 번 글의 `first_name` 을 '철수' 로 수정

   ```python
   # orm
   
   In [6]: user = User.objects.get(pk=102)       
   
   In [7]: user.last_name='김'
   ```

      ```sql
   -- sql
   
   sqlite> UPDATE users_user
      ...> SET first_name='철수'
      ...> WHERE id=101;
      ```

5. 해당 user 레코드 삭제

   - ORM: `102` 번 글 삭제
   - `SQL`:  `101` 번 글 삭제 

   ```python
   # orm
   
   In [13]: User.objects.get(pk=102).delete()    
   Out[13]: (1, {'users.User': 1})
   ```
   
   ```sql
   -- sql
   
   sqlite> DELETE FROM users_user WHERE id=101;
   ```



---



### 2. 조건에 따른 쿼리문

1. 전체 인원 수 

   - `User` 의 전체 인원수

   ```python
   # orm
   
   In [9]: len(User.objects.all())
   Out[9]: 102
   
   In [10]: User.objects.count()
   Out[10]: 102
   ```

   ```sql
   -- sql
   
   sqlite> SELECT COUNT(*) FROM users_user;
   102
   ```

2. 나이가 30인 사람의 이름

   - `ORM` : `.values` 활용
     - 예시: `User.objects.filter(조건).values(컬럼이름)`

   ```python
   # orm
   
   In [5]: User.objects.filter(age=30)      
   Out[5]: <QuerySet [<User: User object (5)>, <User: User object (57)>, <User: User 
   object (60)>]>
   
   In [6]: User.objects.filter(age=30).valu 
      ...: es()
   Out[6]: <QuerySet [{'id': 5, 'first_name': '영환', 'last_name': '차', 'age': 30, 'country': '충청북도', 'phone': '011-2921-4284', 'balance': 220}, {'id': 57, 'first_name': '보람', 'last_name': '안', 'age': 30, 'country': '제주특별자치도', 'phone': '010-6132-4229', 'balance': 68000}, {'id': 60, 'first_name': '은영', 'last_name': '김', 'age': 30, 'country': '경상북도', 'phone': '02-5110-2334', 'balance': 350}]>
   
   In [7]: User.objects.filter(age=30).valu 
      ...: es('first_name')
   Out[7]: <QuerySet [{'first_name': '영환'}, {'first_name': '보람'}, {'first_name': 
   '은영'}]>
   
   In [8]: User.objects.filter(age=30).valu 
      ...: es('first_name', 'balance')      
   Out[8]: <QuerySet [{'first_name': '영환', 'balance': 220}, {'first_name': '보람', 
   'balance': 68000}, {'first_name': '은영', 'balance': 350}]>
   ```

      ```sql
   -- sql
   
   qlite> SELECT first_name FROM users_user WHERE age=30;
      ```

3. 나이가 30살 이상인 사람의 인원 수

   -  ORM: `__gte` , `__lte` , `__gt`, `__lt` -> 대소관계 활용

   ```python
   # orm
   
   In [10]: User.objects.filter(age__gte=30)
   ```

      ```sql
   -- sql
   
   sqlite> SELECT first_name FROM users_user WHERE age>=30;
      ```

4. 나이가 20살 이하인 사람의 인원 수 

   ```python
   # orm
   
   In [18]: User.objects.filter(age__lte=20).cou 
       ...: nt()
   ```

   ```sql
   -- sql
   
   sqlite> SELECT COUNT(*) FROM users_user WHERE 
   age <= 20;
   ```

5. 나이가 30이면서 성이 김씨인 사람의 인원 수

   ```python
   # orm
   
   In [19]: User.objects.filter(last_name='김',  
       ...: age=30).count()
   ```

      ```sql
   -- sql
   
   sqlite> SELECT COUNT(*) FROM users_user WHERE 
   age=30 AND last_name='김';
      ```

6. 나이가 30이거나 성이 김씨인 사람?

   ```python
   # orm
   
   In [20]: User.objects.filter(Q(age=30) | Q(la 
       ...: st_name='김')).count()
   ```

   ```sql
   -- sql
   
   sqlite> SELECT COUNT(*) FROM users_user WHERE 
   age=30 OR last_name='김';
   ```

7. 지역번호가 02인 사람의 인원 수

   - `ORM`: `__startswith` 

   ```python
   # orm
   
   In [21]: User.objects.filter(phone__startswit 
       ...: h='02-').count()
   ```

      ```sql
   -- sql
   
   sqlite> SELECT COUNT(*) FROM users_user WHERE 
   phone LIKE '02-%';
      ```

8. 거주 지역이 강원도이면서 성이 황씨인 사람의 이름

   ```python
   # orm
   
   In [24]: User.objects.get(country='강원도', l 
       ...: ast_name='황').first_name
   ```
   
      ```sql
   -- sql
   
   sqlite> SELECT first_name FROM users_user WHERE country='강원도' AND last_name='황'; 
      ```



---



### 3. 정렬 및 LIMIT, OFFSET

1. 나이가 많은 사람순으로 10명

   ```python
   # orm
   
   In [26]: User.objects.order_by('-age')[:10].v 
       ...: alues('first_name')
   ```

      ```sql
   -- sql
   
   SELECT first_name FROM users_user ORD  E
   R BY age DESC LIMIT 10;
      ```

2. 잔액이 적은 사람순으로 10명

   ```python
   # orm
   
   In [27]: User.objects.order_by('balance')[:10 
       ...: ].values('first_name')
   ```

      ```sql
   -- sql
   
   sqlite> SELECT first_name FROM users_user ORD  E
   R BY balance LIMIT 10;
      ```

3. 잔고는 오름차순, 나이는 내림차순으로 10명?

      ```python
   # orm
   
   In [29]: User.objects.order_by('balance', '-a 
       ...: ge')[:10].values()
   ```
   
   ```sql
   -- sql
   
   sqlite> SELECT * FROM users_user ORDER BY balance, age DESC LIMIT 10;
   ```
   
4. 성, 이름 내림차순 순으로 5번째 있는 사람

   ```python
   # orm
   
   In [33]: User.objects.order_by('-last_name',  
       ...: '-first_name')[4]
   ```
   
      ```sql
   -- sql
   
   sqlite> SELECT * FROM users_user ORDER BY last_name DESC , first_name DESC LIMIT 4, 1; 
   
   sqlite> SELECT * FROM users_user ORDER BY last_name DESC , first_name DESC LIMIT 1 OFFSET  ;
      ```



---



### 4. 표현식

#### 4.1 Aggregate

> - https://docs.djangoproject.com/en/3.2/topics/db/aggregation/#aggregation
>- '종합', '집합', '합계' 등의 사전적 의미
> - 특정 필드 전체의 합, 평균 등을 계산할 때 사용
>- `Django_aggregation.md` 문서 참고

1. 전체 평균 나이

   ```python
   # orm
   
   In [35]: User.objects.aggregate(Avg('age'))
   ```

      ```sql
   -- sql
   
   sqlite> SELECT AVG(age) FROM users_user;  
      ```

2. 김씨의 평균 나이

   ```python
   # orm
   
   In [42]: User.objects.filter(last_name='김'). 
       ...: aggregate(Avg('age'))
   ```

      ```sql
   -- sql
   
   sqlite> SELECT AVG(age) FROM users_user WHERE 
   last_name='김';
      ```

3. 강원도에 사는 사람의 평균 계좌 잔고

   ```python
   # orm
   
   In [43]: User.objects.filter(country='강원도' 
       ...: ).aggregate(Avg('balance'))
   ```

   ```sql
   -- sql
   
   sqlite> SELECT AVG(balance) FROM users_user WH
   ERE country='강원도';
   ```

4. 계좌 잔액 중 가장 높은 값

   ```python
   # orm
   
   In [46]: User.objects.order_by('-balance')[0] 
       ...: .balance
           
   In [47]: User.objects.aggregate(Max('balance' 
       ...: ))
   ```

      ```sql
   -- sql
   
   sqlite> SELECT balance FROM users_user ORDER BY balance DESC LIMIT 1;
   
   sqlite> SELECT MAX(balance) FROM users_user ;
      ```

5. 계좌 잔액 총액

   ```python
   # orm
   
   In [48]: User.objects.aggregate(Sum('balance' 
       ...: ))
   ```
   
      ```sql
   -- sql
   
   sqlite> SELECT SUM(balance) FROM users_user ;
      ```



#### 4.2 Annotate

1. 지역별 인원 수

   ```PYTHON
   # orm
   
   In [49]: User.objects.values('country').annot 
       ...: ate(Count('country'))
   ```
   
   ```SQL
   -- sql
   
   sqlite> SELECT country, COUNT(*) FROM users_user GROUP BY country;
   ```
   
   