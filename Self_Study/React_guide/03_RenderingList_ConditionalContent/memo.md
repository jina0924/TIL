# 렌더링 리스트 및 조건부 Content

[toc]

## 단축평가

### 논리합(`||`)

둘 중 하나만 true이면 true로 평가 => 왼쪽 피연산자가 true이면 바로 true 반환

ex)

```js
"apple" || false;	// "apple"
"apple" || true;	// "apple"
false || "apple"	// "apple"
"apple" || "banana"	// "apple"
```



### 논리곱(`&&`)

둘 다 true여야만 true => 왼쪽 피연산자가 false면 바로 false로 평가됨

ex)

```js
"apple" || false;	// false
"apple" || true;	// true
false || "apple"	// false
"apple" || "banana"	// "banana"
```



## 문자열의 숫자 변환

1. `Number(문자열)`

   ```js
   Number('123')		// 123
   Number('123.4')		// 123.4
   Number('Hello')		// NaN
   ```

2. `+(문자열)`

   자바스크립트에서 문자열과 숫자열의 사칙연산은 숫자로 만들어줌 => 문자열이 숫자열로 변환되는 효과를 가져옴

   ```js
   + ('123')		// 123
   + '123.4'		// 123.4
   + '-123'		// -123
   + 'Hello'		// NaN
   ```

3. `(문자열 * 1)`

   ```js
   '123' * 1		// 123
   '123.4' * 1		// 123.4
   '-123' * 1		// -123
   'Hello' * 1		// NaN
   ```

4. `parseInt(정수 문자열)`,  `parseFloat(실수 문자열)`

   ```js
   parseInt('123')		// 123
   parseFloat('123.4')		// 123.4
   
   parseInt('NaN')		// NaN
   parseFloat('NaN')		// NaN
   
   parseInt('Infinity')		// Infinity
   parseFloat('Infinity')		// Infinity
   
   ParseInt('Hello')		// NaN
   ```

   
