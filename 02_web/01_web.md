# 01_01_HTML & CSS

[toc]



- 웹 서비스란?
  - **request** & **response**
  - request : client가 server에 주소창/코드를 통해 요청함
    - `requests.get()`
  - response : server가 html이라는 문서 1장을 response

- 현재의 웹 표준
  - W3C
  - WHATWG -> WIN
- Browser
  - 브라우저가 표준을 얼마나 잘 지켰는지 -> 익스플로러 점수 낮음
  - 크롬 점수 가장 높음 why? 표준을 잘 지킴 & 속도 빠름(내장 엔진 좋음)
- Can I use?
  - 브라우저 별로 지원하는 기능 알아볼 수 있음



## 개발 환경 설정



## HTML

> 문서
>
> Hyper Text Markup Language

- Hyper Text
  - 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
  - 링크를 타고 넘나듦
- Markup Language
  - 태그 등을 이용하여 문서나 데이터의 구조(강조점)를 명시하는 언어
    - ex) HTML, Markdown

∴ 웹 페이지를 작성(구조화)하기 위한 언어



### Markup Example

`<h1>내용</h1>` : 내용을 강조하기 위해 태그 붙임 -> 제목 크게 만듦x. 구조화



## HTML 기본 구조

여는 태그 + 닫는 태그

- **html** : 문서의 최상위(root) 요소

- **head** : 문서 메타데이터 요소
  - 메타데이터란? - 데이터에 대한 데이터. 데이터에 관한 구조화된 데이터
    - ex) 사진 정보, 도서관에서 서지기술용으로 만든 것
  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
  
  - 일반적으로 브라우저에 나타나지 않는 내용
  
- **body** : 문서 본문 요소
  - 실제 화면 구성과 관련된 내용

```html
<!DOCTYPE html>
<html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>Document</title>
    </head>
    <body>
        
    </body>
</html>
```

※ `!` + `tap` : 기본 골격 만들어줌



### head 예시

- `<title>` : 브라우저 상단 타이틀(탭에 써있는 이름)

- `<mata>` :문서 레벨 메타데이터 요소

- `<link>` : 외부 리소스 연결 요소(CSS 파일, favicon 등)

- `<script>` : 스크립트 요소(JavaScrpit 파일/코드)

- `<style>`: CSS 직접 작성

  ```html
  <head>
    <title>HTML 수업</title>
    <meta charset="UTF-8">
    <link href="style.css" rel="stylesheet">
    <script src="javascript.js"></script>
    <style>
    p {
      color: black;
    >
    </style>
  </head>
  ```

  



### head 예시 : Open Graph Protocol

- 메타 데이터를 표현하는 새로운 규약
  - 페이스북에서 처음 만들었는데 하도 많이 써서 표준처럼 됨
    - 카톡으로 링크 공유했을 때 미리보기 같은 창
  - HTML 문서의 메타 데이터를 통해 문서의 정보를 전달
  - 메타정보에 해당하는 제목, 설명 등을 쓸 수 있도록 정의



### DOM(Document Object Model) 트리 ★

코드가 계층구조를 갖고 있음

마크업 스타일 가이드(2 space) : 4 space도 가능하지만 2 space 권장

- 텍스트 파일인 HTML문서를 브라우저에서 **렌더링** 하기 위한 구조
  - HTML 문서에 대한 모델을 구성함




### 요소(element)

`<h1>contents</h1>`

- 여는 태그와 닫는 태그가 페어를 이룸. 그리고 태그 사이에 위치한 내용으로 구성
  - 태그는 컨텐츠(내용)를 감싸는 것으로 그 정보의 성격과 의미를 정의
  - 모든 태그가 닫는 태그가 있는 건 아님

- 내용이 없는 태그들★
  - br(개행), hr(수평선), img(이미지), input, link, meta
- 요소는 중첩(nested)될 수 있음
  - 요소의 중첩을 통해 하나의 문서를 구조화
  - 여는 태그와 닫는 태그의 쌍을 잘 확인해야함
    - 오류를 반환x 그냥 레이아웃 깨진 상태로 출력되기 때문에 디버깅에 어려움 겪을 수 있음
