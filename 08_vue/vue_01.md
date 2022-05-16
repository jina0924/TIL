# Vue 01

[toc]

데이터 변경 인지 -> 선택 -> 변경 의 과정을 줄이기 위해 Vue, React 등이 나옴

Vue, React 거의 비슷하므로 하나 배워두면 다른데 적용하기 쉬움(?)

장고 + 뷰 는 잘 안씀

drf + 뷰 => 현업에서 많이 씀

렌더링 : 그림



## Intro

**Front-End Development**

- HTML, CSS 그리고 JavaScript를 활용해서 데이터를 볼 수 있게 만들어줌
  - 이 작업을 통해 사용자는 데이터와 상호작용 할 수 있음
- 대표적인 프론트엔드 프레임워크
  - Vue.js, React, Angular



**Vue.js**

- 사용자 인터페이스를 만들기 위한 progressive(점진적인, not 진보적인) 자바스크립트 프레임워크
  - Django - 다른 프레임워크랑 같이 쓰기 어려움. 풀세트
  - progressive - 다른 프레임워크와 같이 쓸 수 있음. 장고랑 같이 or 뷰만 가지고 만들 수 있음
  - react는 대규모 개발에 유용함 why? 분야를 나눠둠(??). 분업화 가능

- 현대적인 tool과 다양한 라이브러리를 통해 SPA(Single Page Application)를 완벽하게 지원



**SPA**

- Single Page Application (단일 페이지 애플리케이션)
  - HTML 한 장만 감
- 현재 페이지를 동적으로 렌더링함으로써 사용자와 소통하는 웹 애플리케이션
- 단일 페이지로 구성되며 서버로부터 최초에만 페이지를 다운로드하고, 이후에는 동적으로 DOM을 구성
  - 처음 페이지를 받은 이후부터는 필요한 부분만 동적으로 다시 작성함

- 연속되는 페이지 간의 사용자 경험(UX)을 향상
- 동작 원리의 일부가 CSR(Client Side Rendering)의 구조를 따름
- 초기 팝업이 다소 느림



**SPA 등장 배경**

- 과거 웹 사이트들은 요청에 따라 매번 새로운 페이지를 응답하는 방식
  - 기존에 장고로 만든 페이지들
- 스마트폰이 등장하면서 모바일 최적화의 필요성이 대두됨



**CSR**

- Client Side Rendering
- SPA가 사용하는 렌더링 방식
- 처음엔 뼈대만 받고 브라우저에서 동적으로 DOM을 그림
  - 뼈대 : HTML, CSS, JS 등 데이터를 제외한 각종 리소스

- 장점
  1. 서버와 클라이언트 간 트래픽 감소
  2. 사용자 경험 (UX) 향상
- 단점
  1. SSR에 비해 전체 페이지 최종 렌더링 시점이 느림
  2. SEO(검색 엔진 최적화)에 어려움이 있음 (최초 문서에 데이터 마크업이 없기 때문)
     - 크롤러는 마크업만 봄(?)
     - 데이터가 로드할 때 까지 기다리지 않으므로 검색에 잘 걸리지 않음

**SSR**

- Server Side Rendering
- 장고에서 html 만들던 방식
- 서버에서 클라이언트에게 보여줄 페이지를 모두 구성하여 전달하는 방식
- 완성된 html 넘김
- 장점
  1. 초기 구동 속도 빠름
  1. SEO에 적합
- 단점
  - 모든 요청마다 새로운 페이지를 구성하여 전달
    - 상대적으로 트래픽이 많아 서버의 부담이 클 수 있음




**SSR & CSF**

- 두 방식의 차이는 최종 HTML 생성 주체가 누구인가에 따라 결정
- 특정 요소(좋아요/팔로우)만 JS(AJAX & DOM조작)를 활용(CSR)



**[참고] SEO**

> 면접에서 종종 물어봄

- Search Enging Optimazation (검색 엔진 최적화)
- 웹 페이지 검색엔진이 자료를 수집하고 순위를 매기는 방식에 맞게 웹 페이지를 구성해서 검색 결과의 상위에 노출될 수 있도록 하는 작업
- 인터넷 마케팅 방법 중 하나
- 구글 등장 이후 → 컨텐츠의 신뢰도를 파악하는 기초 지표로 사용됨
  - 다른 웹 사이트에서 얼마나 인용되었나를 반영



