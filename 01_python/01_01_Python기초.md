# Python 기초

[toc]





## 컴퓨터 프로그래밍 언어

1. 컴퓨터
   - calculation  + remember

2. 프로그래밍
   - program : 일련의 명령어 모음(집합)
3. 언어

**컴퓨터에게 명령하기 위한 약속**

선언적 지식 : 사실에 대한 내용

명령적 지식 : How -to -> 컴퓨터 프로그래밍 언어가 어려운 이유



## 파이썬 개발 환경



### 파이썬이란?

- 간결한 문법 : 읽기 쉬운 언어
- 인터프리터 언어
- 객체 지향 프로그래밍



### 파이썬 개발환경 종류

> 어떤 식으로 파이썬을 사용할 것인가?

- 대화형 환경

  - 파이썬 기본 인터프리터
  - 쥬피터 노트북 -> 실습
    - IDLE의 확장판
    - 데이터분석 / 머신러닝 / 딥러닝 시 많이 활용

- 스크립트 실행 -> 금요일 관통프로젝트 / 평가

  - text editor : 메모장의 확장판 ex) Visual Studio Code -> 코딩(웹 개발)에서 씀

  - IDE : 통합개발환경 ex) Pycharm -> 알고리즘에서 쓰게 됨



## 기초 문법

### 코드 스타일 가이드

- 파이썬에서 제안하는 스타일 가이드 : PEP8
  - 일관적인 코드 작성스타일의 필요

### 들여쓰기

- 4칸(space키 4번) 사용 권장



### 변수(Variable) ★

> 어떻게 저장하고, 이름을 지을까?
>
> `이름 = 값`

- 변수란?

  - 컴퓨터 메모리 어딘가에 저장되어 있는 객체를 참조하기 위해 사용되는 이름

  - 다른 객체를 언제든 할당할 수 있음

    - 객체(object) : things

  - 변수는 할당 연산자(=)를 통해 값을 할당

  - type() ★

    - 변수에 할당된 값의 타입

      ```python
      x = 'string'
      y = 123
      print(type(x), type(y))
      ```
  
      <class 'str'> <class 'int'>

  - 변수 연산
  
    ```python
    i = 5
    j = 3
    s = '파이썬'
    ```
  
    - 숫자 + 숫자
    - 문자 + 문자 : 문자를 연결
    - 문자 * 숫자 : 문자를 숫자만큼 반복
  
    ```python
    i = i - j	# i-j의 값을 i에 할당함
    print(i)
    ```
  
    2
  
    ```python
    s = s * 3
    print(s)
    ```
  
    파이썬파이썬파이썬
  
    - 같은 값을 동시에 할당 할 수 있음
    
      ```python
      x = y = 1004
      print(x, y)		# 1004 1004
      ```
  
    - 다른 값을 동시에 할당 할 수 있음
    
      ```python
      x, y = 1, 2
      print(x, y)		# 1 2
      ```
    
    - 실습 문제
    
      ```
      x = 10, y = 20 일 때,
      각각의 값을 바꿔서 저장하는 코드를 작성하시오.
      ```
    
      ```python
      x, y = 10, 20
      tmp = x		# 임시 변수 활용(새 그릇을 가져와서 잠시 담아둔다고 생각할 것)
      x = y
      y = tmp
      print(x, y)
      ```
    
      ```python
      y, x = x, y		# Pythonic
      print(x, y)
      ```



- 식별자

  > 변수(박스)의 이름을 어떻게 지을 수 있을까?

  - 규칙

    - 영문 알파벳, 언더스코어(_), 숫자로 구성

    - 첫 글자에 숫자 올 수 x

    - 길이제한 없고, 대소문자 구별

    - CamelCase & snake_case : 후자를 좀 더 자주 씀

    - 키워드 / 예약어는 쓰지 않음

      ```python
      import keyword
      print(keyword.kwlist)
      ```
    
      ```
      ['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
      ```
    
    - 내장함수나 모듈 등의 이름으로도 만들면 안됨
    
      ```
      print(5)
      print = 'hi'
      print(5)		# TypeError
      ```
      
      ```python
      del print	# 뒤에서 진행될 코드에 영향이 갈 수 있으므로 앞서 만든 print 변수를 삭제해야함
      ```
      
      

- 사용자 입력
  - input([prompt])
    - 사용자로부터 값을 즉시 입력 받을 수 있는 내장함수
    
    ```python
    data = input()
    print(data * 2, type(data))
    ```
    
    123
    
    123123 <class 'str'>



