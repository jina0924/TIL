# Basic of React

[toc]

## node.js

브라우저 밖에서 자바스크립트 코드가 실행될 수 있도록 하는 자바스크립트 런타임



## npx

npm의 5.2.0 버전부터 새로 추가된 도구

모듈을 로컬에 저장하지 않고, 매번 최신 버전의 파일만 임시로 불러와 실행시킴

→ 다시 그 파일은 없어지는 방식

- npm : Package Manager(관리)
- npx : Package Runner(실행)



## source

> 개발자도구(F12) -> Sources -> statkc/js -> js파일들

전체 리액트 패키지 도구

- 내가 작성한 소스 코드
- 전체 리액트 라이브러리 소스 코드
- 전체 리액트 돔 라이브러리 소스 코드

브라우저에서 실행되도록 변환된 코드



## React 시작

```bash
$ npm install
$ npm start
```



## JSX

자바스크립트 XML

package.json

```json
{
    ...
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
}
```

- react-dom만 사용하게 됨



## Props



**toLocaleString**()

배열의 요소를 나타내는 문자열을 반환



**getFullYear()**

주어진 날짜의 현지 시간 기준 연도를 반환



**Date() 생성자**

시간의 특정 지점을 나타내는 Date 객체를 플랫폼에 종속되지 않은 형태로 생성

새로운 Date 객체를 생성하는 방법 : `new Date()`

- `new Date()` : 현재 날짜 및 시간
- 인자로 value, dateString, year, monthIndex, day, hours, minutes, seconds 등을 넣을 수 있음
