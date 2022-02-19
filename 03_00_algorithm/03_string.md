# 문자열(String)

[toc]



## 문자열

### 문자의 표현

- 각 문자에 대해서 대응되는 숫자를 정해놓고 이것을 메모리에 저장하는 방법 사용

- 영어 - 대소문자 합쳐서 52 -> 6(2^6=64가지) 비트면 모두 표현 가능 => 코드체계

  ex) 000000 -> 'a' / 000001 -> 'b'



- 미국에서 ASCII(American Standard Code for Information Interchange)라는 문자 인코딩 표준이 제정
- ASCII
  - 7bit 인코딩(0~127)
  - 128문자를 표현. 33개의 출력 불가능한 제어문자들, 공백을 비롯한 95개의 출력 가능한 문자들
  - 32번부터 출력 가능한 문자

- 확장 아스키
  - 부가적인 문자 128개 추가(128~255)
  - 8bit를 모두 사용함으로써 추가적인 문자를 표현할 수 있음
  - 서로 다른 프로그램이나 컴퓨터 사이에 교환되지 x
  - 프로그램이나 컴퓨터 또는 프린터가 그것을 해독할 수 있도록 설계되어 있어야만 올바로 해독 가능
- 오늘날 대부분의 컴퓨터는 문자를 읽고 쓰는데 ASCII형식을 사용
- 각 국가들은 자국의 문자를 표현하기 위하여 코드체계를 만들어서 사용
  - 우리나라 : 조합형, 완성형

- 다국어 처리를 위해 표준 마련 => 유니코드



- 유니코드도 다시 Character Set으로 분류됨

  - UCS-2

  - UCS-4

  - 유니코드를 저장하는 변수의 크기를 정의

  - but, 바이트 순서에 대해 표준화하지 못했음

  - 파일을 인식 시 이 파일이 UCS-2, UCS-4인지 인식하고 각 경우를 구분해서 모두 다르게 구현해야되는 문제 발생

    -> 유니 코드의 적당한 외부 인코딩이 필요하게 됨



- big-endian, little-endian
  - 8-bit = 1 Byte
  - 바이트 단위로 주소 가짐 
  - 0000 0000  0011 0000(00 30)에서 00과 30을 메모리 어디에, 누가 먼저 저장할 건지
  - bit-endian : 낮은 자리수를 높은 주소에 저장(0000 0030)
  - little-endian : 낮은 자리수를 빠른 자리에(0030 0000)



- 유니코드 인코딩 (UTF: Unicode Transformation Format)
  - UTF-8 (in web)
    - MIN : 8bit, Max : 32bit(1 Byte * 4)
  - UTF-16 (in windows, java)
    - MIN : 16bit, MAX : 32bit(2 Byte * 2)
  - UTF-32 (in unix)
    - MIN : 32bit, MAX : 32bit(4 Bytes * 1)



- Python 인코딩
  - 2.x 버전 - ASCII -> `#-*-coding: utf-8-*-` (첫 줄에 명시)
  - 3.x 버전 - 유니코드 UTF-8 -> 생략 가능
  - 다른 인코딩 방식으로 처리 시 첫 줄에 작성하는 위 항목에 원하는 인코딩 방식을 지정해주면 됨



- 문자열의 분류

  <img src="03_string.assets/화면 캡처 2022-02-16 094343.jpg" alt="문자열의 분류" style="zoom: 50%;" />

  - 파이썬은 java와 비슷함

- JAVA에서 String 클래스에 대한 메모리 배치 예

  - 문자열은 문자 자체말고도 그것을 처리하기 위한 다른 것들이 붙어서 더 큰 메모리 저장

- C언어에서 문자열 처리

  - 문자배열에 문자열을 저장할 때는 항상 마지막에 끝을 표시하는 널문자(`\0`)을 넣어줘야 함



