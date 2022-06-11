# JavaScript 03

[toc]

## AJAX

- Asynchronous JavaScript And XML (비동기식 JavaScript와 XML)
  - XML : eXtended Markup Language
- 서버와 통신하기 위해 **XMLHttpRequest** 객체를 활용
-  X가 XML이긴 하지만 JSON을 더 많이 사용함
  - 더 가벼운 용량과 JavaScript의 일부라는 장점 때문
  - XML에는 불필요한 데이터가 상대적으로 많은 편



**AJAX 특징**

- 비동기성
  - 페이지 전체를 reload(새로 고침)를 하지 않고서도 수행
  - 서버의 응답에 따라 전체 페이지가 아닌 일부분만을 업데이트 할 수 있음
- 주요 두 가지 특징
  1. 페이지 새로 고침 없이 서버에 요청
  2. 서버로부터 데이터를 받고 작업을 수행



**AJAX 배경**

- AJAX는 특정 기술이 아닌 기존의 여러 기술을 사용하는 새로운 접근법을 설명하는 용어
- Gmail & Goodgle Maps
- 로딩바, 넷플릭스 로고 -> 사용자 경험을 늘리기 위해



**XMLHttpRequest 객체**

- 서버와 상호작용하기 위해 사용되며 전체 페이지의 새로 고침 없이 데이터를 받아올 수 있음

- 주로 AJAX 프로그래밍에 사용

- 이름과 달리 XML 뿐만 아니라 모든 종류의 데이터를 받아올 수 있음

- 생성자
  - `XMLHttpRequest()`
  
  ```js
  const request = new XMLHttpRequest()
  const URL = 'http://jsonplaceholder.typicode.com/todos/1/'
  
  request.open('GET', URL)
  request.send()
  
  const todo = request.response
  console.log(`data: ${todo}`)	// todo 출력되지 않음 why? 데이터 응답을 기다리지 않고 console.log()를 먼저 실행했기 때문
  ```
  
  

블럭 / 논블럭

함수 리턴을 기준으로 리턴 이전의 코드가 다 실행될 때 까지 기다리느냐 마느냐

동기 / 비동기

a, b가 순차적으로 일하느냐 동시에 일하느냐



블럭 + 비동기, 논블럭 + 동기 존재할 수 있음



## Asynchronous JavaScript

> 비동기 자바스크립트



**동기식**

- 순차적, 직렬적 Task 수행

- 요청을 보낸 후 응답을 받아야만 다음 동작이 이루어짐 (blocking)

  ```js
  <script>
      const btn = document.querySelector('button')
  
  	btn.addEventListener('click', function () {
          alert('You clicked me!')
          const pElem = document.createElement('p')
          pElem.innerText = 'sample text'
          document.body.appendChild(pElem)
      })
  </script>
  ```

  - alert 이후의 코드는 alert의 처리가 끝날 때까지 실행되지 않음



**비동기식**

- 병렬적 Task 수행

- 요청을 보낸 후 응답을 기다리지 않고 다음 동작이 이루어짐 (non-blocking)

- 왜 JS는 왜 기다려주지 않는 방식으로 동작하는가?

  - JavaScript는 single threaded

  ```js
  const request = new XMLHttpRequest()  // 생성할 때 new 적어야 함(파이썬의 init같은 느낌)
  const URL = 'https://jsonplaceholder.typicode.com/todos/1/'   // 더미데이터 주는 사이트
  
  request.open('GET', URL)    // 여기까지 동기식
  request.send()    // 비동기식 (응답이 올 때까지 기다리지x), 논블럭(위의 코드가 완료될 때까지 기다리지 x). XMLHttpRequest 요청
  
  const todo = request.response   // 동기식. 빈 응답 값을 todo에 할당
  console.log(todo)
  ```



**왜 비동기를 사용하는가?**

- 사용자 경험
  - 비동기식 코드라면 데이터를 요청하고 응답 받는 동안, 앱 실행을 함께 실행함
    - 데이터를 불러오는 동안 지속적으로 응답하는 화면을 보여줌
    - 더욱 쾌적한 사용자 경험을 제공
  - 많은 웹 API 기능은 현재 비동기 코드를 사용하여 실행됨



**[참고] Threads**

- 프로그램이 작업을 완료하기 위해 사용할 수 있는 단일 프로세스
- 각 thread(스레드)는 한 번에 하나의 작업만 수행할 수 있음
- 브라우저는 1개의 탭 당 하나의 thread(일꾼)



