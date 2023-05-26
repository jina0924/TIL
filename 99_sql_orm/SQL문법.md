# SQL 문법

[toc]

## SELECT

> 데이터 조회

- 모든 컬럼 조회

  ```sql
  SELECT * FROM {TABLE_NAME}
  ```

- 여러 컬럼 조회

  ```sql
  SELECT {COLUMN}, {COLUMN}, ... FROM {TABLE_NAME}
  ```

  

### AS

> 컬럼 혹은 테이블 별칭 사용

```sql
SELECT {COLUMN} AS {COLUMN_ALIAS} FROM {TABLE_NAME} AS {TABLE_ALIAS}
```



## DISTINCT

> 중복된 데이터를 제외하고 조회

```sql
SELECT DISTINCT {COLUMN} FROM {TABLE}
# TABLE 테이블의 COLUMN 필드에서 중복되는 값 제외한 후 조회
```



## LIMIT

> 지정한 개수만큼 데이터 조회

```sql
SELECT {COULMN} FROM {TABLE} LIMIT {CNT}
```



## WHERE

> 조건에 따른 검색

- 비교 연산자
  - `=`, `<>`(같지 않다), `>`, `<`, `>=`, `<=`
- 논리 연산자
  - `NOT`, `AND`, `OR`
- LIKE 연산자
  - 대표 문자를 이용하여 지정된 속성의 값이 문자 패턴과 일치하는 데이터 검색
  - `%` : 모든 문자를 대표함
  - `_` : 문자 하나를 대표함
  - `#` : 숫자 하나를 대표함
- 연산자 우선순위 : 산술 연산자 -> 관계 연산자(비교 연산자) => 논리 연산자



### 조건식 종류

### BETWEEN

> 두 값 사이에 존재하는 값만 조회

```sql
SELECT {COL1} FROM {TABLE} WHERE {COL2} BETWEEN {VAL1} AND {VAL2}
```

- 예시

  ```sql
  SELECT CAR_ID
  FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
  WHERE MONTH(START_DATE) BETWEEN 8 AND 10
  ```

  

### IN

> 해당 데이터 중 조건으로 준 값이 있는지 확인

```sql
SELECT {COL1} FROM {TABLE1} WHERE {COL2} IN {SUB_QUERY_DATASET}
```

- 예시

  ```sql
  SELECT * FROM TABLE WHERE A IN (1, 2, 3)
  SELECT * FROM TABLE WHERE A NOT IN (1, 2, 3)
  ```



### LIKE

> 정규표현식과 같이 문자의 패턴을 비교하는 데 사용

- 특정값으로 시작하는 데이터 검색

  ```sql
  WHERE {COLUMN} LIKE '{특정값%}'
  ```

- 특정값을 포함하는 데이터 검색

  ```sql
  WHERE {COLUMN} LIKE '{%특정값%}'
  ```

- 특정값으로 끝나는 데이터 검색

  ```sql
  WHERE {COLUMN} LIKE '{%특정값}'

- 특정값으로 시작하고 뒤에 다른 문자가 하나 더 있는 데이터 검색

  ```sql
  WHERE {COLUMN} LIKE '{특정값_}'
  ```

  

## ORDER BY

> 데이터를 정렬

- 특정 필드 기준으로 정렬

  ```sql
  SELECT {COULMN} FROM {TABLE} ORDER BY {COULMN}
  ```

  - 예시

    ```sql
    SELECT * FROM TABLE ORDER BY A
    ```

  - `ASC` : 오름차순 정렬(기본값)

  - `DESC` : 내림차순 정렬

- 정렬 기준이 여러 개인 경우

  ```sql
  SELECT {COLUMN} FROM {TABLE} ORDER BY {COLUMN1}, {COLUMN2} DESC, {COLUMN3} ASC
  # COLUMN1 기준으로 오름차순 정렬 -> COLUMN2 기준으로 내림차순 정렬 -> COLUMN3 기준 오름차순으로 정렬
  ```



## GROUP BY

> 조건에 따라 집게된 값을 가져옴
>
> 집계함수와 자주 쓰이게 됨

```sql
SELECT {COLUMN} FROM {TABLE} GROUP BY {COLUMN}
```

- `GROUP BY` 뒤에 열 이름을 직접 적는 대신 열의 위치로 대신하여 적을 수 있음

  - 예시

  ```sql
  SELECT FOOD_TYPE, REST_NAME, FAVORITES FROM REST_INFO GROUP BY 1, 2
  ```
  
  
  
- 예시

  ADDR(주소지)로 그룹핑하고 여성만 필터링하여 회원수 집계

  ```sql
  SELECT ADDR, COUNT(WOMAN_NO) AS WOMAN_CNT FROM MEMBER
  WHERE GENDER = 'WOMAN'
  GROUP BY ADDR
  ```



### 집계함수

- `COUNT` : 행의 개수를 세어줌
  - `COUNT(NAME)`이면 `NAME` 값이 `NULL`이 아닌 행의 개수를 셈

- `SUM` : 행 안에 있는 값의 합을 내어줌
- `AVG` : 행 안에 있는 값의 평균을 내어줌
- `MAX` : 행 안에 있는 값의 최댓값을 반환해줌
- `MIN` : 행 안에 있는 값의 최솟값을 반환해줌
- `STDEV` : 표준편차
- `VAR` : 분산



### HAVING

> GROUP BY로 테이블 그룹핑 후, 특정 조건으로 필터링

- 예시

  ADDR(주소지)별로 회원수를 집계하되, 여자만 뽑고, 회원수가 50 이상만 나오도록 조회

  ```sql
  SELECT ADDR, COUNT(WOMAN_NO) AS WOMAN_CNT FROM MEMBER
  WHERE GENDER = 'WOMAN'
  GROUP BY ADDR
  HAVING COUNT(WOMAN_NO) >= 50
  # HAVING 다음에 SELECT가 실행되므로 ALIAS로 HAVING 적으면 안됨



