# Vue 02

[toc]

## SFC (Single File Component)

**Component (컴포넌트)**

- 기본 HTML 엘리먼트를 확장하여 재사용 가능한 코드를 캡슐화 하는데 도움을 줌
- 다시 쓸 수 있는 부품
- Vue 컴포넌트 === Vue 인스턴스



**SFC (Single File Component)**

- `.vue` 확장자를 가진 싱글 파일 컴포넌트를 통해 개발하는 방식
- 하나의 컴포넌트 = `.vue`확장자를 가진 하나의 파일 안에서 작성되는 코드의 결과물
- 화면의 특정 영역에 대한 HTML, CSS, JavaScript 코드를 하나의 파일(`.vue`)에서 관리
- Vue 컴포넌트 === Vue 인스턴스 === `.vue`파일



**Component 예시**

- component를 쪼개서 합침 (like. include)
- 각 기능별로 파일을 나눠서 개발
  - 처음 개발을 준비하는 단계에서 시간 소요가 증가
  - but. 이후 변수 관리가 용이
  - 기능 별로 유지 & 보수 비용 감소



**Vue Compoenet 구조 예시**

- 트리
  - 사이클이 없는 그래프
- 한 화면 안에서도 기능 별로 각기 다른 컴포넌트가 존재
  - 하나의 컴포넌트는 여러 개의 하위 컴포넌트를 가질 수 있음

- Vue 컴포넌트는 const app = new Vue({...}) 의 app을 의미 === Vue 인스턴스
  - 컴포넌트 기반의 개발 !== 파일 단위로 구분되어야 하는 것
  - 단일 `.html` 파일 안에서도 여러 개의 컴포넌트를 만들어 개발 가능



## Vue CLI

**Node.js**

- 자바스크립트를 브라우저가 아닌 환경에서도 구동할 수 있도록 하는 자바스크립트 런타임 환경
  - 브라우저 밖을 벗어날 수 없던 자바스크립트 언어의 태생적 한계 해결

- Chrome V8 엔진을 제공 -> 여러 OS 환경에서 실행할 수 있는 환경 제공
- 단순히 브라우저만 조작할 수 있던 자바스크립트를 SSR 아키텍처에서도 사용할 수 있도록 함



**NPM (Node Package Manage)**

- 자바스크립트 언어를 위한 패키지 관리자
  - Python  - pip와 같은 관계
- vue라는 말로 명령 시행 가능(django-admin같은 방식)



**Vue CLI Quick Start**

- 설치

  ```bash
  $ npm install -g @vue/cli
  ```

  - 프로젝트마다 분리시키는게 기본 설정(파이썬의 venv처럼)
  - 글로벌로 설치하고 싶다면 `-g`
    - 설치 문서에 `-g`라고 적혀있는 것만 `-g` 쓸 것 (자의적으로 판단 x)

- 버전 확인

  ```bash
  $ vue --version
  ```

- 프로젝트 생성

  ```bash
  $ vue create my-first-app
  # vue2로 선택
  ```

  - vscode terminal에서 할 것

- Vue 버전 선택 (Vue2)

- 프로젝트 생성 성공

  ```bash
  🎉  Successfully created project my-first-app.
  👉  Get started with the following commands:
  
  # 프로젝트 디렉토리 이동
   $ cd my-first-app
   # 서버 실행
   $ npm run serve
  ```

  - Ctrl + C로 끌 수 있음



### Babel & Webpack

**Babel**

- JavaScript compiler
- 자바스크립트의 ECMAScript 2015+ 코드를 이전 버전으로 번역/변환해주는 도구
- 원시 코드(최신 버전)을 목적 코드(구 버전)으로 옮기는 번역기
  - 개발자가 특정 브라우저에서 내 코드가 동작하지 않는지에 대해 고민x




**Webpack**

- static module bundler
- 모듈 간의 의존성 문제를 해결하기 위한 도구
- 프로젝트에 필요한 모든 모듈을 매핑하고 내부적으로 종속성 그래프를 빌드함
- **Module**
  - 모듈은 단지 파일 하나를 의미 (ex. js 파일 하나 === 모듈 하나)
  - 라이브러리를 만들어 모듈을 언제든지 불러오거나 코드를 모듈 단위로 작성하는 등의 다양한 시도가 이루어짐
  - 여러 모듈 시스템
    - ESM (ECMA Script Module) - 현재 표준
  - Module 의존성 문제
    - 모듈의 수가 많아지고 라이브러리 혹은 모듈 간의 의존성(연결성)이 깊어지면서 특정한 곳에서 발생한 문제가 어떤 모듈 간의 문제인지 파악하기 어려움
    - Webpack은 이 모듈 간의 의존성 문제를 해결하기 위해 등장
