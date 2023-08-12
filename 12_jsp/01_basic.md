# JSP 기본 정리

[toc]

## JSP란

- 자카르타 서버 페이지(Jakarta Server Pages, JSP)
- HTML내에 자바 코드를 삽입하여 웹 서버에서 동적으로 웹 페이지를 생성하여 웹 브라우저에 돌려주는 서버 사이드 스크립트 언어
- JSP가 하나의 JAVA클래스이기 때문에 모든 JAVA 라이브러리를 끌어다 쓸 수 있음



## JSP 용어

예시

```jsp
<%@ page language="java" contentType="text/html; charset=EUC-KR" pageEncoding="EUC-KR"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=EUC-KR">
        <title>Insert title here</title>
    </head>
    <body>
        <%! 
    		public int sum(int num1, int num2) {
    			return num1 + num2;
			}
    	%>
        <% 
        	int num1 = 20;
        	int num2 = 10;
        	int sum = num1 + num2;
        %>
        <%=sum %>
    </body>
</html>
```



### 스크립트릿(Scriptlet)

```jsp
<% %>
```

- JSP 문서 안에 JAVA 코드를 넣기 위해 사용

-  HTML 코드와 섞어서 사용해도 오류 발생 x

  ```jsp
  <table>
      <% for (int a=0; a<10; a++ { %>
      	<tr><td>
              <% a %>
          </td></tr>
      	<% } %>
  </table>
  ```

  - 한줄 한줄 감싸줘야함



### 표현식(Expression)

```jsp
<%= %>
```

- 웹 브라우저에 결과값을 출력하기 위해 사용

- 단일연산 결과를 바로 출력할 때 사용 가능

  ```jsp
  <%= 10 + 20 %>
  <%= request.getParameter("파라미터명") %>
  ```

  - `<%= %>`내부에 `;`을 찍지 않도록 주의



### 선언문(Declartion)

```jsp
<%! %>
```

- 변수 선언이나 메소드를 선언하여 사용

  ```jsp
  <%! public int a=10 %>
  <%! public static int a=10 %>
  <%! public final int A=10 %>
  <%! public void sum() {
      ...
  	}
  %>
  ```

  

### 지시자(Directive)

```jsp
<%@ %>
```

- JSP 페이지의 전체적인 환경 설정을 할 때(문서의 종류와 인코딩 방식을 지정) 사용
- `contentType` : 브라우저로 내보내는 내용의 MIME 형식 지정 및 문자집합 지정
- `import` : 현재 JSP 페이지에서 사용할 Java 패키지나 클래스를 지정
- `errorPage` : 에러가 발생할 때에 대신 호출되어 처리될 JSP 페이지 지정



### 주석

```jsp
<!-- -->
```



##  JSP 내장 객체

- 스크립트릿(`<% %>`) 안에서만 사용할 수 있는 객체
- 개발자가 별도로 생성하지 않아도 JSP에서 바로 생성할 수 있는 객체
  - 컨테이너가 JSP를 서블릿으로 변환할 때 자동으로 객체 생성



**종류**

| 변수 이름   | 제공하는 기능 / 변수의 역할                               |
| ----------- | --------------------------------------------------------- |
| request     | doGet, doPost 메서드의 첫 번째 파라미터와 동일한 역할     |
| response    | doGet, doPost 메서드의 두 번째 파라미터와 동일한 역할     |
| out         | 웹 브라우저로 HTML코드를 출력하는 기능                    |
| application | JSP 페이지가 속하는 웹 애플리케이션에 관련된 기능         |
| config      | JSP 페이지의 구성 정보를 가져오는 기능                    |
| pageContext | JSP 페이지 범위 내에서 사용할 수 있는 데이터 저장 기능 등 |
| Session     | 세션에 관련된 기능                                        |
| Page        | JSP 페이지로부터 생성된 서블릿                            |
| Exception   | 익셉션 객체                                               |