## 숫자 함수

- `ROUND(값, 자리수[, 반올림 여부])` : 반올림
- `CEILING(값)` : 올림(정수값 출력)
- `FLOOR(값)` : 버림(정수값 출력)
- `TRUNC` : 소수점 버림
- `MOD` : 나머지



## JOIN

> 2개 이상의 다른 테이블을 결합시키는 것
>
> JOIN을 하려면 반드시 공통열(key)이 있어야 함



### INNER JOIN(JOIN)

> 교집합. 두 테이블의 공통값이 매칭되는 데이터만 조회

- 예시

  ```sql
  SELECT * FROM TABLE_A
  JOIN TABLE_B ON TABLE_A.NAME = TABLE_B.NAME



### OUTER JOIN

> 합집합. 두 테이블 간의 공통값으로 매칭되는 값 뿐만 아니라 매칭되지 않는 데이터까지 조회

- `LEFT JOIN`, `RIGHT JOIN`, `FULL JOIN`

- 예시

  ```sql
  SELECT FIRST_HALF.FLAVOR FROM FIRST_HALF
  LEFT JOIN ICECREAM_INFO ON FIRST_HALF.FLAVOR = ICECREAM_INFO.FLAVOR
  ```

  - `FIRST_HALF` 테이블 기준으로 `LEFT JOIN`하려면 `FROM` 절에 `FIRST_HALF`를, `LEFT JOIN`절에는 `ICECREAM_INFO`를 써야함

https://suy379.tistory.com/105



## DATE_FORMAT

> 날짜 포맷을 변경하는 함수

```sql
DATE_FORMAT(date, format)
```

- 예시

  ```sql
  SELECT DATE_FORMAT('20230209', '&Y/%m/%d')
  # 2023/02/09
  
  SELECT DATE_FORMAT('2023-02-09', '%W %M %Y')
  # Thursday February 2023
  ```

  

## CASE

> 조건에 따라 서로 다른 값을 반환

- 형식

  ```sql
  CASE WHEN {조건식} THEN {반환값}
  WHEN {조건식2} THEN {반환값2}
  ...
  ELSE {조건에 만족하지 않을 경우 반환값}
  END
  ```

  - 예시

  ```sql
  SELECT PT_NAME, PT_NO, GEND_CD, AGE,
  CASE WHEN TLNO IS NULL THEN 'NONE' WHEN TLNO IS NOT NULL THEN TLNO END AS TLNO
  ```




## IF

> 조건에 따라 서로 다른 값을 반환

- 형식

  ```sql
  IF (조건문, 참일 때 값, 거짓일 때 값)
  ```

  - 예시

    ```sql
    SELECT CAR_ID, IF(MAX(END_DATE) >= '2022-10-16', '대여중', '대여 가능') AS AVAILABILITY
    ```

    

## DATEDIFF

> MySQL
>
> 두 날짜 간의 차이 출력

```sql
SELECT DATEDIFF(DATE1, DATE2)
# DATE1 - DATE2 리턴
```

- 예시

  ```sql
  SELECT HISTORY_ID, CAR_ID,
  DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE,
  DATE_FORMAT(END_DATE, '%Y-%m-%d') AS END_DATE,
  CASE WHEN DATEDIFF(END_DATE, START_DATE) >= 29 THEN '장기 대여' ELSE '단기 대여' END AS RENT_TYPE
  FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
  ```



## 문자열 자르기

### SUBSTR

> Oracle

```sql
SUBSTR({문자열}, {시작위치}, {길이})
```

- 예시

  ```sql
  SELECT SUBSTR(PRODUCT_CODE, 1, 2) AS CATEGORY, COUNT(*) AS PRODUCTS
  ```

  

### SUBSTRING, LEFT, RIGHT

> MS-SQL, MySQL

```sql
SUBSTRING({문자열}, {시작위치}, {길이})
# 문자열에서 시작 위치부터 길이만큼 출력