## Why Vue.js?

명령형 프로그래밍 - 5/3 workshop(& practice)에서 작성한 코드

- Vanilla JS
  - 모든 요소를 선택해서 이벤트를 등록하고 값을 변경해야 함

- Vue.js
  - DOM과 Data가 연결되어 있음
  - Data를 변경하면 이에 연결된 DOM은 알아서 변경
  - 우리가 신경 써야 할 것은 오직 Data에 대한 관리 (Developer Exp 향상 = DX)



CDN : 서버에서 가져다 씀. 분산형으로 처리되어 있어서 가까운 서버에서 가져옴

실제로 배포할 때는 CDN이 느린 편 -> 파일을 받아서 쓰는게 빠름



## Concepts of Vue.js

### MVVM Pattern

- 구성 요소

  1. Model

     - Vue에서 Model은 **JavaScript Object**

     - Object === {key: value}
     - Model은 Vue Instance 내부에서 **data**라는 이름으로 존재
     - data가 바뀌면 View(DOM)가 반응

  2. View

     - Vue에서 View는 **DOM(HTML)**
     - data의 변화에 따라서 바뀌는 대상

  3. View Model

     - Vue에서 ViewModel은 모든 **Vue Instance**
     - View와 Model 사이에서 data와 DOM에 관련된 모든 일을 처리
     - DOm과 Data의 중개자



## Quick Start

https://kr.vuejs.org/v2/guide/installation.html



Vue.js 코드 작성 순서

- Data가 변화하면 DOM이 변경
  1. Data 로직 작성
  2. DOM 작성



- CDN 작성

  ```js
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  ```



- 선언적 렌더링

  ```html
    <h2>선언적 렌더링</h2>
    <div id="app1">
      {{ message }}
    </div>
  ```

  ```js
      const app = new Vue({   // VM
        el: '#app1',
        data: {
          message: '안녕하세요 Vue'   // Model
        }
      })
  ```



- Element 속성 바인딩

  ```html
    <h2>Element 속성 바인딩</h2>
      <div id="app2">
        <span v-bind:title="message">
          내 위에 잠시 마우스를 올리면 동적으로 바인딩 된 title을 볼 수 있다?!
        </span>
      </div>
  ```

  ```js
      const app2 = new Vue({
        el: '#app2',
        data: {
          message: `이 메시지는 ${new Date()}에 로드됨!`
        }
      })
  ```



- 조건문

  ```html
    <h2>조건</h2>
      <div id="app3">
        <p v-if="seen">보인다</p>
      </div>
  ```

  ```js
        const app3 = new Vue({
          el: '#app3',
          data: {
            seen: false,
          }
        })
  ```



- 반복문

  ```html
    <h2>반복</h2>
      <div id="app4">
        <ol>
          <li v-for="todo in todos">
            {{ todo.text }}
          </li>
        </ol>
      </div>
  ```

  ```js
      const app4 = new Vue({
        el: '#app4',
        data: {
          todos: [
            { text: 'js 복습'},
            { text: 'vew 배우기'},
            { text: '멋진거 만든대'},
          ]
        }
      })
  ```



- 사용자 입력 핸들링

  ```html
    <h2>사용자 입력 핸들링</h2>
      <div id="app5">
        <p>{{ message }}</p>
        <input v-model="message" type="text">
        <button v-on:click="reverseMessage">로꾸꺼</button>
      </div>
  ```

  ```js
      const app5 = new Vue({
        el: '#app5',
        data: {
          message: '안녕하세요'
        },
        methods: {
          reverseMessage: function () {
            this.message = this.message.split('').reverse().join('')
          }
        }
      })
  ```

  



## Basic Syntax

### Vue instance

- 모든 Vue 앱은 Vue 함수로 새 인스턴스를 만드는 것부터 시작

- Vue 인스턴스를 생성할 때 Options (`{}`) 객체를 전달해야 함
- 여러 Options들을 사용하여 원하는 동작을 구현
- Vue Instance === Vue Component



**Options/DOM - 'el'**

- Vue 인스턴스에 연결(마운트)할 기존 DOM요소

- CSS 선택자 문자열 or HTML Element로 작성

- new를 이용한 인스턴스 생성 때만 사용

  ```js
      const app = new Vue({
        el: '#app',
      })
  ```

  