- 닫는 태그는 앞에 `/`를 적음



### 속성(attribute)

`<태그 속성명="속성값"></태그>`

ex) `<a href="https://google.com"></a>>`

태그별로 사용할 수 있는 속성은 다르다.

공통적인 속성/개별적 속성 있음

- 속성 지정 스타일 가이드
  - `=`양 옆에 공백 x
  - 속성에 들어가는 값은 쌍따옴표 사용
- 속성을 통해 태그의 **부가적인 정보**를 설정할 수 있음
- 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공
- 요소의 **시작 태그에 작성**하며 보통 **이름과 값이 하나의 쌍**으로 존재
- 태그와 상관없이 사용 가능한 속성(HTML Global Attribute)들도 있음



### HTML Global Attribute

- **id** : 문서 전체에서 유일한 고유 식별자 지정
- **class** : 공백으로 구분된 해당 요소의 클래스의 목록 -> 자주 사용함(클래스로 모듈화)
- **data-*** : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
- **style** : inline 스타일
- **title** : 요소에 대한 추가 정보 지정
- **tabindex** : 요소의 탭 순서



### 시맨틱 태그

> semantic : 의미론적인

- HTML5에서 등장한 의미론적 요소를 담은 태그의 등장
  - `<div>` : division. 구역 -> 기존 영역을 의미하는 **div태그를 대체하여 사용**
- 대표적인 태그 목록
  - **header** : 문서 전체나 섹션의 헤더(머리말 부분)
  - **nav** : 내비게이션
  - **aside** : 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
  - **section** : 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
  - **article** : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
  - **footer** : 마지막 부분
  - 다 div와 동일한 역할을 함
    - div로 적는것보다 SEO 점수 높음 -> why? 내용 구분하기 쉬워서
- Non semantic 요소는 div, span 등이 있으며(의미 딱히 없음)
- h1, table 태그들도 시맨틱 태그로 볼 수 있음
- 개발자 및 사용자 뿐만 아니라 검색엔진 등에 의미 있는 정보의 그룹을 태그로 표현
- 단순히 구역을 나누는 것 뿐만 아니라 '의미'를 가지는 태그들을 활용하기 위한 노력
- 요소의 의미가 명확해짐 -> 코드의 가독성↑ & 유지보수 쉬움
- **검색엔진최적화(SEO)**를 위해서 메타태그, 시맨틱 태그 등을 통한 마크업을 효과적으로 활용해야함



### HTML with 개발자 도구

>chrome : 마우스 우클릭 → 검사 / ctrl + shift + i

- elements : 해당 요소의 HTML 태그



## HTML 문서 구조화

html 태그

- inline
  - 컨텐츠의 크기만큼 차지함

- block
  - 한줄을 다 차지함
- 인라인 블록 요소(번외)



### 텍스트 요소

| 태그                               | 설명                                                         |
| ---------------------------------- | ------------------------------------------------------------ |
| `<a></a>`                          | href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성     |
| `<b></b>`<br />`<strong></strong>` | 같은 내용인데 위에는 굵은 글씨<br />밑에는 중요내용 강조(의미론) -> 권장 |
| `<i></i>`<br />`<em></em>`         | 기울임 글씨 요소<br />중요 내용 강조하고자 하는 요소         |
| `<br>`                             | 텍스트 내에 줄 바꿈 생성                                     |
| `<img>`                            | src 속성을 활용하여 이미지 표현. alt엔 대체텍스트            |
| `<span></span>`                    | 의미 없는 inline 컨테이너                                    |

- `<a></a>`
  - `<a href="https://edu.ssafy.com/" target="_blank">`
- `<img>`
  - `<img src="https://www.ssafy.com/swp/images/sns_img.png" alt="ssafy-logo-image">`

- b 태그 & strong 태그
  - 결과는 똑같지만 그냥 bold하고 싶으면 b태그, 강조하고 싶으면 strong태그



### 그룹 컨텐츠

