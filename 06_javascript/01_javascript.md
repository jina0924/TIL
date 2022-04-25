# JavaScript 01

[toc]

## Intro

### 자바스크립트의 필요성

- 브라우저 화면을 동적으로 만들기 위함
- 브라우저를 조작할 수 있는 **유일한 언어**



### Browser

**브라우저에서 할 수 있는 일**

- DOM (Document Object Model) 조작
  - 문서(HTML) 조작
  - 문서를 프로그램으로 조작 가능
- BOM (Browser Object Model) 조작
  - navigator, screen, location, frames, history, XHR
- JavaScript Core (ECMAScript)
  - 에크마 스크립트 = 자바스크립트



**DOM 이란?**

- HTML, XML과 같은 문서를 다루기 위한 프로그래밍 인터페이스
- 문서를 구조화하고, 구조화된 구성 요소를 하나의 객체로 취급하여 다루는 논리적 트리 모델



**DOM - 해석**

- 파싱 (Parsing)
  - 구문 분석, 해석
  - 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정



**BOM 이란?**

- Browser Object Model
- 자바스크립트가 브라우저와 소통하기 위한 모델
- 브라우저의 창이나 프레임을 추상화해서 프로그래밍적으로 제어할 수 있도록 제공하는 수단



∴ 브라우저(BOM)과 그 내부의 문서(DOM)를 조작하기 위해 ECMAScript(JS)를 학습



### 세미콜론

- 자바스크립트는 세미콜론을 선택적으로 사용 가능
- 세미콜론이 없으면 ASI에 의해 자동으로 세미콜론이 삽입됨



### 코딩 스타일 가이드

- 합의된 원칙과 일관성 중요
- 코드의 품질에 직결되는 중요한 요소
  - 개발 과정 전체에 영향을 끼침
- (참고) 다양한 자바스크립트 코딩 스타일 가이드
  - 에어비엔비 -> 수업에서 사용하는 가이드
  - 구글
  - standardjs



## 변수

**식별자 정의와 특징**

- 식별자는 변수를 구분할 수 있는 변수명을 말함
- 식별자는 반드시 문자, 달러(`$`) 또는 밑줄로(`_`) 시작
- 클래스명 외에는 모두 소문자로 시작
- 예약어 사용 불가능



**식별자 작성 스타일**

- **카멜 케이스**(camelCase, lower-camel-case)
  - 변수, 객체, 함수에 사용
- **파스칼 케이스**(PascalCase, upper-carmel-case)
  - 클래스, 생성자에 사용
  - 자바스크립트에서 클래스 거의 사용 x
- **대문자 스네이크 케이스**(SNAKE_CASE)
  - 상수에 사용
    - 상수 : 개발자의 의도와 상관없이 변경될 가능성이 없는 값을 의미
  - ex) API_KEY



### 변수 선언 키워드 (let, const)

**let**

- 재할당 할 예정인 변수 선언 시 사용
- 변수 재선언 불가능
- 블록 스코프

**const**

- 재할당 할 예정이 없는 변수 선언 시 사용
  - `=` 사용 불가
  - 가공은 가능함
- 변수 재선언 불가능
- 블록 스코프*



**[참고] 선언, 할당, 초기화**

```javascript
let foo				// 선언
console.log(foo)	// undefined

foo = 11			// 할당
console.log(foo)	// 11

let bar = 0			// 선언 + 할당
console.log(bar)	// 0
```

- 선언
  - 변수를 생성하는 행위 또는 시점

- 할당
  - 선언된 변수에 값을 저장하는 행위 또는 시점

- 초기화
  - 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점




변수 선언 키워드 (**let**, **const**)

- 블록 스코프* (block scope)
  - if, for, 함수 등 **중괄호 내부**를 가리킴
  - 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능
  
  ```js
  let x = 1
  
  if (x===1) {
      let x = 2
      console.log(x)	// 2
  }
  
  console.log(x)		// 1
  ```
  
  

변수 선언 키워드 - **var**

