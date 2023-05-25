# SQLD 최종 정리

[toc]

## SQL 명령문 개괄

1. 연산순서
   - FROM - WHERE - GROUP BY - HAVING - SELECT - ORDER BY
   
2. 종류
   - DML
     - SELECT, INSERT, DELETE, UPDATE
   - DDL
     - ALTER, CREATE, MODIFY, DROP
   - TCL
     - ROLLBACK, COMMIT
   - DCL
     - GRANT, REVOKE



## SELECT

DISTINCT

- 집약
- Distinct (deptno, mgr) : 실제로는 괄호 적지 않음.
  - group by (deptno, mgr)과 비슷함



### AS

SELECT절에서 쓸 경우

1. AS 생략 가능
2. 컬럼명에 띄어쓰기



FROM

- AS 사용 불가



CONCAT

- 인수가 반드시 2개

- `+` : SQL SERVER
- `||` : ORACLE



## 논리 연산자

AND : 둘 다

OR : 둘 중 하나

NOT



연산순위

1. NOT

2. AND

3. OR

   ```sql
   NOT <조건>	# 조건1
   AND <조건>
   AND NOT <조건>	# 조건2
   OR <조건>
   ```

   ```sql
   조건1 AND 조건 AND 조건2	# 조건3
   OR 조건
   ```

   ```sql
   조건3 OR 조건
   ```



## SQL 연산자

BETWEEN AND

- `A BETWEEN 1 AND 2` => `1 <= A <= 2`



IN

- `IN (1, 2, 3)` => `A = 1 OR A =2 OR A = 3`



LIKE ⭐⭐⭐

- `_` : 미지의 한 글자
- `%` : 0이상의 글자
- ex) `_L%` => `두번째 글자가 L인 경우`



ESCAPE

- 와일드카드(`_`, `%`)를 문자로 취급해주는 함수

  ```sql
  ENAME LIKE 'A_A'
  	ESCAPE
  ```

  ```sql
  'A@_A'
  '@'
  ```

  - `@`가 아닌 아무 문자여도 가능함



Rownum(oracle)

1. Where 조건절에서 Rownum = 1 포함

2. ORDER BY가 가장 마지막에 실행됨 => 정렬 전 ROWNUM에 대한 조건절이 실행됨

   ```sql
   SELECT empno, sal
   FROM emp
   WHERE rownum <= 3
   ORDER BY sal
   ```



TOP(sqlserver)

- Select 옆에 씀
- `SELECT TOP n <컬럼명>` => 컬럼을 출력할 때 상위 n개를 가져옴



## NULL⭐⭐⭐⭐⭐

- 정의
  - 부재, 모르는 값
- 산술연산
  - NULL + 2, NULL - 4, NULL x NULL 등등 => NULL
- 비교연산
  - NULL = 2, NULL = 4 등은 알 수 없음(UNKNOWN)
    - `WHERE <조건>`에서 조건절에 들어가면 `FALSE`와 비슷한 기능을 함
- 정렬 상 의미
  - oracle : ∞
  - sqlserver : -∞



NVL

- `NVL (값1, 값2)`
  - 값1이 NULL이면 값2
  - 값1이 NULL이 아니면 값1

NVL2

- `NVL2 (값1, 값2, 값3)`
  - 값1이 NULL이면 값3
  - 값1이 NULL이 아니면 값2

ISNULL

- `ISNULL (값1, 값2)` = `NVL (값1, 값2)`

NULLIF

- `NULLIF (값1, 값2)`
  - 값1 = 값2이면 NULL
  - 서로 다르면 값1

COALESCE : 널 아닌 첫 번째값

- `COALESCE (값1, 값2, ...)`



## 정렬

- 정렬의 특성
  - 가장 마지막에 실행
  - 성능 느려질 가능성 있음
  - NULL값과의 관계
- 컬럼 번호로 정렬
  - 출력되는 컬럼의 수보다 큰 값 불허
  - 출력되지 않는 
- 인수 두 개 정렬
  - `SAL DESC ENAME ASC` => SAL이 같으면 ENAME 오름차순

- 출력되지 않는 컬럼명으로 정렬 가능
  - `SELECT ENAME ORDER BY SAL` 가능



## 숫자 함수

- ROUND
  - 인수 뭐 들어가는지
- CEIL(oracle) / CEILING(sql server)



## 문자열 함수

- UPPER
- LOWER



- LPAD
- RPAD
- LTRIM
- RTRIM



- SUBSTR
- NSTR



## 날짜 함수

- TO_CHAR
- T0_DATE
- SYSDATE(oracle)
- GETDATE(sql server)



- `날짜데이터 + 100` => 100일 이후(숫자를 DAY로 인식함)



## DECODE/CASE

> CASE만 나오는 편