| 태그                         | 설명                                                   |
| ---------------------------- | ------------------------------------------------------ |
| `<p></p>`                    | 하나의 문단(paragraph)                                 |
| `<hr>`                       | 수평선(A Horizontal Rule). 주제의 분리 의미            |
| `<ol></ol>`<br />`<ul></ul>` | 순서가 있는 리스트(ordered)<br />순서가 없는 리스트    |
| `<pre></pre>`                | HTML에 작성한 내용을 그대로 표현                       |
| `<blockquote></blockquote>`  | 텍스트가 긴 인용문<br />주로 들여쓰기 한 것으로 표현됨 |
| `<div></div>`                | 의미 없는 block 레벨 컨테이너                          |

- `<pre></pre>`

```html
<p>
    안녕하세요 여러분 <br>  <!-- <br> 없으면 밑에 줄도 그대로 옆에 붙어서 출력됨 -->
    하하하하하하
</p>
```

```html
<pre>
  안녕하세요 여러분
  하하하하하하
  </pre>
```

- `<ol></ol>`
  1. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
- `<ul></ul>`
  - Lorem ipsum dolor sit amet, consectetur adipiscing elit.





### table

- table의 각 영역을 명시하기 위해 `<thead><tbody><tfoot>`요소를 활용
  - **thead** : header
  - **tbody** : body. 실제 데이터에 대한 부분
  - **tfoot** : footer
  - **caption** : 테이블을 설명하기 위한 제목
  - `<tr>`로 **가로 줄**을 구성
  - 내부에는 `<th>` 혹은 `<td>`로 셀 구성
  - `colspan`, `rowspan` 속성을 활용하여 셀 병합
  - `<caption>`을 통해 표 설명 or 제목 작성
  
  ```html
      <table>
        <!-- thead -->
        <thead>
          <!-- tr th 첫 번째 가로줄 -->
          <tr>
            <th>ID</th>
            <th>Name</th>
          </tr>
        </thead>
        <!-- tbody -->
        <tbody>
          <!-- tr td 두 번째 가로줄 -->
          <tr>
            <td>1</td>
            <td>홍길동</td>
          </tr>
          <!-- tr td 세 번째 가로줄 -->
          <tr>
            <td>2</td>
            <td>김철수</td>
          </tr>
        </tbody>
        <!-- tfoot 마지막-->
        <tfoot>
          <!-- tr td -->
          <tr>
            <td>총계</td>
            <td colspan="2">2명</td>  <!-- html에선 계산x 직접 값 입력해야함 -->
          </tr>
        </tfoot>
        <caption>
          1반 학생 명단
        </caption>
      </table>
  ```
  
  



### form★

- `<form>`은 정보(데이터)를 서버에 제출하기 위한 영역

- `<form>`의 기본 속성

  - action : form을 처리할 서버의 URL

  - method : form을 제출할 때 사용할 HTTP 메서드 (GET 혹은 POST)

  - enctype : method가 psot인 경우 데이터의 유형

    ```html
    <form action="search" method="GET">
    </form>
    ```




### input

- 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨

- 대표적인 속성

  - name : form control에 적용되는 이름 (이름/값 페어로 전송됨)

  - value : form control에 적용되는 값 (이름/값 페어로 전송됨)

  - required, readonly, autofocus, autocomplete, disabled 등

    ex)

    ```html
        <div>
          <input type="text">
          <input type="submit" value="제출">
        </div>
    ```

    ex)

    ```html
    <form action="/search" method="GET">
        <input type="text" name="q"		<!-- https://www.google.com/search?q=HTML -->
    </form>
    ```

    


### input label

- input 태그가 뭘 하는지 설명해줌
- label을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있음

- 체크박스는 label의 for랑 input의 id를 일치시킬 것

  ```html
      <div>
        <p>checkbox</p>
        <input id="html" type="checkbox" name="language" value="html">
        <label for="html">HTML</label>
        <input id="python" type="checkbox" name="language" value="python">
        <label for="python">파이썬</label>
        <input id="python" type="checkbox" name="language" value="java">
        <label for="java">자바</label>
        <hr>
      </div>
  ```

  



