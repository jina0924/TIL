# Redux

[toc]

## What is Redux

> A state management system for cross=component or app-wide state

State

1. Local State
   - 데이터가 변경되어 하나의 컴포넌트에 속하는 UI에 영향을 미치는 상태
   - `useState`로 컴포넌트 안에서 로컬 상태 관리
2. Cross-Component State
   - 다수의 컴포넌트에 영향을 주는 상태
   - ex)  모달 트리거  
   - prop 체인을 구축해야 함(prop drilling) 
3. App-Wide State
   - 모든 컴포넌트에 영향을 주는 상태
   - ex) 사용자 인증 
   - prop drilling

=> 2, 3을 해결하기 위해 Redux 사용



## React Context - Potential Disadvantages

1. Complex Setup / Management 
2. Performance



## Core Redux Concepts

- 컴포넌트가 redux의 데이터를 `구독`함
- Reducer Function : Mutates(=changes) Store Data
  - 데이터 업데이트 담당
- Action



## Redux 설치

```bash
$ npm install redux react-redux
```

- react-redux : 리액트 앱과 리덕스 스토어와 리듀서에 간단히 접속