**Options/Data- 'data'**

- Vue 인스턴스의 데이터 객체

- Vue 인스턴스의 상태 데이터를 정의하는 곳

- Vue template에서 interpolation을 통해 접근 가능

- v-bind, v-on과 같은 directive에서도 사용 가능

- Vue 객체 내 다른 함수에서 this 키워드를 통해 접근 가능

  ```js
      const app = new Vue({
        el: '#app',
        data: {
          message: '안녕하세요'
        })
  ```



**Options/Data- 'methods'**

- Vue 인스턴스에 추가할 메서드

- Vue template에서 interpolation을 통해 접근 가능

- v-on과 같은 directive에서도 사용 가능

- Vue 객체 내 다른 함수에서 this 키워드를 통해 접근 가능

- **주의**
  
  - 화살표 함수를 메서드를 정의하는데 사용하면 안 됨
  - 화살표 함수가 부모 컨텍스트를 바인딩하기 때문에, 'this'는 Vue 인스턴스가 아님(window를 가리키게 됨)
  
  ```js
      const app = new Vue({
        el: '#app',
        data: {
          message: '안녕하세요'
        },
        methods: {
          greeting: function () {
            const newMessage = this.message + '!!!'
            console.log(newMessage)
            return newMessage
          }
        }
      })
  ```



**'this' keyword in vue.js**

- Vue 함수 객체 내에서 vue 인스턴스를 가리킴



## Template Syntax

- 렌더링된 DOM을 기본 Vue 인스턴스의 데이터에 선언적으로 바인딩할 수 있는 HTML 기반 템플릿 구문 사용



### Interpolation (보간법)

> 중괄호 두 개 씀

1. Text

   - `<span>메시지: {{ message }}</span>`

2. Raw HTML

   - `<span v-html="rawHtml"></span>`

3. Attributes

   - `<div v-bind: id="dynamicId"></div>`

4. JS 표현식

   - `{{ number + 1 }}`
   - `{{ message.split('').reverse().join('') }}`

   

### Directive (디렉티브)

- `v-` 접두사가 있는 특수 속성

- 속성 값은 단일 JS 표현식이 됨 (v-for는 예외)
- 표현식의 값이 변경될 때 반응적으로 DOM에 적용하는 역할을 함



- 전달인자 (Arguments)

  - `:` (콜론)을 통해 전달인자를 받을 수 있음

  ```html
      <img v-bind:src="imageSrc" :alt="altMsg">
      <img :src="imageSrc" :alt="altMsg">
  ```

- 수식어 (Modifiers)

  - `.` (점)으로 표시되는 특수 접미사
  - directive를 특별한 방법으로 바인딩 해야함을 나타냄

  ```html
  <form v-on:submit.prevent="onSubmit">...</form>
  ```

  

**v-text**

- element의 textContent를 업데이트

  ```html
    <div id="app">
      <p>{{ message }}</p>
      <!-- 위와 같음 -->
      <p v-text="message"></p>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      const app = new Vue({
        el: '#app',
        data: {
          message: 'Hello'
        }
      })
  ```



**v-html**

- element의 innerHTML을 업데이터
  - XSS 공격에 취약할 수 있음
- 임의의 사용자로부터 입력 받은 내용은 v-html에 절대 사용 금지



**v-show**

- 조건부 렌더링 중 하나

- 요소는 항상 렌더링됨(DOM에는 있음)

  - 문서에는 있지만 안보이게 처리 가능

- element에 display CSS 속성을 토글하는 것

  ```html
    <div id="app">
      <p v-show="isTrue">TRUE</p>
      <!-- 문서에 있지만 안보이게 처리함 -->
      <p v-show="isFalse">FALSE</p>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      const app = new Vue({
        el: '#app',
        data: {
          isTrue: true,
          isFalse: false,
        }
      })
    </script>
  ```

  

**v-if, v-else-if, v-else**

- 조건부 렌더링

- 조건에 따라 요소를 렌더링

- directive의 표현식이 true일 때만 렌더링