### input 유형 - 일반

##### !!!!!!!!!!!!!!!!!!!

action : 어디로 보낼지 지정하는 것 when? submit 버튼이 눌렸을 때

method : 요청

name : 키

- 일반적으로 입력을 받기 위해 제공됨. 타입별로 HTML기본 검증 혹은 추가 속성을 활용할 수 있음

- text : 일반 텍스트 입력

- password : 입력 시 값이 보이지 않고 문자를 특수기호(`*`)로 표현

- email : 이메일 형식이 아닌 경우 form 제출 불가

- number : min, max, step 속성을 활용하여 숫자 범위 설정 가능

- file : accept 속성을 활용하여 파일 타입 지정 가능

  ex) 

  ```html
      <div>
        <p>file</p>
        <input type="file">
        <hr>
      </div>
  ```

  

### input 유형 - 항목 중 선택

- 일반적으로 label을 사용하여 내용을 작성하여 항목 중 선택할 수 있는 input을 제공
- 동일 항목에 대하여는 name을 지정하고 선택된 항목에 대한 value를 지정해야 함
  - checkbox : 다중 선택
  - radio : 단일 선택



### input 유형 - 기타

- 다양한 종류의 input을 위한 picker를 제공
  - color : color picker
  - date : date picker

- hidden input을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정
  - hidden : 사용자에게 보이지 않는 input



### 마크업 해보기

- `<a>` 속성 중 target
  - _blank : 새윈도우 창을 열어서 웹페이지 띄움
  - _self : 현재 윈도우창에 그대로 링크된 웹페이지 띄움
  - _parent : 현재 프레임의 부모 프레임에서 새 웹페이지 열림
  - _top : 최상위 프레임에서 열림

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>학생 건강 설문</title>
</head>
<body>
  <!-- header -->
  <header>
    <!-- 싸피 홈페이지로 이동하는 링크 -->
    <a href="edu.ssafy.com" target="_blank">
      <img src="https://www.ssafy.com/swp/images/sns_img.png" alt="ssafy-logo-image">
    </a>
  </header>

  <!-- section -->
  <section>
    <!-- 건강 설문 작성 form -->
    <h1>SSAFY 학생 건강설문</h1>
    <!-- 아직 서버에 보낼 내용 안배워서 "#"으로 채움(?) -->
    <form action="#">
      <!-- 이름 -->
      <div>
        <label for="name">이름을 기재해주세요.</label>
        <input type="text" id="name" autofocus name="name">
      </div>

      <!-- 지역 -->
      <div>
        <label for="region">지역을 선택해주세요.</label>
        <select name="region" id="region">
          <option value="서울">서울</option>
          <option value="대전">대전</option>
          <option value="광주">광주</option>
          <option value="구미">구미</option>
          <option value="부울경">부울경</option>
          <!-- 선택지에는 있으나 선택하지 못하게 하려면 disabled -->
          <option value="제주" disabled>제주</option>
        </select>
      </div>

      <!-- 체온 -->
      <div>
        <!-- 큰 역할 없이 하나의 문단 이룰 때 <p></p> -->
        <p>오늘의 체온을 선택해주세요.</p>
        <!-- 기본값으로 먼저 선택되어 있도록 하기 위해 checked -->
        <input type="radio" id="temp-normal" name="body-heat" value="normal" checked>
        <label for="temp-normal">37도 미만</label><br>
        <input type="radio" name="body-heat" id="temp-warning" value="warning">
        <label for="temp-warning">37도 이상</label>
      </div>
      <br>
      <!-- 전송 -->
      <input type="submit" value="제출">
    </form>
  </section>

  <!-- footer -->
  <footer>
    Google 설문지를 통해 비밀번호를 제출하지 마시오.
  </footer>
