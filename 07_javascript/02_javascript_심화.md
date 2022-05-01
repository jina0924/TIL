# JavaScript 심화

[toc]

## History of JS

- 팀 버너스리
  - 웹의 아버지
- 브랜던 아이크
  - 자바스크립트 최초 설계자
  - 모질라 재단 공동 설립자
- 자바스크립트의 탄생
  - 브라우저 전쟁
    - 크로스 브라우징 이슈



## DOM 조작과 Event

브라우저에서 할 수 있는 일

- DOM 조작
  - 문서(HTML) 조작
- BOM 조작
  - navigator, screen, location, frames, history, XHR
- JavaScript Core (ECMAScript)
  - Data Structure(Object, Array), Conditional Expression, Iteration



### DOM

**DOM**

- HTML, XML과 같은 문서를 다루기 위한 문서 프로그래밍 인터페이스
- 문서가 구조화되어 있으며 각 요소는 객체(object)로 취급 - 논리적 트리 모델
- 주요 객체
  - window : DOM을 표현하는 창. 가장 최상위 객체(작성 시 생략 가능)
  - document : 페이지 컨텐츠의 Entry Potin 역할. `<body>`등과 같은 수 많은 다른 요소들을 포함



**BOM**

- Brower Object Model

- 자바스크립트가 브라우저와 소통하기 위한 모델

- 브라우저의 창이나 프레임을 추상화해서 프로그래밍적으로 제어할 수 있도록 제공하는 수단

  - 버튼, URL 입력창, 타이틀 바 등 브라우저 윈도우 및 웹 페이지 일부분을 제어 가능

  ```js
  window.open()	// 새 탭(새 창) 열림
  window.print()	// 인쇄 페이지로 넘어감
  ```

  

**JavaScript Core**

- 프로그래밍 언어

  ```js
  const numbers = [1, 2, 3, 4, 5]
  for (let i=0; i < numbers.length; i++) {
      console.log(numbers[i])
  }
  ```



### DOM 조작

**개념**

- Document는 문서 한 장(HTML)에 해당하고 이를 조작
- DOM 조작 순서
  1. 선택 (Select)
  2. 변경(Manipulation)



DOM 관련 객체의 상속 구조

- EventTarget
  - Event Listener를 가질 수 있는 객체가 구현하는 DOM 인터페이스
- Node
  - 여러 가지 DOM 타입들이 상속하는 인터페이스
- Element
- Document
- HTMLElement



#### DOM 선택

- `document.querySelector(selector)`

  - 단일 element
  - 제공한 선택자를 만족하는 첫 번째 element 객체를 반환

  ```js
      const h1 = document.querySelector('h1')
      const h2 = document.querySelector('h2')
      // 명시적으로 적는게 좋음(id를 통해서 선택하는걸 권장)
      const secondH2 = document.querySelector('#location-header')
      const selectUlTag = document.querySelector('div > ul')
  ```

- `document.querySelectorAll(selector)`

  - 제공한 선택자와 일치하는 여러 element를 선택
  - NodeList를 반환

  ```js
      // 1-3. querySelectorAll
      const liTags = document.querySelectorAll('li')
      const secondLiTags = document.querySelectorAll('.ssafy-location')
  ```

- querySelector(), querySelectorAll()를 사용하는 이유

  - id, class 그리고 tag 선택자 등을 모두 사용 가능
  - HTMLCollection은 DOM의 변경사항을 실시간으로 collection에 반영함



#### DOM 변경

**변경 관련 메서드 (Creation)**

- `document.createElement()`

  - 작성한 태그 명의 HTML 요소를 생성하여 반환

  ```js
      const ulTag = document.querySelector('ul')
      const newLiTag = document.createElement('li')
  ```



**변경 관련 메서드 (append DOM)**

- `Element.append()`

  - 특정 부모 Node의 자식 NodeList 중 마지막 자식 다음에 Node객체나 DOMString을 삽입
  - 여러 개의 Node 객체, DOMString을 추가할 수 있음
  - 반환값 없음

  ```js
      ulTag.append(newLiTag)
      ulTag.append('문자열도 추가 가능')
  ```

- `Node.appendChild()`

  - Node만 추가 가능
  - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입
  - 한번에 오직 하나의 Node만 추가할 수 있음
    - 추가된 Node 객체 반환

  - 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 새로운 위치로 이동
  
  ```js
      const ulTag = document.querySelector('ul')
      const newLiTag = document.createElement('li')
      newLiTag.innerText = '새로운 리스트 태그'
      ulTag.appendChild(newLiTag)
      ulTag.appendChild('문자열은 추가 불가')	// 추가 안됨
  ```



**변경 관련 속성 (property)**

- `Node.innerText`

  - 모두 문자열로
  - 최종적으로 스타일링이 적용된 모습으로 표현

  ```js
      const new1 = document.createElement('li')
      new1.innerText = '리스트 1'
      const new2 = document.createElement('li')
      new2.innerText = '리스트 2'
  ```

- `Element.innerHTML`
  - 요소 내에 포함된  HTML 마크업을 반환
  - XSS 공격에 취약하므로 사용 시 주의
    - 특히 사용자 입력을 받을 때
    - XSS (Cross-site Scripting) : 공격자가 입력요소를 사용하여(`<input>`) 웹 사이트 클라이언트 측 코드에 악성 스크립트를 삽입해 공격하는 방법



#### DOM 삭제

- `ChildNode.remove()`

  - Node가 속한 트리에서 해당 Node를 제거
  - django에서 인스턴스 삭제하는 것과 유사함

  ```js
      const header = document.querySelector('#location-header')
      header.remove()
  ```