- var
  - var로 선언한 변수는 재선언 및 재할당 모두 가능
  
  - ES6 이전에 변수를 선언할 때 사용되던 키워드
    - ES6 이후부터는 var 대신 const와 let을 사용하는 것을 권장
    
  - **호이스팅** 되는 특정으로 인해 예기치 못한 문제 발생 가능
    
    - hoist : 감아올리다 -> 변수를 선언 이전에 참조할 수 있는 현상
    - 변수를 선언 이전에 참조할 수 있는 현상
    - 변수 선언 이전의 위치에서 접근 시 undefined를 반환
    
    ```js
    console.log(username) // undefined
    var username = '홍길동'
    
    console.log(age) // Uncaught ReferenceError
    const age = 50
    ```
    
    ※ 두 줄씩 한번에 입력해야 원하는 결과값 확인할 수 있음
    
  - 함수 스코프
  
    - 함수의 중괄호 내부를 가리킴
    - 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능



## 데이터 타입

데이터 타입 종류

- 자바스크립트의 모든 값은 특정한 데이터 타입을 가짐
- 크게 원시 타입과 참조 타입으로 분류됨



[참고] 원시 타입과 참조 타입 비교

- 원시 타입 (Primitive type)
  - 객체(objects)가 아닌 기본 타입
  - Number, String, Boolean, undefined, null, Symbol
  - 변수에 해당 타입의 값이 담김
  - 다른 변수에 복사할 때 실제 값이 복사됨
- 참조 타입 (Reference type)
  - 객체 타입의 자료형
  - 변수에 해당 객체의 참조 값이 담김
  - 다른 변수에 복사할 때 참조 값이 복사됨



#### 원시 타입

- 숫자 (Number) 타입

  - 정수, 실수 구분 없는 하나의 숫자 타입
  - 부동소수점 형식을 따름
  - (참고) NaN(Not-A-Number)
    - `'abcd' / 10` -> NaN => 에러x but. 숫자형
    - 계산 불가능한 경우 반환되는 값

  ```js
  const a = 13
  const b = -5
  const c = 3.14
  const d = 2.998e8	// 거듭제곱
  const e = Infinity
  const f = -Infinisty
  const g = NaN		// 산술 연산 불가
  ```

- 문자열 타입
  - 템플릿 리터럴(Template Literal)
    - 따옴표 대신 backtick(``)으로 표현
    - ${ expression } 형태로 표현식 삽입 가능

  ```js
  const firstName = 'Brandan'
  const lastName = 'Eich'
  const fullName = '${firstName} ${lastName}'
  
  console.log(fullName)	// Brandan Eich
  ```
  
  
  
- undefined
  - 변수의 값이 없음을 나타내는 데이터 타입
  - 개발자의 의도가 담기지 x
  - 변수 선언 이후 직접 값을 할당하지 않으면, 자동으로 undefined가 할당됨
  
- null
  - 변수의 값이 없음을 **의도적으로** 표현할 때 사용하는 데이터 타입
  - 자동 생성되지 않음
  - typeof 연산자의 결과는 object
  
- Boolean 타입
  - true 또는 false로 표현(대문자 x)
  - Number
    - Undefined, Null : 항상 거짓
    - 0, -0, NaN : 거짓
    - Object : 항상 참
      - 빈 리스트도 자바스크립트에서는 참



#### 참조 타입

- 함수
- 배열
- 객체



## 연산자

**할당 연산자**

- ++

  ```js
  let num = 100
  num += 1
  101
  num++
  101
  ```



**비교 연산자**

- 문자열은 유니코드 값을 사용하며 표준 사전 순서를 기반으로 비교
  - 알파벳끼리 비교할 경우(유니코드값 비교)
    - 알파벳 순서상 후순위가 더 큼
    - 소문자가 대문자보다 더 큼



**동등 비교 연산자**(==)

- 비교할 때 암묵적 타입 변환을 통해 타입을 일치키신 후 같은 값인지 비교

- 예상치 못한 결과가 발생할 수 있으므로 특별한 경우를 제외하고 사용하지 않음

  ```js
  1 == '1'
  true
  ```

  

**일치 비교 연산자(===)**

- 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
- 엄격한 비교가 이뤄지며 암묵적 타입 변환이 발생하지 않음
- 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별



