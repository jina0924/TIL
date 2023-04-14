# 브라우저

[toc]

## 기본 개념

브라우저 : 인터넷에서 웹 페이지를 보여주는 소프트웨어



## 작동 원리

1. 사용자가 URL 입력
   - 사용자가 URL을 입력하면, 브라우저는 DNS(Domain Name System) 서버에서 해당 도메인 이름의 IP 주소를 가져옴
2. 서버와 연결
   - IP 주소를 얻으면 브라우저는 해당 서버에 HTTP(Hypertext Transfer Protocol) 요청을 보내서 웹 페이지를 가져옴
3. 웹 페이지 다운로드
   - 브라우저가 서버에서 받은 HTML(Hypertext Markup Language) 파일을 다운로드하고, CSS(Cascading Style Sheets) 파일과 JavaScript 파일을 가져옴.
4. HTML 파싱
   - 브라우저가 HTML 파일을 파싱하여 웹 페이지의 DOM(Document Object Model)을 생성
   - DOM : 웹 페이지의 구조와 콘텐츠를 나타내는 트리 구조
5. CSS 파싱
   - 브라우저가 CSS 파일을 파싱하여 각 요소의 스타일을 결정함
     - 이를 통해 브라우저는 웹 페이지의 레이아웃을 결정
6. JavaScript 실행
   - 브라우저가 JavaScript 파일을 실행하여 웹 페이지를 동적으로 만듦
     - 이를 통해 사용자와 상호작용하거나, 페이지의 콘텐츠를 업데이트하거나, 애니메이션을 추가 가능
7. 웹 페이지 렌더링
   - 파싱된 HTML, CSS 및 JavaScript를 결합하여 최종적으로 웹 페이지를 렌더링
   - 이 과정에서는 각 요소의 크기와 위치가 결정되고, 웹 페이지의 콘텐츠가 화면에 표시됨
8. 렌더링된 페이지를 사용자에게 보여줌
   - 최종적으로 렌더링된 웹 페이지를 사용자에게 보여줌



### DOM

> Document Object Model

- HTML, XML등의 문서를 프로그래밍 언어에서 다룰 수 있는 객체 모델로 변환하는 인터페이스
- 웹 페이지의 요소들을 트리구조로 나타내고 이 요소들을 조작하는 메서드와 프로퍼티를 제공
- 웹 브라우저가 HTML 문서를 렌더링하고, 사용자의 이벤트를 처리하기 위해 필요함



**작동 과정**

1. HTML 문서 로드

   ```html
   <!DOCTYPE html>
   <html>
     <head>
       <title>DOM 예시</title>
     </head>
     <body>
       <h1>DOM 예시</h1>
       <p>이 문서는 DOM의 예시입니다.</p>
     </body>
   </html>
   ```

2. DOM트리 생성

   ```js
   // HTML 요소(element)들을 객체로 표현한 DOM 트리
   document
     |- doctype
     |- html (Element)
          |- head (Element)
          |    |- title (Element)
          |         |- "DOM 예시" (Text)
          |
          |- body (Element)
               |- h1 (Element)
               |    |- "DOM 예시" (Text)
               |
               |- p (Element)
                    |- "이 문서는 DOM의 예시입니다." (Text)
   ```

   - `document` : 문서 전체를 나타내는 최상위 객체
   - `doctype` : 문서 유형을 나타내는 객체
   - `html`, `head`, `h1` 등 : HTML 요소(element)를 나타내는 객체
     - 이 객체들은 `Element` 클래스의 인스턴스
     - 각 객체는 각자의 속성(attribute)과 메서드(method)를 가지고 있음

3. CSS 스타일 적용하여 브라우저 화면에 웹 페이지 그림

4. JavaScript를 이용하여 DOM을 조작하면 변경된 내용이 화면에 실시간으로 반영됨



### 가상 DOM

- 브라우저 상의 실제 DOM을 추상화한 가상의 DOM
- 가상 DOM의 장점
  1. 성능 향상
     - 변경사항이 있는 부분만을 갱신하는 최적화된 방식으로 UI를 업데이트 => 실제 DOM 조작 횟수를 줄일 수 있음
     - 브라우저에서 UI를 다시 그리는 빈도를 줄여서 성능을 향상시킴
  2. 개발 생산성 향상
     - UI 업데이트를 추상화하므로, 개발자가 실제 DOM 조작에 집중하는 대신, UI를 추상화한 가상 DOM에 대해 작업할 수 있음
  3. 크로스 플랫폼
     - 가상 DOM은 브라우저의 실제 DOM과는 독립적으로 작동하기 때문에, 다양한 플랫폼에서 동일한 코드를 실행할 수 있음
     - React Native와 같은 React 기반의 모바일 애플리케이션 개발에 유용함
  4. 테스트 용이성
     - 가상 DOM은 브라우저에서 실제 DOM과 동일한 API를 제공하기 때문에, 브라우저에서 실행되는 테스트 프레임워크에서 가상 DOM을 이용하여 UI 업데이트를 검증할 수 있음