- 참고

  - 다음 두 코드의 차이 이해하기

    ```python
    s1 = list(input())	# 123입력
    s2 = input()		# 123입력
    print(s1)
    print(s2)
    ```

    ['1', '2', '3']

    123

  - strlen() 함수 만들어보기

    def strlen(a): #'\0'을 만나면 '\0'을 제외한 글자수를 리턴

    ​	# while을 써서 함수 완성해보기

    ```python
    def mystrlen(s):
        i = 0
        while s[i] != '\0':
            i += 1
        return i	# '\0'을 만나면 while 끝남 -> i는 인덱스 => '\0'의 인덱스는 앞의 문자 개수를 나타냄
    
    a = ['a', 'b', 'c', '\0']
    print(mystrlen(a))
    ```

    3

    

- Java(객체지향 언어)에서의 문자열 처리
  - 문자열 데이터를 저장, 처리해주는 클래스를 제공
  - String클래스를 사용
  - 문자열 처리에 필요한 연산을 연산자, 메소드 형태로 제공



- Python에서의 문자열 처리
  - char 타입 없음(C에서는 자료형이 있어서 char 타입 있음)
  - 텍스트 데이터의 취급방법이 통일되어 있음
  - 문자열 기호
    - `'`, `"`, `'''`, `"""`
    - `+` 연결
      - 문자열 + 문자열 : 이어 붙여주는 역할
    - `*` 반복
      - 문자열 * 수 : 수만큼 문자열 반복
  - 문자열은 시퀀스 자료형으로 분류되고ㅡ, 시퀀스 자료형에서 사용할 수 있는 인덱싱, 슬라이싱 연산들을 사용할 수 있음
  - 문자열 클래스에서 제공되는 메소드
    - replace(), split(), isalpha(), find()
  - 문자열은 튜플과 같이 요소값을 변경할 수 없음(immutable)



- C와 Java의 String 처리의 기본적인 차이점

  - c는 아스키 코드로 저장

    ```c
    char * name = "홍길동";
    int count = strlen(name):
    ```

    

  - Java는 유니코드(UTF16, 2byte)로 저장
  
  - Python은 유니코드(UTF8)로 저장



### 문자열 뒤집기

- 자기 문자열에서 뒤집는 방법 or 새로운 빈 문자열을 만들어 소스의 뒤에서부터 읽어서 타겟에 쓰는 방법
- 자기 문자열을 이용할 경우 swap을 위한 임시 변수가 필요, 반복수행을 문자열 길이의 반만을 수행해야 함
  - 문자열 길이 9 -> 9 //2 = 4 => 4회 반복



- 뒤집는 방법
  - s = s[::-1]
  - s.reverse()    # string에서는 동작 안함



### 문자열 비교

- C : strcmp()함수를 제공

- Java에서는 equals() 메소드를 제공

  - 문자열 비교에서 ==연산은 메모리 참조가 같은지를 묻는 것

- Python에서는 ==연산자와 is 연산자를 제공

  - is는 참조를 비교함

  ```python
  s1 = 'abc'
  s2 = 'abc'
  s3 = 'def'
  s4 = s1
  s5 = s1[:2] + 'c'
  s6 = s1[:3]
  print(s1 == s2)		# True
  print(s1 is s2)		# True
  print(s1 == s5)		# True(내용을 비교)
  print(s1 is s5)		# False(내용은 같지만 참조는 달라서)
  print(s1 is s6)		# True
  ```

- 다음 C 코드를 참조해 문자열 비교함수를 만들어보자

  - 문자열이 같으면  0 리턴

  - str1이 str2보다 사전 순서상 앞서면 음수 혹은 -1 리턴

  - str1이 str2보다 사전 순서상 나중이면 양수 혹은 1 리턴

    ```c
    int my_strcmp(const char *str1, const char *str2)
    {
        int i  0;
        while(str1[i] != '\0')
        {
            if(str) != str2[i]) break;
            i++;
        }
        return (str1[i] - str2[i]);
    }
    ```

    ```python
    a = 'ab'
    b = 'abc'
    c = 'de'
    d = 'Abc'
    
    print(a<b)		# Ture (사전상 빠르기 때문)
    print(a>b)		# False
    print(a<c)		# True
    print(a>c)		# False
    print(a<d)		# False
    print(a==d)		# False
    ```

    ```python
    def my_strcmp(s1, s2):
        if s1 < s2:
            return -1
        elif s1 > s2:
            return 1
        else:
            return 0   
    ```