- `Node.removeChild()`

  - DOM에서 자식 Node를 제거하고 제거된 Node를 반환
  - Node : 인자로 들어가는 자식 Node의 부모 Node

  ```js
      const parent = document.querySelector('ul')
      const child = document.querySelector('ul > li')
      const removedChild = parent.removeChild(child)
      console.log(removedChild)
      // 순서 바꾸기 (삭제할 때 반환된 값을 변수에 담아두고 뒤에 다시 붙여넣음)
      parent.append(child)
  ```




#### DOM 속성 - 속성 관련 메서드

- `Element.setAttribute(name, value)`

  - 지정된 요소 값을 설정
  - 속성이 이미 존재 → 갱신
  - 속성이 존재하지 않음 → 지정된 이름과 값으로 새 속성을 추가

  ```js
  const header = document.querySelector('#location-header')
  header.setAttribute('class', 'ssafy-location')
  ```

  

- `Element.getAttribute(attributeName)` 

  - 해당 요소의 지정된 값(문자열)을 반환
  - 인자(attributeName)는 값을 얻고자 하는 속성의 이름

  ```js
  const getAttr = document(querySelector('.ssafy-location'))
  getAttr.getAttribute('class')
  'ssafy-location'
  ```

  

### DOM 조작 실습

```js
h1.innerText
'Hello SSAFY'
h1.innerText = '쉬는 시간!!'	// 객체값 바꿈
'쉬는 시간!!'
```



### Event

- 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체
- 이벤트 발생
  - 마우스를 클릭하거나 키보드를 누르는 등 사용자 행동으로 발생할 수도 있음
  - 특정 메서드를 호출(Element.click())하여 프로그래밍적으로도 만들어 낼 수 있음



**Event 기반 인터페이스**

- AnimationEvent, ClipboardEvent, DragEvent 등
- UIEvent
  - 간단한 사용자 인터페이스 이벤트
  - Event의 상속을 받음
  - MouseEvent, KeyboardEvent, InputEvent, FocusEvent 등의 부모 객체 역할을 함




"특정 이벤트가 발생하면, 할 일을 **등록** 한다"



**Event handle - addEventListener()**

- `EventTartget.addEventListener()`

  - 지정한 이벤트가 대상에 전달될 때마다 호출할 함수를 설정
  - 이벤트를 지원하는 모든 객체를 대상으로 지정 가능

- `target.addEventListener(type, listener[, options])`

  - type
    - 반응 할 이벤트 유형 (대소문자 구분 문자열)
    - 특정 이벤트
      - reset(리셋 버튼 눌렀을 때), submit(제출 버튼 눌렀을 때), click, dbclick, wheel,...
  - listener
    - 지정된 타입의 이벤트가 발생했을 때 알림을 받는 객체
    - EventListener 인터페이스 혹은 JS function 객체(콜백 함수)여야 함
    - 할 일/동작 명세
  
  - `대상.addEventListener(특정 이벤트, 할 일)`
  
    ex) `btn.addEventListener('click', f(){ 경고창 })`
  
  ```js
      // 함수가 실행될 때 event가 넘어옴 but. 안써도 오류 내지 않음
      const alertMessage = function () {
        alert('메롱!!!')
      }
  
      const myButton = document.querySelector('#my-button')
      /*
      alertMessage뒤에 괄호 안 적는 이유: alertMessage함수는 return값 없음 -> undefined가 리턴됨 => 괄호 붙이면 undefined를 넘기는 셈
      ex) path('articles/', views.index)에서 index()로 안적는것과 같은 원리
      */
      myButton.addEventListener('click', alertMessage)
  ```
  
  ```js
      const myTextInput = document.querySelector('#my-text-input')
  
      /*
      event: 어디서 넘어오는지 보이진 않지만 addEventListener에서 알아서 넘어옴
      ex) def index(request)에서 request는 path함수가 알아서 채워서 보냄
      */
      const myP = document.querySelector('#my-paragraph')
      const ifInputIsComing = function (event) {
        // console.log(event.target.value)
        myP.innerText = event.target.value
      }
  
      myTextInput.addEventListener('input', ifInputIsComing) 
  
      // 함수명 굳이 만들지 않고 안에 아예 넣어도 됨
      // myTextInput.addEventListener('input', function (event) {
      //   const myP = document.querySelector('#my-paragraph')
      //   myP.innerText = event.target.value
      // })
      
  	// 화살표 함수로 축약
      // myTextInput.addEventListener('input', event => myP.innerText = event.target.value)
  ```
  
  ```js
      // 입력받은 값과 같은 색으로 색상 변경
  	const h2Tag = document.querySelector('h2')  // 입력마다 소환할 것 없이 한번만 선택되면 됨
  
      const onColorInput = function (event) {
        const userInput = event.target.value
        h2Tag.style.color = userInput
      }
  
      const colorInput = document.querySelector('#change-color-input')
      colorInput.addEventListener('input', onColorInput)
  ```
  
  

**Event 취소**

- `event.preventDefault()`

- 현재 이벤트의 기본 동작을 중단

- HTML 요소의 기본 동작을 작동하지 않게 막음
  - ex) a 태그 기본 동작 -> 클릭 시 링크로 이동
  
- 이벤트를 취소할 수 있는 경우, 이벤트의 전파를 막지 않고 그 이벤트를 취소

  ```js
  const formTag = document.querySelector('#my-form')
  
  formTag.addEventListener('submit', function (event) {
      console.log(event)
      event.preventDefault()
      event.target.reset()		//	제출 후 작성한 값 지우기
  })
  ```

- 취소할 수 없는 이벤트도 존재
  - 취소 가능 여부는 `event.cancelable`을 사용해 확인할 수 있음