**논리 연산자**

- 세 가지 논리 연산자
  - and : `&&`
  - or : `||`
  - not : `!`
    - !true-> false
    - !!true -> true
- 단축 평가 지원



**삼항 연산자 (Tenary Operator)**

- 세 개의 피연산자를 사용하여 조건에 따라 **값을 반환**하는 연산자

- 가장 왼쪽의 조건식이 참이면 콜론(`:`) 앞의 값을 사용하고

- 그렇지 않으면 콜론(`:`) 뒤의 값을 사용

  - `?` 앞에 있는 부분이 통째로 하나의 값으로 평가됨
  - 이게 참이면 왼쪽, 아니면 오른쪽

- 삼항 연산자의 결과 값이기 때문에 변수에 할당 가능

- 한 줄에 표기하는 것을 권장

  ```js
  console.log(ture ? 1 : 2) // 1
  console.log(false ? 1 : 2) // 2
  
  const result = Math.PI > 4 ? 'Yes' : 'No'
  cosole.log(result) // No
  ```



## 조건 / 반복

### 조건

**if statement**

- if, else if, else

  - 조건은 소괄호 안에 작성
  - 실행할 코드는 중괄호 안에 작성
  - 블록 스코프 생성
  
  ```js
  const nation = 'Korea'
  
  if (nation === 'Korea') {
      console.log('안녕하세요!')
  } else if (nation === 'France') {
      console.log('Bonjour!')
  } else {
      console.log('Hello!')
  }
  ```
  
  

**switch statement**

- 표현식의 결과값을 이용한 조건문

- 표현식의 결과값과 case문의 오른쪽 값을 비교

- break 및 default문은 [선택적]으로 사용 가능

- break문이 없는 경우 break문을 만나거나 default문을 실행할 때가지 다음 조건문 실행

- 블록 스코프 생성

  ```javascript
  const nation = 'Korea'
  
  switch(nation) {
      case 'Korea': {
          console.log('안녕하세요!')
          break
      }
      case 'France' : {
          console.log('Bonjour!')
          break
      }
      default : {
          console.log('Hello!')
      }
  }
  ```

  - break가 없으면 case 'Korea'가 참이면 밑의 조건 살피지 않고 그냥 다 출력함



### 반복문

- while

  - 조건은 소괄호 안에 작성
  - 실행한 코드는 중괄호 안에 작성

  ```js
  let i = 0
  whiel (i < 5) {
      console.log(i) // 0, 1, 2, 3, 4
      i++
  }
  ```

- for

  - 구버전에서는 여기까지만 지원
  - 세미콜론(`;`)으로 구분되는 세 부분으로 구성
  - **initialization**
    - 최초 반복문 진입 시 1회만 실행되는 부분
  - **condition**
    - 매 반복 시행 전 평가되는 부분
  - **expression**
    - 매 반복 시행 이후 평가되는 부분
  - 블록 스코프 생성

  ```js
  for (let i=0; i<5; i++) {
      console.log(i)		// 0, 1, 2, 3, 4
  }
  ```

- for ... in

  - 주로 객체(object)의 속성(key)을 순회할 때 사용
    - 객체: 클래스의 인스턴스x -> 딕셔너리
  - 배열도 순회 가능하지만 권장하지 않음
  - 실행할 코드는 중괄호 안에 작성
  - 블록 스코프 생성

  ```js
  const capitals = {
      korea: 'seoul',
      france: 'paris',
      USA: 'washington D.C'
  }
  
  for (let capital in capitals) { 
  	console.log(capital)		// korea, france, USA
  }
  ```

- for ... of

  - 반복 가능한(iterable) 객체를 순회하며 값을 꺼낼 때 사용
  - 실행할 코드는 중괄호 안에 작성
  - 블록 스코프 생성

  ```js
  const fruits = ['딸기', '사과', '수박']
  for (let fruit of fruits) {
      colsole.log(fruit)		// 딸기, 사과, 수박
  }
  ```

  - in으로 적는다면 배열의 인덱스가 출력됨

  ```js
  for (const fruit of fruits) {
      console.log(fruit)		// 딸기, 사과, 수박
  }
  ```

  - const는 재할당 안되는데 같은 결과가 나오는 이유
    - {}가 끝나면 스코프 끝남(?)