- 문자열 숫자를 정수로 변환하기
  - c언어에서는 atoi()함수를 제공. 역 함수로는 itoa()
  - java에서는 숫자 클래스의 parse 메소드를 제공
    - ex) Inetger:parselInt(String)
    - 역함수로는 toString()
  - python에서는 숫자와 문자변환 함수를 제공함
    - int('123'), float('3.14'), str(123), repr(123)



- int()와 같은 atoi()함수 만들기

  ```python
  def atoi(s):
      i = 0
      for x in s:
          i = i * 10 + ord(x) - ord('0')		# ord() : 아스키코드 리턴
          # ord('0') = 48, ord('1') = 49
      return i
  ```

  input이 123일 때

  i = 0*10 + 49 - 48 = 1

  i = 1 * 10 + 50 - 48 = 12

  i = 12 * 10 + 51 - 48 = 123



## 패턴 매칭

- 패턴 매칭에 사용되는 알고리즘들
  - 고지식한 패턴 검색 알고리즘 -> 인덱스 연산으로 반드시 할 수 있어야 함
  - 카프-라빈 알고리즘
  - KMP 알고리즘
  - 보이어-무어 알고리즘



#### !!!!!!!!!!!!!!!!!!!!!!!!다시 읽어보기

### 고지식한 알고리즘(Brute Force)



- 본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 일일이 비교하는 방식으로 동작

  ```pseudocode
  for i: 0 -> N-M(N은 비교 텍스트, M은 패턴 텍스트)
  	for j: 0 -> M-1
  		t[i+j] p[j]를 비교
  	i == M
  ```

  ```python
  p = 'is'	# 찾을 패턴
  t = 'This is a book~!'	# 전체 텍스트
  M = len(p)	# 찾을 패턴의 길이
  N = len(t)	# 전체 텍스트의 길이
  
  def BruteForce(p, t):
      i = 0	# t의 인덱스
      j = 0	# p의 인덱스
      while j < M and i < N:
          if t[i] != p[j]:	# 불일치 했을 때
              i = i - j	# 이전 시작 위치로 되돌아감
              j = -1		# j는 초기화
          i = i + 1	# 불일치를 했건 일치를 했건 시행
          j = j + 1
      if j == M : return i - M	# 검색 성공
      else: return -1		#검색 실패(i == N까지 갔는데도 찾지 못함)
  ```

- 시간복잡도

  - 최악의 경우 시간복잡도는 텍스트의 모든 위치에서 패턴을 비교해야 하므로 O(MN)이 됨



### KMP 알고리즘

- 불일치가 발생한 텍스트 스트링의 앞 부분에 어떤 문자가 있는지를 미리 알고 있으므로, 불일치가 발생한 앞 부분에 대하여 다시 비교하지 않고 매칭을 수행
- 패턴을 전처리하여 배열 next[M] (lps라는 용어 사용하기도 함)을 구해서 잘못된 시작을 최소화함
  - next[M] : 불일치가 발생했을 경우 이동할 다음 위치
- 시간 복잡도 : O(M+N)
- 아이디어 설명
  - 텍스트에서 abcdabc까지는 매치되고, e에서 실패한 상황 패턴의 맨 앞의 abc와 실패 직전의 abc는 동일함을 이용할 수 있다
  - 실패한 텍스트 문자와 p[4]를 비교한다
  - 매칭에 실패했을 때 돌아갈 곳을 계산
  - 일치하면 i += 1, j += 1
  - 패턴의 맨 앞에서 불일치 하는 경우 : i += 1

