# DB: SQL & ORM 개념

[toc]

## Database

- 체계화된 데이터의 모임

- 몇 개의 자료파일을 조직적으로 통합
- 자료 항목의 중복을 없애고 자료를 구조화하여 기억시켜놓은 자료의 집합체



### 데이터베이스로 얻는 장점들

- 데이터 중복 최소화
- 데이터 무결성
- 일관성
- 독립성
- 표준화
- 보안 유지



### RDB

> 관계형 데이터베이스

- Relational Database

- 키와 값을의 관계를 표로 정리한 데이터베이스
- ex) 엑셀



#### 용어 정리

- 스키마(schema) : 데이터베이스의 자료의 구조, 표현방법, 관계 등 전반적인 명세를 기술한 것
- 테이블
  - 열(컬럼/필드)
    - 고유한 데이터 형식이 지정됨
  - 행(레코드/값)
    - 실제 데이터가 저장되는 형태
  - 기본키(Primary Key) : 각 행(레코드)의 고유값
    - 반드시 설정해야 함.
    - 데이터베이스 관리 및 관계 설정 시 주요하게 활용됨



### RDBMS

> 관계형 데이터베이스 관리 시스템

- Relational Database Management System
- 관계형 모델을 기반으로 하는 데이터베이스 관리시스템을 의미
  - SQLite : 장고에 내장되어있음
  - PostgreSQL : 장고 개발자들이 많이 씀



#### SQLite

- 서버 형태 x 파일 형식 o
- 응용 프로그램에 넣어서 사용하는 비교적 가벼운 데이터베이스
- 안드로이드 운영체제에 기본적으로 탑재된 데이터베이스
- 로컬에서 간단한 DB 구성을 할 수 있음
- 오픈소스 프로젝트



#### SQlite Data Type

- Null
  - 파이썬에서 None과 비슷
- INTEGER
- REAL
  - 부동 소수점 값
- TEXT
- BLOB
  - 타입 없이 그대로 저장



#### SQlite Type Affinity

> 타입 선호도

일반적으로 동적 데이터 타입보단 정적 데이터 타입 선호

- 특정 컬럼에 저장하도록 권장하는 데이터 타입
  1. INTEGER
  2. TEXT
  3. BLOB
  4. REAL
  5. NUMERIC



#### SQLite 설치하기



## SQL(Structured Query Language)

- 관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계된 특수 목적의 프로그래밍 언어
- 데이터베이스 스키마 생성 및 수정
- 자료의 검색 및 관리
- 데이터베이스 객체 접근 조정 관리



### SQL 분류 ★

| 분류                   | 개념                                                         | 예시                                        |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------- |
| DDL - 데이터 정의 언어 | 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어 | CREATE<br />DROP<br />ALTER                 |
| DML - 데이터 조작 언어 | 데이터를 저장, 조회, 수정, 삭제 등을 하기 위한 명령어        | INSERT<br />SELECT<br />UPDATE<br />DELETE  |
| DCL - 데이터 제어 언어 | 데이터베이스 사용자의 권한 제어를 위해 사용하는 명령어       | GRANT<br />REVOKE<br />COMMIT<br />ROLLBACK |



#### SQL Keywords - Data Manipulation Language(DML)

- INSERT
- SELECT
- UPDATE
- DELETE



#### 테이블 생성 및 삭제

```bash
$ sqlite3 tutorial.sqlite3
...
sqlite> .database	# '.'은 sqlite프로그램의 기능을 실행하는 것(sql문은 아님)
sqlite> .mode csv
sqlite> .import hellodb.csv example
sqlite> .tables
example
sqlite> SELECT * FROM example;	# ';'까지를 명령어로 간주함
1,"길동","홍",600,"충청도",010-0000-0000
sqlite> .headers on
sqlite> SELECT * FROM example;
id,first_name,last_name,age,country,phone
1,"길동","홍",600,"충청도",010-0000-0000
sqlite> .mode column
sqlite> SELECT * FROM example;
id  first_name  last_name  age  country  phone
--  ----------  ---------  ---  -------  -------------
1   길동          홍          600  충청도      010-0000-0000
```



