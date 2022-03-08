# Model

[toc]

## Model

- 단일한 데이터에 대한 정보를 가짐
  - 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함
- 저장된 데이터베이스의 구조(layout)
- 장고는 모델을 통해 데이터에 접속하고 관리



## Database

- 데이터베이스(DB)
  - 체계화된 데이터의 모임
- 쿼리(Query)
  - 데이터를 조회하기 위한 명령어
  - 조건에 맞는 데이터를 추출하거나 조작하는 명령어
  - 쿼리를 날린다 -> DB를 조작한다



- CRUD
  - Create
  - Read
  - Update
  - Delete



### Database의 기본 구조

- 스키마(Schema)
  - 데이터베이스에서 제약조건(자료의 구조, 표현방법, 관계 등)을 정의한 구조(structure)
- 테이블(Table)
  - 데이터 요소들의 집합
  - 열(column) : 필드(field) or 속성
  - 행(row) : 레코드(record) or 튜플. 데이터가 저장됨
- PK(기본키) : 모든 데이터베이스에서 반드시 존재
  - id
  - 각 행(레코드)의 고유값(식별 가능하도록)
  - 데이터베이스 관리 및 관계 설정시 주요하게 활용됨



∴ 데이터를 구조화하고 조작하기 위해



## ORM

### ORM

- Object-Relational-Mapping
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에(Django - SQL) 데이터를 변환하는 프로그래밍 기술
- OOP 프로그래밍에서 RDBMS을 연동할 때, 데이터베이스
- 파이썬의 코드를 해석해서 SQL로 DB에 넘겨줌(?)

- 장고 : 내장된 Django orm을 사용함



### ORM의 장점과 단점

- 장점
  - SQL을 잘 알지 못해도 DB 조작 가능
  - SQL의 절차적 접근이 아닌 객체 지향적 접근으로 인한 높은 생산성
- 단점
  - ORM만으로 완전한 서비스를 구현하기 어려운 경우 있음
- 현대 웹 프레임워크의 요점 = 웹 개발 속도를 높이는 것(생산성)

∴ DB를 객체로 조작하기 위해 ORM을 사용



### models.py

- CharField

- TextField(**options)
  - 글자의 수가 많을 때 사용



## Migrations

### Migrations

- Django가 model에 생긴 변화를 반영하는 방법
- Migration 실행 및 DB 스키마를 다루기 위한 몇가지 명령어
  - makemigrations ★
  - migrate ★
  - sqlmigrate
  - showmigrations



### Migrations commands

- makemigrations
  - model을 변경한 것에 기반한 새로운 마이그레이션(설계도)을 만들 때 사용

- migrate
  - 마이그레이션을 DB에 반영하기 위해 사용
  - 설계도를 실제 DB에 반영하는 과정
  - 모델에서의 변경 사항들과 DB의 스키마가 동기화를 이룸
- sqlmigrate
  - 마이그레이션에 대한 SQL 구문을 보기 위해 사용
- showmigrations
  - 마이그레이션 상태 정보를 확인하기 위해 사용
  - `[X]` : 데이터베이스에 반영되어있다는 의미



### DateField's options

- auto_now_add
  - 최초 생성 일자
- auto_now



### 반드시

1. models.py
2. python manage.py makemigrations
3. python manage.py migrate



## Database API

### DB API

- DB를 조작하기 위한 도구
- Django가 기본적으로 ORM을 제공함에 따른 것으로 DB를 편하게 조작할 수 있도록 도움
- Model을 만들면 Django는 객체들을 만들고 읽고 수정하고 지울 수 있는 database-abstract API를 자동으로 만듦
- database-abstract API 혹은 database-access API라고도 함



### DB API 구문 - Making Queries

`ClassName.Manager.QuerySetAPI`

ex) `Article.objects.all()`



### DB API

- manager
  - Django모델에 데이터베이스 query 작업이 제공되는 인터페이스
  - 기본적으로 모든 Django 모델 클래스에 objects라는 Manager를 추가
- QuerySet
  - 유사리스트 : 인덱스접근, 정렬 가능
  - 데이터베이스로부터 전달받은 객체 목록
  - queryset 안의 객체는 0개, 1개 혹은 여러 개일 수 있음
  - 데이터베이스로부터 조회, 필터, 정렬 등을 수행할 수 있음



### Django shell

- 일반 Python shell을 통해서는 장고 프로젝트 환경에 접근할 수 없음



## CRUD

### Read

- all()
- get()
- filter()

### Create

1. 인스턴스 만들고 변수에 값들 넣기
2. 클래스에 변수 넣어서 만들기
3. 클래스에 바로 값 넣어서 만들기 -> save 없어도 바로 저장



### Update



### Delete

- delete()



### str method

표준 파이썬 클래스의 메소드인 str()



## Admin Site

### Automatic admin interface

- 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지
- Model class를 admin.py에 등록하고 관리
- django.contrib.auth 모듈에서 제공됨



## CRUD with views