```python
def kmp(t, p):
    N = len(t)
    M = len(p)
    lps = [0] * (M+1)	# 일치했을 때 이동할 인덱스때문에(?)
    # preprocessing
    j = 0	# 일치한 개수 == 비교할 패턴 위치
    lps[0] = -1
    for i in range(1, M):
        lps[i] = j			# p[i] 이전에 일치한 개수
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[M] = j
    # search
    i = 0	# 비교할 텍스트 위치
    j = 0	# 비교할 패턴 위치
    while i < N and j <= M:
        if j == -1 or t[i] == p[j]:		# 첫 글자가 불일치했거나, 일치하면
            i += 1
            j += 1
        else:				# 불일치
            j = lps[j]
        if j == M:			# 패턴을 찾을 경우
            print(i-M, end=' ')		# 패턴의 인덱스 출력
            j = lps[j]				# 다음 패턴을 찾기 위해 어디부터 시작해야 하는지
    print()
    return
            

t = 'zzzabcdabcdabcdefabcd'
p = 'abcdabcdef'
kmp(t, p)
t = 'AABAACAADAABAABA'
p = 'AABA'
kmp(t, p)
t = 'AAAAABAAABA'
P = 'AAAA'
kmp(t, p)
```



### 보이어-무어 알고리즘

- 오른쪽에서 왼쪽으로 비교
- 대부분의 상용 소프트웨어에서 채택하고 있는 알고리즘
- 패턴의 오른쪽 끝에 있는 문자가 불일치하고 이 문자가 패턴 내에 존재하지 않는 경우, 이동 거리는 무려 패턴의 길이만큼이 됨
- 오른쪽 끝에 있는 문자가 불일치하고 이 문자가 패턴 내에 존재할 경우



- 문자열 매칭 알고리즘 비교
  - 찾고자 하는 문자열 패턴의 길이 m, 총 문자열 길이 n
  - 고지식한 패턴 검색 알고리즘: O(mn)
  - 카프-라빈 알고리즘 : Θ(n) (Θ는 늘 이정도다 라는 뜻)
  - KMP 알고리즘 : Θ(n)
  - 보이어-무어 알고리즘
    - 앞의 두 매칭 알고리즘들의 공통점: 텍스트 문자열의 문자를 적어도 한번씩 훑음. 따라서 최선의 경우 Ω(n) (Ω는 잘 해봐야 이정도다 라는 뜻)
    - 보이어-무어 알고리즘은 텍스트 문자를 다 보지 않아도 됨
    - 발상의 전환 : 패턴의 오른쪽부터 비교
    - 최악의 경우 수행시간  :Θ(mn)
    - 입력에 따라 다르지만 일반적으로 Θ(n)보다 시간이 덜 듦





## 문자열 암호화

### 시저 암호(Caesar cipher)

- 알파벳을 일정한 문자수만큼 [평행이동] 시킴으로써 암호화를 행함
- 1만큼 평행이동했을 때 키 값 = 1



- 시저 암호문에 대한 전사공격
- 문자 변환표를 이용한 암호화(단일 치환 암호)
- 단일 치환 암호의 복호화
  - 복호화하기 위해서는 모든 키의 조합(key space)가 필요
- bit열의 암호화
  - 배타적 논리합(exclusive-or) 연산 사용



## 문자열 압축

- 다음과 같은 문자열이 있다. 저장소의 크기를 줄이며 정확한 정보를 저장하는 방법은?

  - Run-legnth encoding 알고리즘

  - ABBBBBBBA => A1B7A1

  - 좀 더 효율적이고 일반적인 압축방법은? -> 허프만 코딩 알고리즘





9386. 연속한 1의 개수

      ```python
      n = int(input())
      arr = list(map(int, input()))
      cnt = [0] * len(arr)
      max_cnt = 0
      
      for i in range(len(arr)):
          if arr[i] == 0:
              cnt[i] = 0
          elif arr[i] == 1:
              cnt[i] += 1
              if max_cnt < cnt[i]:
                  max_cnt = cnt[i]

9367. 점점 커지는 당근의 개수

      ```python
      n = int(input())
      arr = list(map(int, input().split()))
      cnt = 1
      max_cnt = 1
      for i in range(1, n):
          if arr[i-1] < arr[i]:
              cnt += 1
              if max_cnt < cnt:
                  max_cnt = cnt
          else:
              cnt = 1
      ```

      

고대 유적