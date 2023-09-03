# jQuery 기본 문법

[toc]

## 기본 문법

```javascript
$(선택자).동작함수1().동작함수2()
```

- `$` : 제이쿼리를 의미. 제이쿼리에 접근할 수 있게 해주는 식별자
  - 선택자를 이용하여 원하는 HTML 요소 선택
  - 동작함수를 정의하여 선택된 요소에 원하는 동작 설정



### jQuery $객체

```javascript
$()
```

- jQuery 객체를 반환



### 선택자

**jQuery 문법**

```javascript
$('#ssd')	// #id 선택자
$('.hdd')	// .class 선택자
$('h1')		// 요소 선택자
```



**javascript 문법**

```javascript
document.getElementById('ssd')
document.querySelectorAll('.hdd')
document.querySelector("p")
```



### jQuery 이벤트

- click() : 선택된 요소를 클릭하면 함수 실행

- dbclick() : 선택된 요소를 더블클릭하면 함수 실행

- mouseenter() : 마우스 포인터가 들어가면

- mouseleave() : 마우스 포인터가 떠나면

- mousedown() : 마우스 버튼을 누르면

- mouseup() : 마우스 버튼을 놓으면

- hover() : mouseenter() + mouseleave()

- foucus() : 양식 필드에 포커스가 있을 때

- blur() : 양식 필드가 포커스를 잃을 때

- on() : 선택한 요소에 대해 하나 이상의 이벤트 핸들러 연결

  ```javascript
  $('p').click(function() {	// <p>태그에서 클릭 이벤트 발생 시
      $(this).hide();			// 해당 <p>태그 숨김
  })
  
  $('#p1').hover(function() {
      alert('You entered p1');
  }, function() {
      alert('You now leave p1');
  });
  ```

  

#### 셀렉터 이벤트 등록

**HTML**

```html
<button id="b1" class="btn">Button1</button>
<button id="b2" class="btn">Button1</button>
<button id="b3" class="btn">Button1</button>
<button id="b4" class="btn">Button1</button>
```



**jQuery 문법**

```javascript
// jQuery는 여러개 요소 리스트일 경우 자동으로 순회해서 등록
$('.btn').on('click', function() { });
```

- `$()`로 반환된 jQuery객체는 jQuery전용 함수를 사용해야함

  ```javascript
  $("p").on("click", function() {
      $("#jq").css("border", "2px solid orange");
  });
  
  $("h1").text("Hello!");
  ```

  

**javascript 문법**

```javascript
// javascript는 하나의 요소마다 일일이 click 이벤트 등록해야함
const btn = document.querySelectorAll('.btn');
for (let i; i < btn.length; i++) {
    btn[i].addEventListener('click', function() { });
}
```

```javascript
document.querySelector("p").addEventListner("click", function() {
    document.querySelector("#jq").style.border = "2px solid orange";
})

document.querySelector("h1").textContent = "Hello!";
```



### jQuery 이팩트

1. 숨김/표시

   - hide()
   - show()
   - toggle()

   ```javascript
   // 인자를 설정하여 숨김/표시의 속도를 지정할 수 있음
   $('p').hide(1000);
   $('p').hide("slow");
   ```

2. 페이드

   - fadeIn()
   - fadeOut()
   - fadeToggle()
   - fadeTo() : 선택한 요소의 불투명도를 지정하여 페이딩을 지정

   ```javascript
   // $(selector).fadeTo(speed, opacity, callback);
   $("button").click(function() {
       $("#div1").fadeTo("slow", 0.15);
       $("#div2").fadeTo("slow", 0.4);
       $("#div3").fadeTo("slow", 0.7);
   });
   ```

3. 슬라이딩

   - slideDown()
   - slideUp()
   - slideToggle()

4. 애니메이션

   - animate()

   ```javascript
   $("button").click(function() {
       $("div").animate({left: '250px'});
   })
   ```

5. jQuery 중지

   - stop() :  모든 jQuery 이펙트에 대해 작용. 이펙트가 완료되기 전에 중지함

6. jQuery 콜백

   - 현재 효과가 완료된 후 콜백 함수가 실행됨

   ```javascript
   $('button').click(function() {
       $('p').hide("slow", function() {			// hide() 실행 완료 후
           alert('The paragraph is now hidden');	// alert를 띄움
       });
   });
   ```


7. jQuery 체이닝

	```javascript
	$("#list").find("li").eq(1).html("두 번째 아이템을 선택했어요!")
	```
	
	- `$()`함수는 자기자신 노드객체를 반환하기 때문에 체이닝 기법 사용 가능
	  1. id가 list인 요소를 반환
	  2. li요소를 find(찾고자 하는게 여러개일 경우 리스트로 반환)
	  3. eq는 노드리스트에서 인덱스가 인수인 것을 가져옴
	  4. html()은 innerHtml과 비슷. setter로서 사용됨



### jQuery HTML