</body>
</html>
```







## CSS

> 문서를 꾸며주는 내용
>
> Cascading Style Sheets
>
> cascade : 폭포처럼 흐르다

- 스타일을 지정하기 위한 언어
  - 선택하고, 스타일을 지정한다



### CSS 구문

```css
h1 {
    color: blue;
    font-size: 15px;
}
```

- h1 : 선택자(무엇을 바꿀 것인가 -> 대상). html에서 원하는 것을 지정해서 스타일을 지정
- key: value처럼 선언

- font-size : 속성(property) -> 어떤 스타일 기능을 변경할지 결정

- 15px : 값(value) -> 어떻게 스타일 기능을 변경할지 결정



### CSS 정의 방법

- 인라인 태그를 활용하여 작성
- 내부 참조 - `<style>`
- 외부 참조 - 분리된 CSS 파일



#### CSS 정의 방법 - 1 (인라인)

###### !!!!!!!!!!!!!!!!추가!!!!!!!!!

#### CSS 정의 방법 - 2 (내부 참조)



#### CSS 정의 방법 - 3 (외부 참조) ★ 자주 사용

- 모듈화 가능
  - 폰트사이즈 같은데 색만 다르게 적용하고 싶다면 내부에 폰트만 넣고 외부에 색상 파일 만듦



### CSS with 개발자 도구





## CSS Selectors

### 선택자 유형

- 기본 선택자
  - 전체 선택자, 요소 선택자 (h1, h2, div,...)
  -  
- 결합자
  - 자손 결합자
  - 일반 형제 결합자
- 의사 클래스/요소(Pseudo Class)
  - 가상으로 선택하는 행위? hover
  -  



### 선택자 with 개발자 도구



### CSS 선택자 정리

- 요소 선택자
  - HTML 태그를 직접 선택
  - ex) h2, div

- 클래스 선택자

  - 여러 요소를 선택하여 변경 가능
  - 마침표(`.`)문자로 시작. 해당 클래스가 적용된 항목을 선택

- 아이디 선택자

  - `#` 문자로 시작. 해당 아이디가 적용된 항목을 선택
  - 단 한개의 요소만 선택 -> 여러 개도 선택 가능 but. 단일 id 사용 권장
    why? id는 JS에게 양보할 것.

  

- 자식 결합자

  - box 클래스 바로 아래 p만 선택

- 자손 결합자

  - box 클래스 아래 있으면 다 선택



### CSS 적용 우선순위

1. 중요도 (Importance) - 사용시 주의(사실상 안쓰는 걸 권장)
   - `!important`
2. 우선 순위 (Specificity)
   - 인라인 > id > class, 속성, pseudo-class > 요소, psedu-element
   - 명시적인 순서
3. CSS 파일 로딩 순서



### CSS 상속

- 부모 요소의 속성을 자식에게 상속
- 눈에 보이는 모든 것 상속 가능(?)
- 상속 되는 것 예시
  - Text 관련 요소
- 상속 되지 않는 것 예시
  - Box model 관련 요소, position 관련 요소 등


##### !!!!!!!!!!추가추가!!!!!!!!!



## CSS 기본 스타일

### 크기 단위

- px(픽셀)
  - 모니터 해상도의 한 화소인 '픽셀' 기준
  - 픽셀의 크기는 변하지 않기 때문에 고정적인 단위
- `%`
  - 백분율 단위
  - 가변적인 레이아웃에서 자주 사용
- em
  - (바로 위, 부모 요소에 대한) 상속의 영향을 받음 ex) text
  - 
- rem
  - 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐
  - root를 기준으로 함(일반적으로 root는 16px)
- viewport
  - 브라우저에서 보여지는 화면(디바이스 화면)



### 색상 단위

- 색상 키워드
- RGB 색상
  - rgb(R, G, B) 함수 표기형
- HSL 색상
- a 는 alpha(투명도)



### CSS 문서 표현

- 텍스트
- 컬러, 배경
- 기타 HTML 태그별 스타일링



## Selectors 심화

### 결합자

- 자손 결합자 : 공백
  - 하위의 모든 요소
- 자식 결합자 : `>`
  - 바로 아래