- 주석
  - 컴퓨터는 이 부분을 실행하지 않음

  - 한 줄 주석 : `#` + 내용

  - 여러 줄 주석

    - 한 줄 씩 `#`을 사용

    - `"""` 또는 `'''` 

      ```python
      """
      이것은
      여러줄에 걸친
      주석을 만드는 코드입니다.
      """
      print('world')
      ```

      world

  - VS code에선 ctrl + l로 여러 줄 주석 작성 가능



## 파이썬 자료형

<img src="https://user-images.githubusercontent.com/45934087/148158891-fe28256b-1df4-4b83-ab51-54d06c107d20.png" alt="파이썬 자료형 분류" style="zoom: 50%;" />

### None

- 값이 없음을 표현하기 위한 타입

### Boolean Type

> True vs. False

- 다음은 모두 False로 반환
  `0, 0.0, (), [], {}, '', None`

- ```python
  bool([0])		# True
  ```

### Numeric Type

#### int (정수, integer)

- 모든 정수의 타입은 int

- 매우 큰 수를 나타낼 때 오버플로우 발생하지 않음(다른 언어에선 발생)

- 진수 표현

  - 2진수 : `0b`

    ```python
    0b10		# 2
    ```

  - 8진수 : `0o`

  - 16진수 : `0x`

#### float (부동소수점, 실수, floating point number)

- 정수가 아닌 모든 실수는 float 타입

- 부동소수점

  ```python
  11/2		#5.5
  ```


#### Floating point rounding error

- 부동소수점에서 실수 연산 과정에서 발생 가능

  - 값 비교하는 과정에서 정수가 아닌 실수인 경우 주의할 것

    ```python
    3.14 - 3.02 == 0.12		# 왼쪽은 0.12000000001
    ```

    False
  
  1. 기본적인 처리방법
  
     ```python
     a = 3.5 - 3.12
     b= 0.38
     
     abs(a -b0 <= 1e-10)
     ```
  
     True
  
  2. sys 모듈 이용
  
     ```python
     import sys
     abs(a -b) <= sys.float_info.epsilon	# 'epsilon'은 부동소수점 연산에서 반올림함
     ```
  
     True
  
  3. python 3.5부터 활용 가능한 math 모듈을 통해 처리
  
     ```python
     import math
     math.isclose(a, b)
     ```
  
     True

#### complex (복소수, complex number)

- 각각 실수로 표현되는 실수부와 허수부를 가짐

- 복소수는 허수부를 `j`로 표현함

  ```python
  a = 3+4j	# 중앙의 + 또는 - 연산자 주위에 공백을 포함해서는 안됨
  print(type(a))
  ```

  <class 'complex'>



### 문자열(String Type)

- 모든 문자는 str 타입

- 문자열은 (`'`)나 (`"`)를 활용하여 표기

  - 따옴표 안에 따옴표를 쓸 때는 서로 다른 것을 쓸 것
  - 하나로 통일해서 사용할 것

- Immutable : 불변함

  ```python
  a = 'my string?'
  a[-1] = '!'		# TypeError: 'str' object does not support item assignment
  ```

- Iterable : 반복 가능

  ```python
  a = '123'
  for char in a:
      print(char)
  ```
  
  1
  
  2
  
  3

#### 중첩따옴표

- 따옴표 안에 따옴표를 표현할 경우 -> 문자열 안에 쓰는 따옴표와 다른 따옴표로 묶음

#### 삼중따옴표

- 작은 따옴표나 큰 따옴표를 삼중으로 사용
  - 따옴표 안에 따옴표를 넣을 때
  - 여러줄을 나눠 입력할 때 편리
  - `"""`를 사용하도록 권장

#### Escape sequence

