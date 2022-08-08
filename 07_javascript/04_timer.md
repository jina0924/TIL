# 타이머 함수

[toc]

## setTimeout

```js
setTimeout(function[, delay, arg1, arg2, ...])
setTimeout(code[, delay])
```

- function : 타이머가 만료된 후 실행할 함수
- code : 함수 대신 문자열을 지정하는 대체 구문
  - 타이머가 만료될 때 코드로 컴파일 후 실행함
  - 사용을 권장하지 않음
- delay (option) : 주어진 함수 또는 코드를 실행하기 전에 기다릴 단위 시간(ms)
- arg1, ... (option) : 함수에 전달한 추가 매개변수



```js
var timeoutID = setTimeout(function[, delay, arg1, arg2, ...]);
```

- timeoutID
  - 양의 정수
  - `setTimeout()`이 생성한 타이머를 식별할 때 사용
    - ex) `clearTimeout()`에 전달하여 타이머 취소함





## clear Timeout

```js
clearTimeout(timeoutID)
```

- `setTimeout()`이 반환한 timeoutID를 이용하여 예약된 타이머를 취소할 수 있음





## setInterval

```js
setInterval(code)
setInterval(code, delay)

setInterval(func)
setInterval(func, delay)
setInterval(func, delay, arg0)
setInterval(func, delay, arg0, arg1)
setInterval(func, delay, arg0, arg1, /* … ,*/ argN)
```

- func : 주어진 지연 시간마다 계속해서 수행할 함수
- delay : 주어진 함수 또는 코드를 실행하기 전에 기다릴 단위 시간(ms)



```js
var intervalID = setInterval(func)
```

- intervalID
  - 양의 정수
  - `setInterval()`이 생성한 타이머를 식별할 때 사용
    - ex) `clearInterval()`에 전달하여 타이머 취소함





## clearInterval

```js
clearInterval(intervalID)
```

`setInterval()`이 반환한 intervalID를 이용하여 예약된 타이머를 취소할 수 있음