- v-show와의 차이점 : v-if는 문서에서도 사라짐

  - `<!---->`표시 남음

  ```html
    <div id="app">
      <!-- 아예 없으면 없다는 주석 달림 -->
      <p v-if="seen">seen is True</p>
      <!-- v-show와 차이점: v-if는 화면에서 아예 사라짐 -->
      <p v-if="myType === 'A'">A</p>
      <p v-else-if="myType === 'B'">B</p>
      <p v-else-if="myType === 'C'">C</p>
      <p v-else>NOT A/B/C</p>
    </div>
  
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      const app = new Vue({
        el: '#app',
        data: {
          seen: false,
          myType: 'A',
        }
      })
    </script>
  ```

  

**v-show와 v-if**

- v-show (Expensive initial load, cheep toggle)
  - CSS display 속성을 hidden으로 만들어 토글
  - 자주 변경되는 요소라면 한 번 렌더링 된 이후부터는 보여지는 여부만 판단하면 되므로 토글 비용이 적음
- v-if (Cheap initial load, expensive toggle)
  - 전달인자가 false인 경우 렌더링 x
  - 자주 변경되는 요소의 경우 다시 렌더링 해야하므로 비용 증가할 수 있음



**v-for**

- 원본 데이터를 기반으로 엘리번트 또는 템플릿 블록을 여러 번 렌더링

- `item in items` 구문 사용

- item 위치의 변수를 각 요소에서 사용할 수 있음

  - 객체의 경우는 key

- v-for 사용 시 반드시 key 속성을 각 요소에 작성

  - why? 안그럼 꼬임

- v-if와 함께 사용하는 경우 v-for가 우선순위 더 높음

  - but, 동시에 사용 지양할 것

  ```html
    <div id="app">
      <h2>String</h2>
      <div v-for="char in myStr">
        {{ char }}
      </div>
      <h2>Array</h2>
      <div v-for="fruit in fruits">
        {{ fruit }}
      </div>
      <!-- v-for할 때는 무조건 key 있어야 함
      key는 무조건 독립적이어야 함 -->
      <div v-for="(fruit, idx) in fruits" :key="idx">
        {{ idx }} => {{ fruit }}
      </div>
  
      <div v-for="todo in todos" :key="`todo-${todo.id}`">
        <p>{{ todo.title }} => {{ todo.completed }}</p>
      </div>
  
      <h2>Object</h2>
      <div v-for="(value, key) in myObj">
        {{ key }} => {{ value }}
      </div>
    </div>
  
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      const app = new Vue({
        el: '#app',
        data: {
          myStr: 'Hello World!',
          fruits: ['apple', 'banana', 'cacao'],
          todos: [
            { id: 1, title: 'todo1', completed: true},
            { id: 2, title: 'todo2', completed: false},
            { id: 3, title: 'todo3', completed: true},
          ],
          myObj: {
            name: 'kim',
            age: 150,
          }
        }
      })
    </script>
  ```

  

**v-on**

- 엘리번트에 이벤트 리스너를 연결

- 이벤트 유형은 전달 인자로 표시함

- 특정 이벤트가 발생했을 때, 주어진 코드가 실행됨

- 약어

  - `@`
  - `v-on:click` === `@click`

  ```html
    <div id="app">
      <!-- 메서드 핸들러 -->
      <!-- ele,addEventListener(eventName, cbFunction) -->
      <button v-on:click="alertHello">Button</button>
      <button @click="alertHello">Button</button>
      <!-- 기본 동작 방지 -->
      <!-- event.preventDefault -->
      <form action="" @submit.prevent="alertHello">
        <button>GOGO</button>
      </form>
      <!-- 이벤트를 단순히 막고 싶다면
      <form action="" @submit.prevent> -->
  
      <!-- 키 별칭을 이용한 키 입력 수식어 -->
      <!-- 모든 키 입력 추적 -->
      <input type="text" @keyup="log">
      <!-- 엔터 입력만 추적 -->
      <input type="text" @keyup.enter="log">
      <!-- cb 함수에서 특수문법 ()
      log를 실행할건데, 1번 인자로 'asdf'를 넘기고 싶다????? -->
      <input type="text" @keyup.enter="log('asdf')">
  
      <p>{{ message }}</p>
      <button @click="changeMessage">change message</button>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      const app = new Vue({
        el: '#app',
        // 값
        data: {
          message: 'Hello Vue',
        },
        // 행동(함수)
        methods: {
          alertHello: function () {
            alert('hello')
          },
          log: function (event) {
            console.log(event)
          },
          changeMessage() {
            this.message = 'New message!!'
          }
        }
      })
    </script>
  ```

  