※ const 먼저 쓸 것

- 나중에 재할당이 필요해지면 let으로 수정할 것



## 함수

- JavaScript에서 함수를 정의하는 방법
  - 함수 선언식
  - 함수 표현식
- (참고) JavaScript의 함수는 **일급 객체**에 해당
  - 일급 객체 : 다음의 조건들을 만족하는 객체를 의미함
    - 변수에 할당 가능
    - 함수의 매개변수로 전달 가능
    - 함수의 반환 값으로 사용 가능



**함수 선언식**

- 함수의 이름과 함께 정의하는 방식

- 3가지 부분으로 구성

  - 함수의 이름 (name)
  - 매개변수 (args)
  - 몸통 (중괄호 내부)

  ```js
  function name(args) {
      //do something
  }
  ```

  ```js
  function add(num1, num2) {
      return num1 + num2
  }
  
  add(1, 2)
  ```



**함수 표현식**

- 함수 표현식* 내에서 정의하는 방식

  - 함수 표현식 : 어떤 하나의 값으로 결정되는 코드의 단위

- 함수의 이름을 생략하고 익명 함수로 정의 가능

  - 익명 함수 : 이름이 없는 함수
  - 익명 함수는 함수 표현식에서만 가능

- 3가지 부분으로 구성

  - 함수의 이름(생략 가능)
  - 매개변수(args)
  - 몸통 (중괄호 내부)

  ```js
  const name = function (args) {
      // do something
  }
  ```

  ```js
  const add = function (num1, num2) {
      return num1 + num2
  }
  
  add(1, 2)
  ```



기본 인자

- 인자 작성 시 `=` 문자 뒤 기본 인자 선언 가능

  ```js
  const greeting = function (name = 'Anonymous') {
      return 'Hi ${name}'
  }
  
  greeting()	// Hi Anonymous
  ```

- 매개변수보다 인자의 개수가 많을 경우

  ```js
  const noArgs = function () {
      return 0
  }
  
  noArgs(1, 2, 3)		// 0
  
  const twoArgs = function (arg1, arg2) {
      return [arg1, arg2]
  }
  
  twoArgs(1, 2, 3)	// [1, 2]
  ```

- 매개변수보다 인자의 개수가 적을 경우

  ```js
  const threeArgs = function (arg1, arg2, arg3) {
      return [arg1, arg2, arg3]
  }
  
  threeArgs()			// [undefined, undefined, undefined]
  threeArgs(1)		// [1, undefined, undefined]
  threeArgs(1, 2)		// [1, 2, undefined]
  ```



**Rest operator**

- rest operator(...)를 사용하면 함수가 정해지지 않은 수의 매개변수를 배열로 받음

  - python의 *args 와 유사
  - 만약 rest poerator로 처리한 매개변수에 인자가 넘어오지 않을 경우에는, 빈 배열로 처리

  ```js
  const restOpr = function (arg1, arg2, ...restArgs) {
      return [arg1, arg2, restArgs]
  }
  
  restArgs(1, 2, 3, 4, 5)		// [1, 2, [3, 4, 5]]
  restArgs(1, 2)				// [1, 2, []]
  ```

  

**Spread operator**

- spread operator(...)를 사용하면 배열 인자를 전개하여 전달 가능

  ```js
  const spreadOpr = function (arg1, arg2, arg3) {
      return arg1 + arg2 + arg3
  }
  
  const numbers = [1, 2, 3]
  spreadOpr(...numbers)		// 6
  ```

  



## 선언식 vs. 표현식

|        | 함수 선언식                      | 함수 표현식                    |
| ------ | -------------------------------- | ------------------------------ |
| 공통점 |                                  |                                |
| 차이점 | 익명 함수 불가능<br />호이스팅 O | 익명 함수 가능<br />호이스팅 X |
| 비고   |                                  | Airbnb Style Guide 권장 방식   |







## Arrow Function







## 문자열 (String)







## 배열 (Arrays)







## 객체 (Objects)







## this 정리