#### SELECT 확인하기

```bash
sqlite> SELECT * FROM example;	# ';'까지를 명령어로 간주함
```



#### sqlite 확장프로그램 사용하기

New Query 클릭 -> 파일 생성

```sql
-- SQLite(SQL에서 주석 : --)
SELECT * FROM example;
```

코드에서 오른쪽클릭 -> run selected query



#### 테이블 생성 및 삭제 statement

- creage table

  ```sql
  CREATE TABLE classmates (
    id INTERGER PRIMARY KEY,
    name TEXT
  );
  ```

  드래그 -> run selected query



#### DROP

```sql
DROP TABLE classmates;
```



#### CREATE

- INSERT

  - 'insert a single row into a table'

  - 테이블에 단일 행 삽입

    ```sql
    INSERT INTO 테이블이름 (컬럼1, 컬럼2, ...) VALUES (값1, 값2, ...);
    ```

    ```sql
    -- SQLite
    INSERT INTO classmates (name, age) VALUES ('홍길동', 22);
    -- 모든 열에 데이터가 있는 경우 colum을 명시하지 않아도 됨
    INSERT INTO classmates VALUES ('홍길동', 30, '서울');
    ```



- sqlite는 따로 PRIMARY KEY 속성의 컬럼을 작성하지 않으면 값이 자동으로 증가하는 PK옵션을 가진 rowid컬럼을 정의

- 기본적으로 id 존재하지만 출력에서 보여주지 않았을 뿐

  -  보여지게 하려면

    ```sql
    SELECT rowid, * FROM classmates;
    ```

- Null

  - 꼭 필요한 정보라면 not Null 필요

  - 스키마 지정할 때 NOT NULL 설정

    ```sql
    CREATE TABLE classmates (
      -- PRIMARY KEY 속성값은 INT로 하면 안됨 -> 반드시 INTEGER로 할 것
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
      age INT NOT NULL,
      address TEXT NOT NULL
    );
    
    -- 이렇게 실행하면 에러남 why? id값 직접 작성해서
    INSERT INTO classmates VALUES ('홍길동', 30, '서울');
    -- 해결방법1 : id를 포함한 모든 value를 작성
    INSERT INTO classmates VALUES (1, '홍길동', 30, '서울');
    -- 해결방법2 : 각 value에 맞는 column들을 명시적으로 작성
    INSERT INTO classmates (name, age, address) VALUES ('홍길동', 30, '서울');
    -- rowid사용하는게 편함
    ```

- insert 여러 값 한번에 넣어보기

  ```sql
  INSERT INTO classmates VALUES 
    ('홍길동', 31, '서울'), 
    ('김철수', 30, '대전'), 
    ('이싸피', 26, '광주'), 
    ('박삼성', 25, '구미'), 
    ('최전자', 29, '부산');
  ```



#### READ

> 데이터베이스에서 가장 중요

- SELECT statement
  - 'query data from a table'
  - 테이블에서 데이터를 조회
  - SELECT문은 SQLite에서 가장 복잡한 문이며 다양한 절(clause)와 함께 사용
    - ORDER BY, DISTINCT, WHERE, LIMIT, GROUP BY, ...



#### SELECT와 함께 사용하는 clause

- LIMIT

  - constrain the number of rows returned by a query
  - 쿼리에서 반환되는 행 수를 제한
  - 특정 행부터 시작해서 조회하기 위해 OFFSET 키워드와 함께 사용하기도 함

- WHERE

  - specify the search condition for rows returned by the query
  - 쿼리에서 반환된 행에 대한 특정 검색 조건을 지정
  - if문과 유사