Blocking vs. Non-Blocking

- Blocking

  ```python
  import requests
  
  response = requests.get('https://jsonplaceholder.typicode.com/todos/1/')
  todo = response.json()
  
  print(todo)
  ```

- Non-Blocking

  ```js
  const request = new XMLHttpRequest()
  const URL = 'https://jsonplaceholder.typicode.com/todos/1/'
  
  request.open('GET', URL)
  reuqest.send()
  
  const todo = request.response
  console.log(todo)
  ```

  



> "JavaScript는 single threaded이다"

- 이벤트를 처리하는 Call Stack이 하나인 언어라는 의미
- 이 문제를 해결하기 위해
  1. 즉시 처리하지 못하는 이벤트들을 다른 곳(Web API)으로 보내서 처리하도록 하고
     - 처리는 자바스크립트 엔진이 함
     - Web API는 브라우저
  2. 처리된 이벤트들은 처리된 순서대로 대기실(Task queue)에 줄을 세워 놓고
  3. Call Stack이 비면 담당자(Event Loop)가 대기 줄에서 가장 오래된(제일 앞의) 이벤트를 Call Stack으로 보냄



**Concurrency model**

- Event loop를 기반으로 하는 동시성 모델(Concurrency model)

1. **Call Stack**

   - 요청이 들어올 때마다 해당 요청을 순차적으로 처리하는 Stack(LIFO)형태의 자료 구조

2. **Web API (Browser API)**

   - JavaScript 엔진이 아닌 브라우저 영역에서 제공하는 API
     - ex) 크롬이 API를 통해 일을 처리해줌
     - ex) addEventListener
     - multi thread
   - AJAX로 데이터를 가져오는 시간이 소요되는 일들
   - setTimeout(), DOM events
   - AJAX, 시간 관련 일들은 Web API가 함 => 비동기 동작 (언제 끝날지 모르는 일들)

3. **Task Queue**

   - 여기 쌓여있는 애들은 바로 call stack에 오는 애들보다 우선순위가 낮음
   - 먼저 끝나더라도 순위가 더 높은 애들이 끝날 때까지 실행 x
   - call stack에 비어있을 때만 task queue에서 빼서 올라갈 수 있음(?)
   - web api에서 먼저 끝낸 것 먼저 queue에 넣어줌

4. **Event Loop**

   - 자동 감시자
   - Call Stack이 비어있는지 확인
   - Task Queue에 대기 중인 callback 함수가 있다면 가장 앞에 있는 callback함수를 Call Stack으로 push
   
   ```js
   console.log('Hi')	// 1순위
   
   setTimeout(function go () {	// setTimeout 함수 자체는 1순위 (Web API에 던지고 끝남)
       console.log('GO')
   }, 3000)		// 콜백 함수는 2순위
   
   console.log('Bye')	// 1순위
   ```
   
   

순차적인 비동기 처리하기

- Web API로 들어오는 순서는 중요 x
- 어떤 이벤트가 **먼저 처리되느냐**가 중요(즉, 실행 순서 불명확)
- 이를 해결하기 위해 순차적인 비동기 처리를 위한 2가지 작성 방식
  1. Async callbacks
     - 백그라운드에서 실행을 시작할 함수를 호출할 때 인자로 지정된 함수
     - ex) addEventListener()의 두 번째 인자
  2. promise-style
     - XMLHttpRequest 객체를 사용하는 구조보다 조금 더 현대적인 버전



### Callback Function

- 다른 함수에 인자로 전달된 함수
- 외부 함수 내에서 호출되어 일종의 루틴 또는 작업을 완료함
- 동기식, 비동기식 모두 사용됨
  - 비동기 작업이 완료된 후 코드 실행을 계속하는 데 주로 사용됨
- 비동기 작업이 왼료된 후 코드 실행을 계속하는 데 사용되는 경우 = 비동기 콜백(asynchronous callback)



JavaScript의 함수는 "일급 객체 (First Class Object)"

- 일급 객체 (일급 함수)
  - 다른 객체들에 적용할 수 있는 연산을 모두 지원하는 객체(함수)
  - 자격
- 일급 객체 조건
  - 인자로 넘길 수 있어야 함
  - 함수의 반환 값으로 사용할 수 있어야 함
  - 변수에 할당할 수 있어야 함