1. GET

   - 내용을 가져오는 text(), html(), val() 메소드에는 인자 x
   - text() : 선택한 요소의 텍스트 내용을 반환
   - html() : 선택한 요소(HTML 마크업 포함)의 내용을 반환
   - val() : 양식 필드의 값(value 속성 값)을 반환

   ```javascript
   $('#btn1').click(function() {
       alert('Text: ' + $('#test').text());
   });
   $('#btn2').click(function() {
       alert('HTML: ' + $('#test').html());
   })
   ```

2. SET

   - 내용을 설정하는 메소드에 인자 있음
   - text()
   - html()
   - val()

   ```javascript
   $('#btn1').click(function() {
       $('#test1').text("Hello world!");
   });
   $('#btn2').click(function() {
       $('#test2').html("<b>Hello world!</b>");
   });
   $('#btn3').click(function() {
       $('#test3').val("Duck Duck");
   });
   ```

3. 추가

   - 선택한 요소의 앞 또는 뒤에 내용을 추가
   - append() : 선택한 HTML 요소 끝 부분에 내용을 추가 (선택한 요소 태그 안에 자식요소로 추가)
   - prepend() : 선택한 HTML 요소 시작 부분에 내용을 추가
   - after() : 선택한 HTML 요소 뒤에 내용을 추가 (선택한 요소 태그 밖 뒤에 형제 요소로 추가)
   - before() : 선택한 HTML 요소 뒤에 내용을 추가

4. 제거

   - remove() : 선택한 요소와 그 자식 요소 모두를 제거
   - empty() : 선택한 요소의 자식 요소를 제거

5. CSS 클래스 조작

   - addClass() : 선택한 요소에 하나 이상의 클래스를 추가
   - removeClass() : 선택한 요소에서 하나 이상의 클래스를 제거
   - toggleClass() : 선택한 요소에서 클래스 추가/제거 사이를 전환
   - css() : 스타일 속성을 설정하거나 반환



### Method

#### attr

```javascript
.attr()
```

- 요소(element)의 속성(attribute)의 값을 가져오거나 속성을 추가함



1. 속성 값 가져오기

   ```javascript
   .attr(attributeName)
   ```

   ```javascript
   $('div').attr('class');		// div 요소의 class 속성 값을 가져옴
   ```

2. 속성 추가

   ```javascript
   .attr(attributeName, value)
   ```

   ```javascript
   $('h1').attr('title', 'Hello');		// h1 요소에 title 속성 추가하고 값을 Hello로 함



#### parent

```javascript
.parent([selector])
```

- 어떤 요소의 부모 요소를 선택함
- selector가 없으면 바로 위에 존재하는 부모 요소 반환

예제

- `p`태그의 부모 요소 중 `div`의 색을 빨간색으로 만들기

  ```javascript
  $('p').parent('div').css('color', 'red');
  ```

  

#### closest

```javascript
.closest(selector)
```

- 어떤 요소의 부모 중 selector를 만족하는 가장 가까운 부모를 반환



#### siblings()

```javascript
.siblings([selector])
```

- 어떤 요소의 형제 요소를 선택



#### children

```javascript
.children([selector])
```

- 어떤 요소의 자식 요소를 선택함

예제

- ul 요소의 자식 요소 중 `ip`를 클래스 값으로 가지는 요소의 색을 빨간색으로 만들기

```html
<body>
    <ul>
        <li>Lorem</li>
        <li class="ip">Ipsum</li>
        <li>Dolor</li>
    </ul>
</body>

<script>
	$(document).ready( function() {
        $('ul').chilren('.ip').css('color', 'red');
    });
</script>
```



#### find

```javascript
.find(selector)
```

- 어떤 요소의 하위 요소 중 특정 요소를 찾을 때 사용

예제

- `h1` 요소의 하위 요소 중 `span` 요소 선택

  ```javascript
  $('h1').find('span')
  ```

  

### this

```javascript
$(this)
```

- 이벤트 핸들러 내에서 이벤트가 발생한 요소를 가리키는 역할

- javascript에서의 this와 jQuery에서의 this 차이

  | javascript                           | jQuery               |
  | ------------------------------------ | -------------------- |
  | 현재 실행 컨텍스트에서 참조되는 객체 | 이벤트가 발생한 요소 |
  | this                                 | $(this)[0]           |

예제

- 여러 버튼 중 클릭한 버튼만 text 변경하기

  ```html
  <button class="btn">1번</button>
  <button class="btn">2번</button>
  <button class="btn">3번</button>
  
  <script>
  	$('.btn').click(function() {
          console.log(this);		// 1
          console.log($(this));	// 2
          $(this).text('눌렀지롱');
      })
  </script>
  ```

  ```tex
  // 1(this)
  <button class="btn">1번</button>
  
  // 2($(this))
  S.fn.init [button.btn]
  	0: button.btn
      length: 1
      [[Prototype]]: Object(0)
  ```

  