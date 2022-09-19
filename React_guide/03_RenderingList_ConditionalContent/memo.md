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