```sql
CASE
	WHEN THEN
	WHEN TEHN
ELSE			# ELSE가 없을 때 조건1, 조건2 만족하지 않으면 NULL출력됨
END
```



## 집계함수⭐⭐

- NULL과의 관계

- EX)

  | A    | B    | C    | A+B+C |
  | ---- | ---- | ---- | ----- |
  | NULL | NULL | 1    | NULL  |
  | 3    | 2    | 2    | 7     |
  | NULL | 2    | 3    | NULL  |

  - `SUM(A) = 3`
  - `SUM(B) = 4`
  - `COUNT(A) = 1`
  - `COUNT(*) = 3`
  - `SUM(A + B + C) = 7`
  - `SUM(A) + SUM(B) + SUM(C) = 13`



## GROUP BY

- 집약기능
- WHERE 다음에 실행됨
- 그룹 수준으로 정보를 바꿈
- HAVING : GROUP BY의 조건식



## JOIN

- NATURAL JOIN, USING
  - 중복된 컬럼 하나만 출력 & 제일 앞에 등장
  - alias 사용 안됨
- LEFT OUTER JOIN
  - `A LEFT OUTER JOIN B` = `A COL1 = B COL1(+)`

- JOIN 하면할수록 COL 늘어남
- `FROM A, B, C` => A와 B JOIN => 앞에서 JOIN한 걸로 C와 JOIN



## 서브쿼리

- SELECT
  - scalar
- FROM
  - inline view
    - 메인쿼리의 컬럼 사용 가능
- WHERE
  - 거의 모든 서브쿼리 들어감(중첩 서브쿼리)
- GROUP BY : 서브쿼리 안들어감
- HAVING
  - 거의 모든 서브쿼리(중첩 서브쿼리)
- ORDER BY
  - scalar

  ```sql
  SELECT
  FROM A
  WHERE (
      SELECT
	    FROM B
      A COL1....
  ```

  - A row마다 서브쿼리 다 돎



- IN
- ANY/SOME
- ALL
- EXIST
  - `'1'`, `'X'`, `'a'` => TRUE
  - `0 rows` => FALSE



## 집합연산자

- UNION
  - 합집합
- INTERSECT
  - 교집합
- MINUS(oracle) / EXCEPT(sql server)
  - 차집합
- UNIONALL
  - 중복데이터 존재
  - 정렬작업 없음(위에 있는 것들은 정렬 작업 있음 => 느림)
  - 빠름



## DDL

- TCL과 연관지어서 생각할 것
- TRUNCATE vs. DROP
  - TRUNCATE : 입주민 퇴거 => 구조 남음
  - DROP : 건물 철거 => 구조 삭제
- TRUNCATE vs. DELETE
  - DDL vs. DML => ROLLBACK, COMMIT과 엮어서 나옴



## DML

- TCL(COMMIT, ROLLBACK과 연관지어 나옴)
  - INSERT
    - `INSERT ( ) VALUES( )`에 넣는 인수 개수 서로 같아야함
  - UPDATE
  - DELETE



- MERGE
  - 신유형(기출 37회)



## 제약조건⭐⭐⭐

- PK
  - UNIQUE + NOT NULL
- UNIQUE
- NOT NULL



## DCL

> 정의 물어보는 문제 나옴
>
> 문법 살펴보기

- GRANT
- REVOKE
-  ROLE 특징
  - 명령어 아님
  - object



## VIEW

- 독립성
  - 기존 테이블이 구조가 변경되면 VIEW의 구조가 같이 변경됨
- 편리성
  - 계속 테이블을 조작할 필요 없이 쓸때마다 나옴
- 보안성
  - 원하는 정보만 얻고 나머지 숨길 수 있음
- 테이블 자체가 아니라 SQL 명령문을 저장함 => 따로 저장공간이 필요하지만 기존 테이블보다 적게 필요함



## 그룹함수⭐⭐⭐

- ROLLUP
  - `ROLLUP (A, B)`와 `ROLLUP (B, A)`는 서로 다른 결과(계층 구조로 진행되기 때문)
- CUBE
  - `CUBE(A, B)` = `CUBE(B, A)`

- GROUPINGSETS
  - ROLLUP인지 CUBE인지 GROUPINGSETS인지 판단하는 방법
    1. NULL 다 찾기
    2. 총합행이 있는지 찾기
       - 없으면 GROUPINGSETS
       - 있으면 ROLLUP, CUBE
         - 양쪽으로 결과가 나오면 CUBE
         - 한 쪽만 결과가 나와서 계층으로 나오면 ROLLUP
- GROUPING



## TCL

- COMMIT

  ```sql
  AUTO COMMIT OFF
  	AND
  BEGIN TRANSACTION
  # DDL에 COMMIT기능 없앤 것
  ```

  

- ROLLBACK



## 윈도우 함수

> 무조건 문제풀기

- ROWS

- RANGE

  => 차이점 익혀두기