LEFT({문자열}, {길이})
# 문자열에서 왼쪽부터 길이만큼 출력

RIGHT({문자열}, {길이})
# 문자열에서 오른쪽부터 길이만큼 출력
```

- 예시

  ```sql
  SELECT LEFT(PRODUCT_CODE, 2) AS CATEGORY, COUNT(*) AS PRODUCTS
  ```



## 문자열 연결

### CONCAT

> ORACLE은 매개변수 2개만 받음
>
> MySQL은 2개 이상의 매개 변수 허용

```sql
CONCAT(문자열1, 문자열2)
```

- 예시

  ```sql
  SELECT CONCAT('home/grap/src/', BOARD_ID, '/', FILE_ID, FILE_NAME, FILE_EXT) AS FILE_PATH
  FROM USED_GOODS_FILE
  ```



### CONCAT_WS

> MySQL

```sql
CONCAT_WS(구분자, 문자열 [, 문자열2, 문자열3 ...])
```



### ||

> ORACLE

```sql
(문자열1) || (문자열2) || (문자열3) || ...
```



## 서브쿼리

>  하나의 SQL문에 포함되어 있는 또다른 SQL문

- 서브쿼리를 괄호로 감싸서 사용

- 서브쿼리는 단일행 또는 복수행 비교 연산자와 함께 사용 가능

- 서브쿼리에서는 `ORDER BY`를 사용하지 못함

- 서브쿼리가 사용 가능한 곳
  - `SELECT`절
  - `FROM`절
  - `WHERE`절
  - `HAVING`절
  - `ORDER BY`절
  - `INSERT`문의 `VALUES`절
  - `UPDATE`문의 `SET`절

- 예시

  ```sql
  /*
  CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블에서 대여 시작일을 기준으로 2022년 8월부터 2022년 10월까지 총 대여 횟수가 5회 이상인 자동차들에 대해서 해당 기간 동안의 월별 자동차 ID 별 총 대여 횟수(컬럼명: RECORDS) 리스트를 출력하는 SQL문을 작성해주세요. 결과는 월을 기준으로 오름차순 정렬하고, 월이 같다면 자동차 ID를 기준으로 내림차순 정렬해주세요. 특정 월의 총 대여 횟수가 0인 경우에는 결과에서 제외해주세요.
  */
  SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(HISTORY_ID) AS RECORDS
  FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
  WHERE CAR_ID IN (
      SELECT CAR_ID
      FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
      WHERE MONTH(START_DATE) BETWEEN 8 AND 10
      GROUP BY CAR_ID
      HAVING COUNT(HISTORY_ID) >= 5)
      AND MONTH(START_DATE) BETWEEN 8 AND 10
  GROUP BY MONTH, CAR_ID
  HAVING COUNT(HISTORY_ID) >= 0
  ORDER BY MONTH, CAR_ID DESC
  ```
  
  ```sql
  /*
  REST_INFO 테이블에서 음식종류별로 즐겨찾기수가 가장 많은 식당의 음식 종류, ID, 식당 이름, 즐겨찾기수를 조회하는 SQL문을 작성해주세요. 이때 결과는 음식 종류를 기준으로 내림차순 정렬해주세요.
  */
  SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
  FROM REST_INFO
  WHERE FAVORITES IN (
      SELECT MAX(FAVORITES)
      FROM REST_INFO
      GROUP BY FOOD_TYPE)
  GROUP BY FOOD_TYPE
  ORDER BY FOOD_TYPE DESC
  ```
  



### WITH

> 반복되는 서브쿼리 블록을 임시테이블로 만들어 재사용 가능

```sql
# 1개의 임시테이블
WITH 임시테이블명 AS (
	서브쿼리문 (SELECT절)
)
SELECT 컬럼[, 컬럼, ...]
FROM 임시테이블명
```

```sql
# 2개 이상의 임시테이블
WITH
임시테이블명1 AS (
	서브쿼리문 (SELECT절)
),
임시테이블명2 AS (
	서브쿼리문 (SELECT절)
)
SELECT 컬럼[, 컬럼, ...]
FROM 임시테이블명1, 임시테이블명2
```



#### WITH RECURSIVE

```sql
WITH RECURSIVE 임시테이블명 AS (
    초기 쿼리
    UNION RECURSIVE_QUERY WHERE 반복할_조건
	)
```

- 예시

  ```sql
  # 각 시간대별 ROW값 가진 테이블 만들기
  WITH RECURSIVE TIME AS(
      SELECT 0 AS HOUR
      UNION SELECT HOUR + 1 FROM TIME WHERE HOUR < 23
  )
  ```

  

## SQL 문법 순서

1. SELECT
2. FROM
3. WHERE
4. GROUP BY
5. HAVING
6. ORDER BY



## SQL 실제 실행 순서

1. FROM
2. ON
3. JOIN
4. WHERE
5. GROUP BY
6. HAVING
7. SELECT
8. DISTINCT
9. ORDER BY