**v-bind**

- HTML 요소의 속성에 Vue의 상태 데이터를 값으로 할당

- Object 형태로 사용하면 value가 true인 key가 class 바인딩 값으로 할당

- 약어

  - `:`
  - `v-bind:href` === `:href`

  ```html
    <style>
      .active {
        color: red;
      }
  
      .my-background-color {
        background-color: yellow;
      }
    </style>
  </head>
  <body>
    <div id="app">
      <!-- 속성 바인딩 -->
      <img v-bind:src="imageSrc" :alt="altMsg">
      <img :src="imageSrc" :alt="altMsg">
  
      <hr>
  
      <!-- 클래스 바인딩 -->
      <!-- isRed가 true이면 active 클래스 토글 -->
      <div :class="{ active: isRed }">
        클래스 바인딩
      </div>
  	
      <!-- 삼항 연산자도 가능 -->
      <h3 :class="[activeRed, myBackground]">
        Hello Vue
      </h3>
  
      <hr>
  
      <!-- 스타일 바인딩 -->
      <p :style="{ fontSize: fontSize + 'px' }">
        this is paragraph
      </p>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      const app = new Vue({
        el: '#app',
        data: {
          fontSize: 16,
          altMsg: 'This is image',
          imageSrc: 'https://picsum.photos/200/300',
          isRed: true,
          activeRed: 'active',
          myBackground: 'my-background-color',
        }
      })
    </script>
  </body>
  ```

  - 조건부 토글 방법 - 삼항 연산자
    - `<div v-bind:class="[isActive ? activeClass : '', errorClass]"></div>`
  - 조건부 토글 방법 - 객체 구문
    - `<div v-bind:class="[{ active: isActive }, errorClass]"></div>`



**v-model**

- HTML form 요소의 값과 data를 양방향 바인딩

  ```html
    <div id="app">
      <!-- input의 변화가 data를 바꾸지만 data의 변화가 input을 바꾸진 x -->
      <h2>Input -> Data 단방향</h2>
      <p>{{ msg1 }}</p>
      <!-- 모든 변화를 다 감지하는 이벤트: input -->
      <input type="text" @input="onInputChange">
      <hr>
      <h2>Input <-> Data 양방향</h2>
      <p>{{ msg2 }}</p>
      <input type="text" v-model="msg2">
      <hr>
      췍<input id="box" type="checkbox" v-model="checked">
      <label for="box">{{ checked }}</label>
    </div>
  
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      const app = new Vue ({
        el: '#app',
        data: {
          msg1: '111',
          msg2: '222',
          checked: true,
        },
        methods: {
          onInputChange (event) {
            this.msg1 = event.target.value
          }
        },
      })
    </script>
  ```

- 수식어
  - `.lazy`
    - input 대신 change 이벤트 이후에 동기화
  - `.number`
    - 문자열을 숫자로 변경
  - `.trim`
    - 입력에 대한 trim을 진행



**Options/Data - 'computed'**

- 데이터를 기반으로 하는 계산된 **속성**

- 함수의 형태로 정의 but, 함수가 아닌 함수의 반환 값이 바인딩 됨

- 종속된 데이터에 따라 저장(캐싱)됨

- 종속된 데이터가 변경될 때만 함수를 실행