- 일반 형제 결합자 : `~`
  - A의 형제 요소 중 뒤에 있는 B 요소를 모두 선택
- 인접 형제 결합자
  - **바로 뒤**에 오는 B요소를 선택



## CSS Box model

모든 요소는 네모(box model)이고,

위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다. (좌측 상단에 배치)

block은 한 줄을 다 차지함 -> 다음 부분은 밑에 쌓임 ex) div => 위에서 아래로

Inline : content요소 크기에 맞춰 자리 차지함 ex)span => 왼쪽에서 오른쪽으로



### Box model

- 모든 HTML 요소는 box 형태로 되어있음
- 하나의 박스는 네 부분(영역)으로 이루어짐
  - content : 내용물
  - padding : 경계선과 내용물의 사이. 이미지, 배경색은 padding까지. 상하좌우 설정 가능
  - border : 테두리 영역
  - margin : 외부 여백. 배경색 지정 x. 상하좌우 설정 가능



#### Box model 구성(margin/padding)

전부

상하/좌우

상/좌우/하

상/우/하/좌(반시계방향)



기본이 content-box -> 눈에 보이는 부분은 border-box니까 이걸로 바꿔서 쓸것(?)



## CSS Display

- 모든 요소는 네모(박스모델)이고, 좌측상단에 배치
- **display에 따라 크기와 배치가 달라진다**



### 대표적으로 활용되는 display

- display: block
  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음
- display: inline
  - content 너비만큼 가로 폭을 차지한다.
  - **width, height, margin-top, margin-bottom을 지정할 수 없다**
  - 상하 여백은 line-height로 지정한다



### 블록 레벨 요소와 인라인 레벨 요소

- 블록 레벨 요소와 인라인 레벨 요소 구분
- 대표적인 블록 레벨 요소
  - div / ul, ol, li / p / hr / form 등
- 대표적인 인라인 레벨 요소
  - span / a / img / input, label / b, em, i, strong 등



### block

너비를 가질 수 없다면 자동으로 부여되는 margin (비어있어도 밑에서 올라올 수 없음)



### 속성에 따른 수평 정렬

margin-right: auto : 왼쪽 정렬



margin-right: auto; margin-left: auto; : 수평정렬



### inline

inline의 기본 너비는 컨텐츠 영역만큼 -> 너비, 높이, margin-top, margin-bottom 지정 불가



### display

- display: inline-block
  - inline처럼 한 줄에 표시 가능하고, block처럼 width, height, margin 속성을 모두 지정할 수 있음
- display: none
  - 해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
  - visibility: hidden은 해당 요소가 공간은 차지하나 화면에 표시만 하지 않는다



## CSS Position

- 문서 상에서 요소의 위치를 지정
- static : 모든 태그의 기본 값
  - 일반적인 요소의 배치 순서에 따름(좌측 상단)
  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨
- 아래는 좌표 프로퍼티(offset; top, bottom, left, right)을 사용하여 이동 가능
- relative : 상대 위치
  - 자기 자신의 static 위치를 기준으로 이동(normal flow 유지)
  - 외출 -> 나머지 요소는 원래 자리 유지함
- absolute : 절대 위치
  - normal flow에서 벗어남
  - static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동(없는 경우 body)
  - 집 나감 -> 나머지 요소가 그 자리 차지함

- fixed : 고정 위치
  - normal flow에서 벗어남
  - 부모 요소와 상관없이 viewport를 기준으로 이동
    - 스크롤 시에도 항상 같은 곳에 위치함
    - 예시: 맨 위로 올라가는 버튼




### CSS 원칙 ★

- CSS 원칙 Ⅰ,Ⅱ : Normal flow
  - 모든 요소는 네모(박스모델), 좌측상단에 배치
  - display에 따라 크기와 배치가 달라짐
- CSS 원칙 Ⅲ
  - **position으로 위치의 기준을 변경**
    - relative : 본인의 원래 위치
    - absolute : 특정 부모의 위치
    - fixed : 화면의 위치



## 추가 컨텐츠



## 마무리



## Practice



## Box Position



## Card Styling

