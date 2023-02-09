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

- 예시

  ADDR(주소지)로 그룹핑하고 여성만 필터링하여 회원수 집계

  ```sql
  SELECT ADDR, COUNT(WOMAN_NO) AS WOMAN_CNT FROM MEMBER
  WHERE GENDER = 'WOMAN'
  GROUP BY ADDR
  ```

  

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



## 집계함수

- `COUNT`
- `SUM`
- `AVG`
- `MAX`
- `MIN`
- `STDEV` : 표준편차
- `VAR` : 분산



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

- if 문 방식

  ```sql
  CASE WHEN {조건식} THEN {반환값}
  WHEN {조건식2} THEN {반환값2}
  ...
  ELSE {조건에 만족하지 않을 경우 반환값}
  END
  ```

  

  ```sql
  SELECT PT_NAME, PT_NO, GEND_CD, AGE,
  CASE WHEN TLNO IS NULL THEN 'NONE' WHEN TLNO IS NOT NULL THEN TLNO END AS TLNO
  ```

  