**Async callback**

- 백그라운드에서 코드 실행을 시작할 함수를 호출할 때 인자로 지정된 함수
- 백그라운드 코드 실행이 끝나면 callback 함수를 호출하여 작업이 완료되었음을 알리거나, 다음 작업을 실행하게 할 수 있음
  - ex) addEventListener()의 두 번째 매개변수

- callback 함수를 다른 함수의 인수로 전달할 때, 함수의 참조를 인수로 전달할 뿐 즉시 실행되지 않고, 함수의 body에서 "called back"됨.
  정의된 함수는 때가 되면 callback 함수를 실행하는 역할을 함



**Why use callback?**

-  callback 함수 : 명시적인 호출이 아닌 특정 루틴 혹은 action에 의해 호출되는 함수
-  비동기 로직을 수행할 때 callback 함수는 필수
   -  명시적인 호출이 아니라 다른 함수의 매개변수로 전달하여 해당 함수 내에서 특정 시점에 호출




**callback Hell**

- 여러 개의 연쇄 비동기 작업을 할 때 마주하는 상황



callback Hell 해결하기

1. Keep your code shallow
2. Modularize
3. Handle every single error
4. **Promise callbacks** (Promise 콜백 방식 사용)



### Promise

**Promise object**

- 비동기 작업의 최종 완료 또는 실패를 나타내는 객체
- 성공(이행)에 대한 약속
  - `.then()`
- 실패(거절)에 대한 약속
  - `.catch()`



**Promise methods**

- `.then(callback)`
  -  이전 코드가 성공했다면 then을 실행
  -  각 callback 함수는 이전 작업의 성공 결과를 인자로 전달받음
  -  → 성공했을 때의 코드를 callback 함수 안에 작성

- `.catch(callback)`
  -  언제든 오류 발생하면 catch 실행

- 각각의 `.then()` 블록은 서로 다른 promise를 반환

  - `.then`을 여러 개 사용(chaining)하여 연쇄적인 작업을 수행할 수 있음

- .then()과 .catch() 메서드는 모두 promise를 반환하기 때문에 chaining 가능

  ※ 반환 값이 반드시 있어야 함 (없다면 callback 함수가 이전의 promise 결과를 받을 수 없음)

- `.finally(callback)`
  -  위의 코드 성공/실패 여부에 상관없이 무조건 실행
  -  어떠한 인자도 전달받지 않음



**Promise가 보장하는 것**

- Async callback 작성 스타일과 달리 Promise가 보장하는 특징
  1. 엄격한 순서로 호출됨
  2. .then() 메서드를 이용
  3. chaining



### Axios

- "Promise based HTTP client for the brower and Node.js"

- 브라우저를 위한 Promise 기반의 클라이언트

- 확장 가능한 인터페이스와 함께 패키지로 사용이 간편한 라이브러리를 제공
  - jsDelivr CDN or unpkg CDN 둘 중 하나 골라서 복붙
  
- 알아서 파싱해줌(res.data)

- Axios 깃헙에서 사용법 찾아볼 수 있음

  ```js
  axios.get('주소')	// Promise return
  	.then(..)
  	.catch(..)
  ```

  



## [부록] async & await

callback 과 promise는 다름

promise와 async & await은 같음

- Promise 구조의 then chaining을 제거
- 비동기 코드를 조금 더 동기 코드처럼 표현

요즘은 거의 다 async-await으로 처리함

- Promise

  ```js
  const URL = 'https://dog.ceo/api'
  
  function fetchFirstDogImage() {
      axios.get(URL + '/breeds/list/all')
      	.then(res => {
          const breed = Object.keys(res.data.message)[0]
          return axios.get(URL + '/breed/${breed}/images')
      	})
      	.then(res => {
          console.log(res)
      	})
      	.catch(err => {
          console.error(err.response)
      	})
  }
  
  fetchFristDogImage()
  ```

- async & await

  ```js
  const URL = 'https://dog.ceo/api'
  
  async function fetchFirstDogImage() {
      const res = axios.get(URL + '/breeds/list/all')
      const breed = Object.keys(res.data.message)[0]
      const images = await axios.get(URL + '/breed/${breed}/images')
      console.log(res)
  }
  
  fetchFristDogImage()
  	.catch(err => console.error(err.response))
  ```

  