- SELECT DISTINCT

  - remove duplicate rows in the result set
  - 조회 결과에서 중복 행을 제거
  - DISTINCT 절은 SELECT 키워드 바로 뒤에 작성해야 함

  ```sql
  -- id, name만 조회
  SELECT rowid, name FROM classmates;
  -- id, name 컬럼 값 하나만 조회
  SELECT rowid, name FROM classmates LIMIT 1;
  -- id, name 컬럼 값을 세 번째에 있는 하나만 조회
  -- 0부터 시작하니까 세 번째 OFFSET 2로 해야함
  SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
  -- 특정 데이터(조건) 조회하기
  SELECT rowid, name FROM classmates WHERE address = '서울';
  -- 특정 컬럼을 기준으로 중복없이 가져오기
  SELECT DISTINCT age FROM classmates;
  ```

  

#### [참고] OFFSET

- 동일 오브젝트 안에서 오브젝트 처음부터 주어진 요소나 지점까지의 변위차(위치 변화량)을 나타내는 정수형
- 예시
  1. 문자열 'abcedf'에서 문자 'c'는 시작점 'a'에서 2의 OFFSET을 지님
  2. SELECT * FROM MY_TABLE LIMIT 10 OFFSET 5
     - 6번째 행부터 10개 행을 조회(6번째 행부터 10개를 출력)
     - 0부터 시작함



#### DELETE

- 조건을 통해 특정 레코드 삭제

  ```sql
  DELETE FROM classmates WHERE rowid=5;
  INSERT INTO classmates VALUES ('최전자', 28, '광주');
  SELECT rowid, * FROM classmates;
  -- 지워진 id 5를 재사용함
  ```

  - SQLite는 기본적으로 id 재사용

- AUTOINCREMENT

  - Column attribute

  - SQLite가 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지

    ```sql
    CREAT TABLE 테이블이름 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ...
    );
    ```

    - django에서는 기본 값으로 사용되는 설정



#### UPDATE

- update data of existing rows in the table

- 기존 행의 데이터를 수정

- SET clause에서 테이블의 각 열에 대해 새로운 값을 설정

  ```sql
  UPDATE 테이블이름 SET 컬럼1=값1, 컬럼2, 값2, ... WHERE 조건;
  UPDATE classmates SET name='홍길동', address='제주도' WHERE rowid=5;
  -- UPDATE SET WHERE마다 Enter쳐도 됨
  ```



#### CRUD 정리

> Table 생성 및 삭제 제외

|      | 구문   | 예시                                   |
| ---- | ------ | -------------------------------------- |
| C    | INSERT | INSERT INTO 테이블이름 ... VALUES ...; |
| R    | SELECT | SELECT * FROM 테이블이름 WHERE 조건;   |
| U    | UPDATE | UPDATE 테이블이름 SET ... WHERE 조건;  |
| D    | DELETE | DELETE FROM 테이블이름 WHERE 조거니    |

- 테이블 생성 : CREATE
- 테이블 삭제 : DROP



#### WHERE

```sql
CREATE TABLE users (
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INTEGER NOT NULL,
country TEXT NOT NULL,
phone TEXT NOT NULL,
balance INTEGER NOT NULL
);
```

```bash
$ sqlite3 tutorial.sqlite3
SQLite version 3.38.1 2022-03-12 13:37:29
Enter ".help" for usage hints.
sqlite> .tables
classmates  example     examples
sqlite> .mode csv
sqlite> .import users.csv users
sqlite> .tables
classmates  example     examples    users
sqlite>
```

```sql
-- 30세 이상만 조회
SELECT * FROM users WHERE age >= 30;

-- 이름만 조회
SELECT first_name FROM users WHERE age >= 30;

-- 30세 이상이고 성이 '김'인 사람의 나이와 성만 조회
SELECT age, first_name FROM users WHERE age >= 30 AND last_name='김';
```



### SQLite Aggregate Functions