- RANK : 중복 건너뜀
- DENSE RANK : 중복 건너뛰기X



- PARTITION BY
- ORDER BY



## 계층형 질의

- PRIOR 자식데이터 = 부모데이터
  - 부모데이터 = PRIOR 자식데이터 랑 같은 의미
- 부모에서 자식으로 가는 경우 순방향


- EX)
  | level 1 | KING  | empno |
  | ------- | ----- | ----- |
  | level 2 | JAMES | mgr   |
  | level 3 | SCOTT |       |
  
  - PRIOR empno = mgr



## 절차형 PL/SQL

- EXCEPTION => 생략 가능
- Procedure, trigger, user defined function 차이점
  - trigger : commit, roll back 안됨. DML 많이 씀
  - procedure : 반드시 값이 안나옴
  - user defined function : 반드시 값 나옴



## 데이터 모델링

- 소프트웨어 개발 방법론
  1. 데이터 구조화
  2. 관계형 데이터베이스
  3. 객체지향 프로그래밍



## 엔터티

- 업무 상 관리하고자 하는 대상
- 특징
- 분류
  - 유형 / 개념 / 사건
  - 기본 / 중심 / 행위



## 속성

- 관리하고자 하는 대상인 instance의 특성
- 분류
  - 기본 속성 / 설계 속성 / 파생 속성 => 정의 확인할 것



## 도메인

- 데이터 유형, 크기, 제약 조건
- 물리적 데이터 모델링 => check, primary key, ...



## 관계

- IE 표기법
- Barker 표기법



## 식별자

- 주식별자 특징
  - 유일성 / 최소성 / 불변성 / 존재성 => 모두 만족하면 후보키 될 수 있음 => 대표로 선정되면 기본키 



## 식별자 관계, 비식별자 관계

|      | 식별                              | 비식별                            |
| ---- | --------------------------------- | --------------------------------- |
|      | 강한 관계                         | 약한 관계                         |
| 단점 | SQL 구문 복잡<br />pk 속성수 증가 | 불필요한 조인 많이 생김 => 느려짐 |
| 선   | 실선                              | 점선                              |



- ERD 서술 규칙
  - 시선 좌상단 -> 우하단
  - 관계명 반드시 표기하지 않아도 됨
  - UML은 객체지향모델링에서만 쓰임



## 성능 데이터 모델링

- 아키텍처 모델링
  - 아키텍처 = 구조
- SQL 명령문 수정
  - 조인 수행 원리⭐
  - optimizer
  - 실행계획



## 정규화⭐⭐⭐⭐⭐

- 정규화 방법
  - 1차 : 원자성 확보
  - 2차 : 부분원소 종속성 제거
  - 3차 : 이행함수 종속 제거
  - BCNF : 후보키가 상속하는것 제거

- 이상현상
- 성능
  - select에서는 join때문에 성능 저하
  - insert, update에서는 테이블이 작아지므로 성능 향상



## 반정규화

- 데이터 무결성 해침⭐
  - 대량범위
  - 범위처리
  - 통계처리
- 방법
  - 테이블
    - 병합 : 1:1, 1:M, 슈퍼/서브타입
    - 분할 : 부분테이블 병합, 통계 테이블, 중복 테이블
  - 속성
    - 파생
    - 오류
    - 이력컬럼
    - pk를 일반 속성으로 편입
    - 중복속성
  - 관계
    - 중복 관계 추가



## 데이터에 따른 성능

- row migration

- row chaining

  => 해결하기 위해 list, range, hash partitioning



## 슈퍼/서브타입

- 용량별로 처리 가능
  - 적은 경우 => one to one(트랙잭션이 개별로 들어감)
  - 큰 경우 => 바로 트랙잭션으로 들어감
    - 공통/차이
    - 전체 통합 (single type)
- transaction에 따라 처리 가능



## 분산데이터베이스

- 특징
  - 반정규화와 유사 => 데이터 무결성 해짐
  - 투명성 떨어짐



## 조인 수행 원리⭐⭐⭐

> 문제 많이 풀어보기

- NL
  - 랜덤액세스
  - 대용량 소트 작업시 유리
- Sort merge
  - 조인 키를 기준으로 정렬
  - 등가/비등가 조인
- Hash
  - 등가 조인 only
  - 선행테이블 작음
  - Hash 처리를 하기 때문에 별도 저장공간 필요



## 옵티마이저

- CBO
  - 경로를 다 짜봤을 때 경제적인 것으로
- RBO
  - 규칙에 따라서 옵티마이징



## 인덱스

- 사용 시기
  - 부정형, LIKE, 묵시적 형변환에서 안씀
- 인덱스 사용시 성능 감소되는 것
  - INSERT, UPDATE, DELETE(DML) 성능 저하



## 실행계획

- 순서⭐



정규화

PIVOT / UNPIVOT

Merge