- 문자열 내에서 특정 문자나 조작을 위해서 역슬래시(`\`)를 활용하여 구분

  | 예약문자 | 내용(의미)                                                  |
  | -------- | ----------------------------------------------------------- |
  | `\n`     | 줄 바꿈(new line)                                           |
  | `\t`     | 탭                                                          |
  | `\r`     | 캐리지리턴                                                  |
  | `\0`     | 널(Null)                                                    |
  | `\\`     | `\`(이스케이프 문자열이 아니라 역슬래시를 표현하고 싶을 때) |
  | `\'`     | 단일인용부호(`'`)                                           |
  | `\"`     | 이중인용부호(`"`)                                           |

  

#### String Interpolation ★

> 문자열 사이에 변수를 넣고 싶을 때

- 변수를 활용하여 문자열을 만드는 법

  - `%-formatting` -> 거의 대부분 타 프로그래밍 언어에서 사용하는 방식

    - `%d` : 정수
    - `%f` : 실수
    - `%s` : 문자열

    ```python
    name = '길동'
    print('Hello, %s' % name)
    ```
  
    Hello, 길동
  
  - `str.format()`
  
    ```python
    name, score = '길동', 50
    print('Hello, {0}! 성적은 {1}'.format(name, score))
    ```

    Hello, 길동! 성적은 50
  
  - `f-strings` : python 3.6+
  
    ```python
    name, score = '길동', 50
    print(f'Hello, {name}! 성적은 {score}')
    ```
  
    Hello, 길동! 성적은 50
  
    - `f-strings` 에서는 형식을 지정할 수 있음
  
      ```python
      import datetime
      today = datetime.datetime.now()
      print(f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일 {today:%A}')
      ```
  
      오늘은 22년 -1월 31일 Monday
  
    - 연산과 출력형식 지정도 가능
  
      ```python
      pi = 3.141592
      f'원주율은 {pi:.3}. 반지름이 2일때 원의 넓이는 {pi*2*2}'
      ```
  
      변수가 해당자리에 있어 직관적으로 이해하기 쉬움
    



### 컨테이너

- 컨테이너란?
  - 여러 개의 값을 담을 수 있는 것
  - 순서가 있는 데이터(Ordered) vs. 순서가 없는 데이터(Unordered)
  - 순서가 있다 != 정렬되어 이다.
  - 시퀀스형(순서가 있음)
    - 리스트(가변)
    - 튜플
    - 레인지
  - 비시퀀스형(순서가 없음)
    - 세트(가변)
    - 딕셔너리(가변)

<img src="https://user-images.githubusercontent.com/45934087/148164052-3b12d3a2-a95e-4d4d-ae25-86ca1ba9657b.png" alt="컨테이너 분류" style="zoom:50%;" />



## 시퀀스형 컨테이너

> sequence : 데이터가 순서대로 나열된 형식 ≠ 정렬되었다(sorted)

- 특징
  - 순서가 있음
  - 특정 위치의 데이터를 가리킬 수 있음

### 리스트

- 순서를 가지는 0개 이상의 객체를 참조하는 자료형
  - 가변자료형
  - 순서는 0부터 시작함

#### 생성과 접근

- 대괄호(`[]`) 혹은 `list()`를 통해 생성
- 순서가 있는 시퀀스로 인덱스를 통해 접근 가능
  - 값에 대한 접근은 `list[index]`
  - 시작은 0, 맨 마지막 인덱스는 -1

```python
my_list = []
another_list = list()
```

- `len(list)` : 리스트 길이

```python
boxes = ['a', 'b', ['apple', 'banana', 'cherry']]
len(boxes)		# 3
boxes[2]		# ['apple', 'banana', 'cherry']
boxes[2][-1]		# cherry
boxes[-1][1][0]		# b
```



### 튜플(Tuple)

- 리스트와의 차이점 : 불변 자료형 ★
- 항상 소괄호 형태로 출력



#### 생성과 접근

- 소괄호(`()`) 혹은 `tuple()`을 통해 생성
- 수정 불가능한(immuable) 시퀀스. 인덱스로 접근 가능
  - 값에 대한 접근은 `my_tuple[i]`

```python
a = (1, 2, 3, 1)
a[1]		
```



#### 생성시 주의사항

- 단일 항목의 경우

  - 하나의 항목으로 구성된 튜플은 새엉 시 값 뒤에 쉼표를 붙여야 함

    ```python
    a = 1,
    print(a, type(a))
    ```
    
    1 <class 'tuple'>

- 복수항목의 경우

  - 마지막 항목에 붙은 쉼표는 불필요

  

#### 튜플 대입

- 튜플 대입이란?

  - 우변의 값을 좌변의 변수에 한번에 할당하는 과정

- 튜플은 일반적으로 파이썬 내부에서 활용

  - 추후 함수에서 복수의 값을 반환하는 경우에도 활용

    ```python
    x, y = 1, 2
    print(x, y)		# 1 2
    ```

    



### 레인지

- 숫자의 시퀀스를 나타내기 위해 사용

  - 기본형 : `range(n)`

    - 0부터 n-1까지의 숫자 시퀀스

  - 범위 지정 : `range(n, m)`

    - n부터 m-1까지 숫자의 시퀀스

  - 범위 및 스텝 지정 : `range(n, m, s)`

    - n부터 m-1까지 s만큼 증가시키며 숫자의 시퀀스

      ```python
      list(range(6, 1, -1))
      [6, 5, 4, 3, 2]
      ```



### 패킹 / 언패킹

- 모든 시퀀스형(리스트, 튜플 등)은 패킹/언패킹 연산자`*`를 사용하여 객체의 패킹 또는 언패킹 가능

- 패킹
  - 대입문의 좌변 변수에 위치
  
  - 우변의 객체 수가 좌변의 변수 수보다 많을 경우 객체를 순서대로 대입
  
  - 나머지 항목들은 모두 별 기호 표시된 변수에 리스트로 대입
  
    ```python
    x, *y = 1, 2, 3, 4
    print(x, y, type(x), type(y))
    ```
  
    1 [2, 3, 4] int list
  
- 언패킹

  - argument 이름이 `*`로 시작하는 경우, argument unpacking이라고 부름
  - 패킹의 경우, 리스트로 대입
  - 언패킹의 경우, 튜플 형태로 대입



## 비시퀀스형 컨테이너

### 셋(set)

- 순서없이 0개 이상의 해시가능한 객체를 참조하는 자료형
- 담고있는 객체를 삽입 변경, 삭제 가능
- 수학에서의 집합

#### 셋 생성

- 중복없이 준서가 없는 자료구조
  - 인덱스 접근 불가능
  - 중괄호(`{}`) 혹은 `set()`을 통해 생성
    - 빈 set을 만들기 위해서는 `set()`을 반드시 활용해야 함 -> `{}`는 비어있는 dictionary
  - 활용 가능한 연산자는 차집합(`-`), 합집합(`|`), 교집합(`&`)

#### 셋 활용

- 셋을 활용하면 다른 컨테이너에서 중복된 값을 쉽게 제거할 수 있음
  - 단, 이후 순서가 무시되므로 순서가 중요한 경우 사용할 수 없음

```python
my_list = ['서울', '서울', '부산', '광주']
len(set(my_list))		# 3
```



### 딕셔너리

- 순서 없이 키-값(key-value) 쌍으로 이뤄진 객체를 참조하는 자료형

#### 딕셔너리 생성

- 중괄호(`{}`) 혹은 `dict()`을 통해 생성
  - **key에는 변경 불가능한 데이터(immutable)만 활용 가능**
    - string, integer, float, boolean, tuple, range
  - value는 모든 값으로 설정 가능
  - dict[key] 로 value에 접근 가능
  
  

### 형 변환(Typecasting)

- 암시적 형 변환(Implicit)
  - 파이썬 내부적으로 자료형을 변환
- 명시적 형 변환(Explicit)
  - 사용자가 직접 의도적으로 자료형을 변환

#### 암시적 형 변환

- bool
- Numeric type(int, float, complex)

```python
True + 3		# 4 (1 + 3)
3 + 5.0			# 8.0
3 + 4j + 5		#(8+4j)
```

#### 명시적 형 변환

- `int()`

  - str(형식에 맞는 문자열만), float

  ```python
  '3' + 4			# TypeError
  int('3') + 4		# 7
  ```

- `float()`

  - str(형식에 맞는), int

- `str()` : 모든 타입들이 문자열로 변환 가능



### 컨테이너 형 변환

- range, dictionary 는 다른 것에서 변환 불가능

  <img src="https://user-images.githubusercontent.com/18046097/61180466-a6a67780-a651-11e9-8c0a-adb9e1ee04de.png" alt="컨테이너형 형변환" style="zoom: 50%;" />

  - 행에서 열로 바꿀 수 있는지 없는지 나타냄

  

## 연산자

### 산술 연산자

- 기본적인 사칙연산 및 수식 계산

  - `divmod(n, m)` : (몫, 나머지) 튜플을 결과로 내줌

  | 연산자 | 내용                                             |
  | ------ | ------------------------------------------------ |
  | `+`    | 덧셈                                             |
  | `-`    | 뺄셈                                             |
  | `*`    | 곱셈                                             |
  | `/`    | 나눗셈 (항상 float를 돌려줌)                     |
  | `//`   | 몫                                               |
  | `%`    | 나머지(modulo) -> 홀수, 짝수 구별할 때 자주 사용 |
  | `**`   | 거듭제곱                                         |

  



### 비교 연산자

- 값을 비교하며, True / False 값을 리턴함
  
  | 연산자   | 내용                        |
  | -------- | --------------------------- |
  | `<`      | 미만                        |
  | `<=`     | 이하                        |
  | `>`      | 초과                        |
  | `>=`     | 이상                        |
  | `==`     | 같음                        |
  | `!=`     | 같지 않음                   |
  | `is`     | 객체 아이덴티티             |
  | `is not` | 객체 아이덴티티가 아닌 경우 |
  
  




### 논리 연산자

| 연산자    | 내용                         |
| --------- | ---------------------------- |
| `a and b` | a와 b 모두 True시만 True     |
| `a or b`  | a와 b 모두 False시만 False   |
| `not a`   | True -> False, False -> True |

- 일반적으로 비교연산자와 함께 사용됨

  ```python
  num = 100
  num >= 100 and num % 3 == 1
  ```

#### 논리 연산자 단축평가

- 결과가 확실한 경우 두번째 값은 확인하지 않고 첫번째 값 반환

  - and 연산에서 첫번째 값이 False인 경우 무조건 False => 첫번째 값 반환
  - or 연산에서 첫번째 값이 True인 경우 무조건 True => 첫번째 값 반환

  ```python
  a = 5 and 4
  print(a)		# 4
  
  b = 5 or 3
  print(b)		# 5
  
  c = 0 and 5
  print(c)		# 0
  
  d = 5 or 0
  print(d)		# 5
  ```

#### 복합 연산자

- 연산과 대입이 함께 이뤄짐

  | 연산자    | 내용       |
  | --------- | ---------- |
  | `a += b`  | a = a + b  |
  | `a -= b`  | a = a - b  |
  | `a *= b`  | a = a * b  |
  | `a /= b`  | a = a / b  |
  | `a //= b` | a = a // b |
  | `a %= b`  | a = a % b  |
  | `a **= b` | a = a ** b |

```python
cnt = 0
while cnt < 3:
    print(cnt)
    cnt += 1
```

```python
0
1
2
```





#### 식별 연산자

- `is`연산자를 통해 동일한 object인지 확인



#### 멤버십 연산자

- 요소가 시퀀스에 속해있는지 확인

  - `in`
  - `not in`

  ```python
  1 in [3, 2]		# F
  4 in (1, 2, 'hi')		# F
  'a' in 'apple'		# T
  ```

  

#### 시퀀스형 연산자

- 산술연산자(`+`)
  - 시퀀스간의 연결 / 인쇄
- 반복연산자(`*`)
  - 시퀀스를 반복

#### 기타 : 인덱싱(Indexing)

- 시퀀스의 특정 인덱스 값에 접근 (`[]`를 통해 값에 접근)
  - 맨 처음은 0, 맨 마지막은 -1
  - 해당 인덱스가 없는 경우 IndexError

#### 기타 : 슬라이싱

- `[:]`을 통해 슬라이싱

  - Sequence[start:end[:step]]
  
  ```python
  s = 'abcdefghi'
  s[2:5]		# cde
  s[-6:-2]		# defg
  s[2:-4]			# cde
  s[2:5:2]		#ce
  s[-6:-1:3]		#dg
  s[:3]		# abc
  s[5:]		# fghi
  s[::]		# abcdefghi
  s[::-1]		# ihgfedcba
  ```

#### 기타 : set 연산자

- `|` : 합집합
- `&` : 교집합
- `-` : 여집합
- `^` : 대칭차집합

#### 연산자 우선 순위

0. `()`을 통한 grouping
1. Slicing
2. Indexing
3. 제곱연산자 `**`
4. 단항연산자 `+`, `-` (음수/양수 부호)
5. 산술연산자 `*`, `/`, `%`
6. 산술연산자 `+`, `-`
7. 비교연산자 `in`, `is`
8. `not`
9. `and`
10. `or` 



## 컨테이터 정리

### 파이썬 프로그램 구성 단위

- 식별자

  - 변수, 함수, 클래스 등 프로그램이 실행되는 동안 다양한 값을 가질 수 있는 이름
  - 예약어는 사용 불가능
    - 파이썬 키워드 (명령어)

- 리터럴(literal)
  - 읽혀지는 대로 쓰여있는 값 그 자체

  ```python
  name = '고길동'
  # name은 식별자 == 변수
  # '고길동'은 리터럴
  ```

  

  

#### 프로그램 구성 단위

- 표현식
  - 새로운 데이터 값을 생성하거나 계산하는 코드 조각
- 문장
  - 특정한 작업을 수행하는 코드 전체를 의미
  - 파이썬이 실행 가능한 최소한의 코드 단위
  - 모든 표현식은 문장이다. (표현식 ⊂ 문장)
- 함수
  - 문장들을 모아서 하나의 기능으로 만듦
- 모듈
- 패키지
- 라이브러리