- 반드시 반환 값이 있어야 함

  ```html
    <div id="app">
      <p>{{ r }}</p>
      <p>{{ area }}</p>
      <p>{{ perim }}</p>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      const app = new Vue({
        el: '#app',
        data: {
          r: 2,
        },
        computed: {
          area: function () {
            return this.r ** 2 * 3.14
          },
          perim: function () {
            return this.r * 2 * 3.14
          }
        }
      })
    </script>



**computed vs. method**

- computed
  - return 하는 값
  - 변수처럼 `()`없이 사용
  - 저장해뒀다가 씀 (특별한 일 없으면 바뀌지 않음)


- method
  - `()`뒤에 반드시 붙음
  - 호출하면 렌더링을 다시 할 때마다 항상 함수를 실행

- vue객체가 바구니라면 computed는 바구니 안에 있는 것만 트래킹 가능

- Math.random()은 vue 밖에 있는 데이터 -> 트래킹 불가능

- ※ 객체 = 정보(변수) + 행동(함수 -> 메서드)

  ※ this : 객체 자기 자신을 의미함

  ```html
    <div id="app">
      <div>
        <input type="text" v-model="message">
      </div>
  
      <p>Original: {{ message }}</p>
      <p>Reverse by Method: <strong>{{ reverseMessage() }}</strong></p>
      <p>Reverse by Computed: <strong>{{ reversedMessage }}</strong></p>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      const app = new Vue ({
        el: '#app',
        data: {
          message: 'Original',
          other: 'asdf'
        },
        // data를 바꾸는 로직 위주(setter 함수)
        methods: {
          reverseMessage() {
            console.log('method')
            return this.message.split('').reverse().join('')
          }
        },
        // data를 통한 값을 얻는게 핵심 (getter 함수)
        computed: {
          // (data에 의존하는) 계산된 값
          reversedMessage() {
            console.log('computed')
            return this.message.split('').reverse().join('')
          }
        }
      })
    </script>
  ```

  

**Options/Data - 'watch'**

- 데이터를 감시

- 데이터에 변화가 일어났을 때 실행되는 함수

  ```html
    <div id="app">
      <p>{{ num }}</p>
      <button @click="num += 1">add 1</button>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      const app = new Vue({
        el: '#app',
        data: {
          num: 2,
        },
        watch: {
          num: function () {
            console.log(`${this.num}이 변경되었습니다.`)
          }
        },
  ```

  

**computed vs. watch**

- computed
  - 특정 데이터를 직접적으로 사용/가공하여 다른 값으로 만들 때 사용
  - 속성 계산해야 하는 목표 데이터를 정의하는 방식
  - 소프트웨어 공학에서 이야기하는 '선언형 프로그래밍' 방식
  - "특정 값이 변동하면 해당 값을 다시 계산해서 보여준다"
- watch
  - 특정 데이터의 변화 상황에 맞춰 다른  data 등이 바뀌어야 할 때 주로 사용
  - 감시할 데이터를 지정하고 그 데이터가 바뀌면 특정 함수를 실행하는 방식
  - 소프트웨어 공학에서 이야기하는 '명령형 프로그래밍' 방식
  - "특정 값이 변동하면 다른 작업을 한다"
  - 특정 대상이 변경되었을 때 콜백 함수를 실행시키기 위한 트리거



선언형 & 명령형

- 선언형 프로그램
  - 계산해야 하는 목표 데이터를 정의 (computed)
- 명령형 프로그램
  - 데이터가 바뀌면 특정 함수를 실행해 (watch)



**Options/Assets - filter**

- 텍스트 형식화를 적용할 수 있는 필터

- 배열에도 쓸 수 있지만 텍스트에서 주로 사용(?)

- chaining 가능

  ```html
  <body>
    <div id="app">
      {{ numbers | getOddNumbers | getUnderTen }}
      {{ getOddAndUnderTen }}
    </div>
  
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      const app = new Vue({
        el: '#app',
        data: {
          numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        },
        filters: {
          getOddNumbers(array) {
            return array.filter(num => num%2)
          },
          getUnderTen(array) {
            return array.filter(num => num < 10)
          }
        },
        computed: {
          getOddAndUnderTen() {
            return this.numbers.filter(num => num % 2 && num < 10)
          }
        }
      })
    </script>
  ```

  

## Lifecycle Hooks

created

외부 API에서 초기 데이터 받아올 때 주로 사용

vue 바구니의 생애주기

데이터 가져옴

created에서 함수 실행할 수 있음

html 만듦

연결

created 때 데이터를 준비해둬야 원하는 페이지를 출력 가능(?)

mounted : 연결과정

updated는 현업에서 잘 안씀. updated할 때 가상 DOM 사용함

-  

  ```html
    <div id="app">
      <img v-if="imgSrc" :src="imgSrc" alt="sample img">
      <button @click="getImg">GetDog</button>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      const API_URL = 'https://dog.ceo/api/breeds/image/random'
      const app = new Vue({
        el: '#app',
        data: {
          imgSrc: '',
        },
        methods: {
          getImg: function () {
            axios.get(API_URL)
              .then(response => {
                this.imgSrc = response.data.message
              })
          }
        },
        // vue 인스턴스가 생성될 때 해당 함수를 실행함
        created: function () {
          this.getImg()
        }
      })
    </script>
  ```

  