- 집계 함수
- 값 집합에 대한 계산을 수행하고 단일 값을 반환
  - 여러 행으로부터 **하나의 결과값**을 반환하는 함수
- SELECT 구문에서만 사용됨

- ex.

  - COUNT(*) : 테이블 전체 행 수를 구함
  - AVG(age) : age 컬럼 전체 평균 값을 구함
  - MAX
  - MIN
  - SUM

- 구조

  ```sql
  SELECT COUNT (컬럼) FROM 테이블이름;
  ```

  ```sql
  -- 컬럼 수 구함
  SELECT COUNT(*) FROM users;
  
  -- 30세 이상인 사람들의 나이 평균 구함
  SELECT AVG(age) FROM users WHERE age >= 30;
  
  -- 계좌 잔액이 가장 높은 사람과 그 액수를 조회
  SELECT first_name, MAX(balance) FROM users;
  
  -- 나이가 30세 이상인 사람의 계좌 평균 잔액을 조회
  SELECT AVG(balance) FROM users WHERE age >= 30;
  ```

  

#### LIKE

- query data based on pattern matching
- 패턴 일치를 기반으로 데이터를 조회하는 방법
- SQLite는 패턴 구성을 위한 2개의 wildcards를 제공
  - %
    - 0개 이상의 문자



##### [참고] wildcard character

- 파일을 지정할 때, 구체적인 이름 대신에 여러 파일을 동시에 지정할 목적으로 사용하는 특수 기호
  - `*`, `?` 등
- 주로 특정한 패턴이 있는 문자열 혹은 파일을 찾거나, 긴 이름을 생략할 때 쓰임
- 유사하지만 동일한 데이터가 아닌 여러 항목을 찾기에 매우 편리한 문자



- `%` : 이 자리에 문자열이 있을 수도, 없을 수도 있다

- `-` : 반드시 이 자리에 한 개의 문자가 존재해야 한다 

- wildcards 사용 예시

  ```sql
  SELECT * FROM 테이블 WHERE 컬럼 LIKE '와일드카드패턴';
  ```

  | 와일드카드패턴   | 의미                                          |
  | ---------------- | --------------------------------------------- |
  | 2%               | 2로 시작하는 값                               |
  | %2               | 2로 끝나는 값                                 |
  | %2%              | 2가 들어가는 값                               |
  | _2%              | 아무 값이 하나 있고 두 번째가 2로 시작하는 값 |
  | `1___`           | 1로 시작하고 총 4자리인 값                    |
  | `2_%_%` / `2__%` | 2로 시작하고 적어도 3자리인 값                |

  ```sql
  -- 나이가 20대인 사람 조회
  SELECT * FROM users WHERE age LIKE '2_';
  
  -- 지역번호가 02인 사람만 조회
  SELECT * FROM users WHERE phone LIKE '02-%';
  
  -- 이름이 '준'으로 끝나는 사람만 조회
  SELECT * FROM users WHERE first_name LIKE '%준';
  
  -- 전화번호의 중간 번호가 5114인 사람만 조회
  SELECT * FROM users WHERE phone LIKE '%-5114-%';
  ```



#### ORDER BY

- sort a result set of a query

- 조회 결과 집합을 정렬

- SELECT 문에 추가하여 사용

- 정렬 순서를 위한 2개의 keyword 제공

  - ASC - 오름차순(default)
  - DESC - 내림차순

  ```sql
  SELECT * FROM 테이블 ORDER BY 컬럼 ASC;
  -- ASC는 생략 가능
  SELECT * FROM 테이블 ORDER BY 컬럼1, 컬럼2 DESC;
  ```

  ```sql
  -- 나이 순으로 오름차순 정렬하여 상위 10개만 조회
  SELECT * FROM users ORDER BY age  ASC LIMIT 10;
  
  -- 나이 순, 성 순으로 오름차순 정렬하여 상위 10개만 조회
  -- 나이로 먼저 정렬하고 같은 나이 그룹끼리 성 순으로 정렬
  SELECT * FROM users ORDER BY age, last_name LIMIT 10;
  
  -- 계좌 잔액 순으로 내림차순 정렬하여 해당 유저의 성과 이름을 10개만 조회
  SELECT first_name, last_name FROM users ORDER BY balance DESC LIMIT 10;
  ```

  