- **Bundler**
  - 모듈 의존성 문제를 해결해주는 작업 = Bundling
  - Webpack은 다양한 Bundler 중 하나
  - 여러 모듈을 하나로 묶어주고 묶인 파일은 하나(혹은 여러 개)로 합쳐짐
  - Bundling된 결과물은 더 이상 순서에 영향을 받지 않고 동작하게 됨




- Vue CLI는 이러한 Babel, Webpack에 대한 초기 설정이 자동으로 되어 있음



**정리**

- Node.js
  - JavaScript Runtime Environment
  - JavaScript를 브라우저 밖에서 실행할 수 있는 새로운 환경

- Babel
  - Compiler

- Webpack
  - Module Bundler




**Vue 프로젝트 구조**

- node_modules (파이썬의 venv)

  - git에 올리면 안됨
  - mode.js 환경의 여러 의존성 모듈

- public / index.html

  - Vue앱의 뼈대가 되는 파일
  - 실제 제공되는 단일 html 파일

- 작업은 거의다 src에서

- src/assets

  - webpack에 의해 빌드 된 정적 파일

- src/components

  - 잔잔바리 기능들
  - 하위 컴포넌트들 위치

- src/App.vue

  - canvas 역할
  - 최상위 컴포넌트

- src/main.js

  - 이 스크립트로 인해 나머지 스크립트가 연관됨
  - 실제 단일 파일에서 DOM과 data를 연결 했던 것과 동일한 작업이 이루어지는 곳
  - Vue 전역에서 활용 할 모듈을 등록할 수 있는 파일

  ```js
  new Vue({
    render: h => h(App),
  }).$mount('#app')	// el: '#app'과 같음

- package.json / package-lock.jsoin
  - requirements.txt와 같은 역할
  - freeze필요 x
  - package.json
    - 프로젝트의 종속성 목록과 지원되는 브라우저에 대한 구성 옵션이 포함
  - package-lock.json
    - node_modules에 설치되는 모듈과 관련된 모든 의존성을 설정 및 관리
    - 팀원 및 배포 환경에서 정확히 동일한 종속성을 설치하도록 보장하는 표현
    - 사용할 패키지의 버전을 고정
    - 개발 과정 간의 의존성 패키지 충돌 방지



## Pass props & Emit event

컴포넌트 작성

- 부모는 자식에게 데이터를 전달(Pass props)
- 자식은 자신에게 일어난 일을 부모에게 알림(Emit event `$emit`)
- props는 아래로, events는 위로
- 부모는 props를 통해 자식에게 '데이터'를 전달
- 자식은 events를 통해 부모에게 '메시지'를 보냄



컴포넌트 구조

1. 템플릿

   - 마크업
   - HTML의 body 부분

2. 스크립트

   - 자바스크립트가 작성되는 곳
   - 컴포넌트 정보, 데이터, 메서드 등 vue 인스턴스를 구성하는 대부분이 작성 됨

3. 스타일

   - CSS

   ```vue
   <template></template>
   <script></script>
   <style></style>
   ```



컴포넌트 등록 3단계

- vue + enter 하면 자동으로 기본틀 작성(`! + tap`과 같은 역할)
  - vetur가 해줌

1. 불러오기 (import)
2. 등록하기 (register)
3. 보여주기 (print)



**Props**

- 부모(상위) 컴포넌트의 정보를 전달하기 위한 사용자 지정 특성
- 자식(하위)컴포넌트는 props 옵션을 사용하여 수신하는 props를 명시적으로 선언해야 함

- 주의
  - 모든 컴포넌트 인스턴스에는 자체 격리된 범위가 있음
  - 즉, 자식 컴포넌트의 템플릿에서 상위 데이터를 직접 참조할 수 없음



**Static Props 작성**

- 자식 컴포넌트(About.vue)에 보낼 prop 데이터 선언

- `prop-data-name="value"`

  ```vue
  <template>
  	<div id="app">
  		<img alt="Vue logo" src="./assets/logo.png">
          <about my-message="This is prop data"></about>
      </div>
  </template>
  ```

- 수신할 prop 데이터를 명시적으로 선언 후 사용

  ```vue
  // TheAbout.vue
  <template>
  <!-- template안에는 반드시 하나의 Element만 있어야 한다 -->
  <!-- template밑에 div쓰고 시작할 것 -->
  <div>
    <h1>{{ myMessage }}</h1>
    <p>아하 div는 하나구만</p>
  </div>
  </template>
  
  <script>
  export default {
    name: 'TheAbout',   // 컴포넌트 코드 확인용(?)
    props: {
      myMessage: String,  // 타입 적어줘야 함
    }
  }
  </script>
  ```

  

Dynamic Props 작성

- v-bind directive를 사용해 부모의 데이터의 props를 동적으로 바인딩

- 부모에서 데이터가 업데이트 될 때마다 자식 데이터로도 전달 됨

  ```vue
  // App.vue
  <template>
    <div id="app">
      <img alt="Vue logo" src="./assets/logo.png">
      <!-- 3. 보여주기 (print) -->
      <!-- 카멜 케이스 -->
      <!-- <TheAbout my-message="CamelCase"/> -->
      <TheAbout :my-message="parentData"/>
      <!-- 케밥 케이스 -->
      <the-about my-message="kebab-case"></the-about>
    </div>
  </template>
  
  <script>
  // 1. 불러오기 (import)
  import TheAbout from './components/TheAbout.vue'
  // import는 as와 같은 역할. 무슨 이름으로 부를지 설정
  export default {
    name: 'App',
    // 2. 등록하기 (register)
    components: {
      TheAbout,
    },
    data: function () {
      return {
        parentData: 'This is parent data to child component'
      }
    },
  ```

- 수신할 prop 데이터를 명시적으로 선언 후 사용

  

**Props 이름 컨벤션**

- during declaration (선언 시)
  - camelCase
- in template (HTML)
  - kebab-case



**※ 컴포넌트의 'data'는 반드시 함수여야 함**

- 기본적으로 각 인스턴스는 모두 같은 data 객체를 공유하므로 새로운 data 객체를 반환(return)해야 함

  ```vue
    data: function () {
      return {
        parentData: 'This is parent data to child component'
      }
    },
  ```



Props시 숫자 전달하려면

- JavaScript 표현식으로 평가되도록 v-bind를 사용해야 함



**Emit event**

- Listening to Child Components Events
- `$emit(eventName)`
  - 현재 인스턴스에서 이벤트를 트리거
  - 추가 인자는 리스터의 콜백 함수로 전달

- 부모 컴포넌트는 자식 컴포넌트가 사용되는 템플릿에서 v-on을 사용하여 자식 컴포넌트가 보낸 이벤트를 청취 (v-on을 이요한 사용자 지정 이벤트)



Emit event 작성

- 현재 인스턴스에서 $emit 인스턴스 메서드를 사용해 child-input-change 이벤트를 트리거

  ```vue
  <script>
  export default {
    ...
    methods: {
      childInputChange: function () {
        console.log('Child!!', this.childInputData)
        this.$emit('child-input-change', this.childInputData)  // 바로 위에만 boss 이벤트가 발생함. 인자 여러개 가능 but. 비추천 -> 묶어서 보낼 것(context처럼)
      }
    },
  }
  </script>
  ```

- 부모 컴포넌트

  ```vue
  <template>
    <div id="app">
      <img alt="Vue logo" src="./assets/logo.png">
      <the-about my-message="kebab-case" 
      @child-input-change="parentGetChange"
      ></the-about>
    </div>
  </template>
  ```

  

**event 이름 컨벤션**

- 이벤트는 자동 대소문자 변환을 제공하지 않음
- 항상 kebab-case를 사용하는 것을 권장



## Vue Router

- url이 없으니까 라우트(route)에 컴포넌트를 매핑한 후, 어떤 주소에서 렌더링할 지 알려줌
- 컴포넌트와 주소를 매핑
- url을 통한 하이퍼링크의 이동x 그런 척만 함



**Vue Router 시작하기**

1. 프로젝트 생성 및 이동

   ```bash
   $ vue create my-router-app
   $ cd my-router-app
   ```

2. Vue Router plugin 설치 (Vue CLI 환경)

   ```bash
   $ vue add router
   ```

3. commit 여부 (y)

4. History mode 사용 여부 (y)



**Vue Router로 인한 변화**

1. App.vue 코드

   ```vue
   <template>
     <div id="app">
       <nav>
         <router-link :to="{ name: 'home' }">Home</router-link> |
         <router-link :to="{ name: 'about' }">About</router-link>
       </nav>
       <router-view/>
     </div>
   </template>
   ```

   - router-link가 a태그 대신함

2. router/index.js 생성

3. views 디렉토리 생성



**index.js**

- 라우트에 관련된 정보 및 설정이 작성되는 곳

  ```js
  const routes = [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView
    },
    {
      path: '/user/:userId',
      name: 'profile',
      component: UserProfile
    }
  ]
  ```

  

**Vue Router - "router-link"**

- `<router-link>`
  - 목표 경로는 'to' prop으로 지정됨
  - a태그이지만 이벤트 제거된 형태




**Vue Router - "router-view"**

- `<router-view>`
- History mode
  - url 바뀌는 척



1. Named Routes
   - 바인드가 있어야지만 객체로 동작함
2. 프로그래밍 방식 네비게이션
   - 



## Youtube Project