#### GROUP BY

- make a set of summary rows from a set of rows

- 행 집합에서 요약 행 집합을 만듦

- SELECT문의 optional절

- 선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만듦

- 문장에 WHERE 절이 포함된 경우 반드시 WHERE절 뒤에 작성해야 함

  ```sql
  SELECT 컬럼1, aggregate_function(컬럼2) FROM 테이블 GROUP BY 컬럼1, 컬럼2;
  ```

  ```sql
  -- 각 성씨가 몇 명씩 있는지 조회
  SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
  
  -- 각 성씨가 몇 명씩 있는지 조회 & column명 바꾸기
  SELECT last_name, COUNT(*) AS name_count FROM users GROUP BY last_name;
  ```

  

#### ALTER TABLE

- 3가지 기능

  1. table 이름 변경

  2. 테이블에 새로운 column 추가

  3. [참고] column 이름 수정(new in sqlite 3.25.0)

     ```sql
     ALTER TABLE table_name
     RENAME COLUMN current_name TO new_name;
     ```

  4. [참고] drop column(new in sqlite 3.35)

  ```sql
  CREATE TABLE articles (
  title TEXT NOT NULL,
  content TEXT NOT NULL
  );
  
  INSERT INTO articles VALUES ('1번 제목', '1번 내용');
  
  -- 테이블 이름 변경
  ALTER TABLE articles RENAME TO news;
  
  -- 새로운 컬럼 추가
  ALTER TABLE news ADD COLUMN create_at TEXT NOT NULL;
  -- 에러 남 why? 값이 없으니까
  ```

  ```bash
  Runtime error near line 4: Cannot add a NOT NULL column with default value NULL
  ```

  해결 방법 2가지

  - NOT NULL 설정 없이 추가하기
  - 기본 값(default) 설정하기

  ```sql
  -- 1. NOT NULL 설정 없이 추가
  ALTER TABLE news ADD COLUMN create_at TEXT;
  
  INSERT INTO news VALUES ('제목', '내용', datetime('now'));
  ```

  | title    | content  | create_at           |
  | -------- | -------- | ------------------- |
  | 1번 제목 | 1번 내용 | NULL                |
  | 제목     | 내용     | 2022-03-14 06:32:59 |

  ```sql
  -- 2. 디폴트값 넣고 새 컬럼 추가
  ALTER TABLE news ADD COLUMN subtitle TEXT NOT NULL DEFAULT '소제목';
  ```

  | title    | content  | create_at           | subtitle |
  | -------- | -------- | ------------------- | -------- |
  | 1번 제목 | 1번 내용 | NULL                | 소제목   |
  | 제목     | 내용     | 2022-03-14 06:32:59 | 소제목   |

  ```sql
  -- column 이름 수정
  ALTER TABLE news RENAME COLUMN title TO main_title;
  ```

  | main_title | content  | create_at           | subtitle |
  | ---------- | -------- | ------------------- | -------- |
  | 1번 제목   | 1번 내용 | NULL                | 소제목   |
  | 제목       | 내용     | 2022-03-14 06:32:59 | 소제목   |

  ```sql
  -- column 삭제
  ALTER TABLE news DROP COLUMN subtitle;
  ```

  | main_title | content  | create_at           |
  | ---------- | -------- | ------------------- |
  | 1번 제목   | 1번 내용 | NULL                |
  | 제목       | 내용     | 2022-03-14 06:32:59 |



※ SQLite Tutorial사이트 들어가서 내용 살펴볼 수 있음