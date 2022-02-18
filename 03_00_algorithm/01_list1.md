# List 1(Array 1) 개념

[toc]

## 알고리즘

유한한 단계를 통해 문제를 해결하기 위한 절차나 방법

- 의사코드(Pseudocode)와 순서도 -> 슈도코드 위주로 쓰게 됨

- 무엇이 좋은 알고리즘인가?
  1. 정확성
  2. 작업량 : 얼마나 적은 연산으로 원하는 결과를 얻어내는가
  3. 메모리 사용량 : 얼마나 적은 메모리를 사용하는가
  4. 단순성 : 얼마나 단순한가
  5. 최적성 : 더 이상 개선할 여지없이 최적화되었는가



- 알고리즘의 성능은 무엇을 측정하는가

  ex) 1부터 n까지 합을 구하는 문제

  1. 1+2+3+...+n-> n번의 연산
  2. n* (1 + n) / 2 -> 3번의 연산



- 알고리즘의 작업량을 표현할 때 **시간복잡도**로 표현
- **시간 복잡도(Time Complexity)**
  - 실제 걸리는 시간을 측정
  - 실행되는 명령문의 개수(연산의 횟수)를 계산



- **빅-오(O) 표기법(Big-O Notation)**

  ex) O(3n  + 2) = O(3n) = O(n)

  최고차항 3n만 선택 -> 계수 3제거

  ex) O(4) = O(1)



- O(1) > O(logn) > O(n) > O(nlogn) > O(n^2) > O(2^n) > O(n!)
  - 기가 = 10억



## 배열

- 배열이란 무엇인가
  - 일정한 자료형의 변수들을 하나의 이름을 열거하여 사용하는 자료구조
- 배열의 필요성
  - 일일이 다른 변수명을 이용하여 자료에 접근하는 것은 매우 비효율적
  - 하나의 선언을 통해 둘 이상의 변수를 선언할 수 있음
  - 다수의 변수로는 하기 힘든 작업을 배열을 활용해 쉽게 할 수 있음

- 1차원 배열의 선언

  - 별도의 선언 방법이 없으면 변수에 처음 값을 할당할 때 생성

    Arr = list()

    Arr = []

    Arr = [1, 2, 3]	# 선언과 할당을 동시에

    Arr = [0] * 10 -> 크기를 미리 정해놓고 사용하는게 더 빠르게 가능

- 배열 활용 예제: Gravity

  - 상자 높이 7 4 2 0 0 6 0 7 0
  - 각 숫자별로 오른쪽으로 나보다 작은 숫자 개수를 셈
  - 7 5 4 ... 중 가장 큰 값 찾기



## 정렬

- 2개 이상의 자료를 특정 기준에 의해 오름차순(작은 값부터 큰 값) 혹은 내림차순으로 재배열하는 것
- 키
  - 자료를 정렬하는 기준이 되는 특정 값
- 대표적인 정렬 방식의 종류
  - 버블 정렬
  - 카운팅 정렬
  - 선택 정렬
  - 퀵 정렬
  - 삽입 정렬
  - 병합 정렬



### 버블 정렬(Bubble Sort)

- 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식
  - 선택 정렬과 잘 구분할 것
- 정렬 과정(오름차순)
  - 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동
  - 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬됨
  - 교환하며 자리를 이동하는 모습이 물 위에 올라오는 거품 모양과 비슷해서 버블 정렬

- 시간 복잡도
  - O(n^2)

- [55, 7, 78, 12, 42]를 버블 정렬하는 과정(오름차순)

  - 첫 번째 패스 : 가장 큰 수를 맨 뒤로

    <u>55 7</u> 78 12 42

    7 <u>55 78</u> 12 42

    7 55 <u>78 12</u> 42

    7 55 12 <u>78 42</u>

    7 55 12 42 **78**

    비교할 기준 위치를 왼쪽으로 할지 오른쪽으로 할 지 결정

    -> 왼쪽이라면 0 ~ 3(n-2)

    j : 0 -> 3

    for j : -> 3

    ​	if arr[j] > arr[j+1]

    ​		arr[j] <- arr[j+1]	# 큰 수를 오른쪽으로 옮기기

    

  - 두 번째 패스

    <u>7 55</u> 12 42 **78**

    7 <u>55 12</u> 42 **78**

    7 12 5<u>5 42</u> **78**

    7 12 42 **55** **78**

    구간 0 -> n-1

    구간의 끝이 i라면 구간 결정 for i : n-1 -> 1

    for j : 0 -> i-1

    ​	if arr[j] > arr[j+1]

    ​		arr[j] <- arr[j+1]

    

  - 세 번째 패스

    <u>7 12</u> 42 **55** **78**

    7 <u>12 42</u> **55** **78**

    7 12 **42** **55** **78**

    구간 0 -> n-2

    

  - 네 번째 패스

    <u>7 12</u> **42** **55** **78**

    7 **12** **42** **55** **78**

  

- 배열을 활용한 버블 정렬

  슈도코드

  ```pseudocode
  BubbleSort(a, N)					# 정렬할 배열과 배열의 크기
      for i : N-1 -> 1				# 정렬될 구간의 끝
          for j : 0 -> i-1			# 비교할 원소 중 왼쪽 원소의 인덱스
              if a[j] > a[j+1]		# 왼쪽 원소가 더 크면
                  a[j] <-> a[j+1]		# 오른쪽 원소와 교환
  ```

  파이썬 코드

  ```python
  def BubbleSort(a, N):
      for i in range(N-1, 0, -1):		# 범위의 끝 위치
          for j in range(0, i):
              if a[j] > a[j+1]:
                  a[j], a[j+1] = a[j+1], a[j]
  ```

  

  

### 카운팅 정렬(Counting Sort)

- 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘

- 제한 사항

  - 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능

- 시작 복잡도

  - O(n + k) : n은 리스트 길이, k는 정수의 최대값

- [0, 4, 1, 3, 1, 2, 4, 1]을 카운팅 정렬하는 과정(범위 주어질 것)

- 1단계 ★

  DATA 			0 4 1 3 1 2 4 1

  COUNTS		0 0 0 0 0	# 처리하기 위한 별도의 저장 공간 마련

  COUNTS		1 3 1 1 2

  슈도코드

  ```pseudocode
  count = [0] * (m+1)	# m까지의 수가 주어질 때
  for i: 0 -> n-1
      count[data[i]] += 1
  ```

- 정렬된 집합에서 각 항목의 앞에 위치할 항목의 개수를 반영하기 위해 counts의 원소를 조정

  DATA 			0 4 1 3 1 2 4 1

  COUNTS		1 3 1 1 2	# 0 1 1 1 2 3 4 4

  COUNTS		1 4 5 6 8	# 1까지는 총 4개, 2까지는 총 5개 -> 누적된 개수 나타냄(**누적합**)

  ```pseudocode
  for i: 1 -> 4		# 저장할 자리 기준(밑의 줄 counts)
  	counts[i] += count[i-1] 
  ```

- count[1]을 감소시키고 Temp에 1을 삽입

  DATA 			0 4 1 3 1 2 4 **1**	# 뒤에서부터 앞으로 감

  COUNTS		1 **3** 5 6 8	# DATA 마지막 1의 자리를 잡아주므로 4-1이 되어서 3

  TEMP 			_ _ _ **1** _ _ _ _

  ```pseudocode
  for i: n-1 -> 0
  	counts[data[i]] --	# --는 하나 빼라는 소리
  	temp[counts[data[i]]] = data[i]
  ```

- counts[4]를 감소시키고 temp에 4를 삽입

  DATA 			0 4 1 3 1 2 **4** 1	

  COUNTS		1 3 5 6 **7**	

  TEMP 			_ _ _ 1 _ _ _ **4**

- count[2]를 감소시키고 temp에 2를 삽입

  DATA 			0 4 1 3 1 **2** 4 1	

  COUNTS		1 3 **4** 6 7	

  TEMP 			_ _ _ 1 **2** _ _ 4

  

```python
def Counting_Sort(A, B, k):
# A [] -- 입력 배열(1 to k) DATA
# B [] -- 정렬된 배열 TEMP
# C [] -- 카운트 배열 COUNTS

    C = [0] * (k+1)
    
    for i in range(0, len(A)):
        C[A[i]] += 1
        
    for i in range(1, len(C)):
        C[i] += C[i-1]
        
    for i in range(len(B)-1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
```



- 정렬 알고리즘의 특성을 다른 정렬들과 비교

  | 알고리즘    | 평균 수행시간 | 최악 수행시간 | 알고리즘 기법 | 비고                      |
  | ----------- | ------------- | ------------- | ------------- | ------------------------- |
  | 버블 정렬★  | O(n^2)        | O(n^2)        | 비교와 교환   | 코딩이 가장 손쉬움        |
  | 카운팅 정렬 | O(n+k)        | O(n+k)        | 비교환 방식   | n이 비교적 작을 때만 가능 |

  버블 정렬은 필수로 알고 있을 것.



## Baby-gin Game

- 설명
  - 0~9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가 연속적인 번호를 갖는 경우는 run, 3장의 카드가 동일한 번호를 갖는 경우를 triplet
  - 6장의 카드가 run과 triplet로만 구성된 경우 baby-gin
  - 6자리의 숫자를 입력 받아 baby-gin여부를 판단하는 프로그램을 작성



### 완전검색

- 완전 검색 방법은 문제의 해법으로 생각할 수 있는 모든 경우의 수를 나열해보고 확인하는 기법
- **Brute-force** 혹은 generate-and-test 기법이라고도 불림
- 모든 경우의 수를 테스트한 후, 최종 해법을 도출
- 일반적으로 경우의 수가 상대적으로 작을 때 유용함

- 수행 속도는 느림 but. 해답을 찾아내지 못할 확률이 작음
- 자격검정평가 등에서 주어진 문제를 풀 때, 우선 완전 검색으로 접근하여 해답을 도출한 후, 성능 개선을 위해 다른 알고리즘을 사용하고 해답을 확인하는 것이 바람직(실제로는 이렇게 하면 오래걸리긴 함)



### 완전 검색을 활용한 Baby-gin 접근

- 고려할 수 있는 모든 경우의 수 생성하기
  - 6개의 숫자로 만들 수 있는 모든 숫자 나열 (중복 포함)
  - 앞의 3자리와 뒤의 3자리를 잘라, run과 triplet 여부를 테스트하고 최종적으로 baby-gin 판단



- 순열 (Permutation)

  - 서로 다른 것들 중 몇개를 뽑아서 한 줄로 나열하는 것

  - 서로 다른 n개 중 r개를 택하는 순열 : **nPr**

    nPr = n * (n-1) * (n-2) * ... * (n-r+1)

  ex) {1, 2, 3}을 포함하는 모든 순열을 생성하는 함수

  ```python
  for i1 in range(1, 4):
      for i2 in range(1, 4):
          if i2 != i1:
              for i3 in range(1, 4):
                  if i3 != i1 and i3 != i2:
                      print(i1, i2, i3)

​		1 2 3

​		1 3 2

​		2 1 3

​		2 3 1

​		3 1 2

​		3 2 1



### 그리디 (Greedy Algorithm)

- 탐욕(Greedy) 알고리즘은 최적해를 구하는 데 사용되는 근시안적인 방법
- 여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 진행하여 최종적인 해답에 도달
- 각 선택의 시점에서 이루어지는 결정은 지역적으로는 최적
  but, 그 선택들을 계속 수집하여 최종적인 해답을 만들었다고 해서 그것이 최적이라는 보장은 없음
- 일반적으로, 머릿속에 떠오르는 생각을 검증 없이 바로 구현하면 Greedy 접근



- 동작 과정
  1. 해 선택 : 현재 상태에서 부분 문제의 최적 해를 구한 뒤, 이를 부분해 집합에 추가
  2. 실행 가능성 검사 : 문제의 제약 조건을 위반하지 않는지를 검사
  3. 해 검사 : 새로운 부분해 집합이 문제의 해가 되는지를 확인
     아직 전체 문제의 해가 완성되지 않았다면 1)의 해 선택부터 다시 시작



- 거스름돈 줄이기
  1. 해 선택 : 현재 고를 수 있는 가장 단위가 큰 동전을 하나 골라 거스름돈에 추가
  2. 실행 가능성 검사 : 거스름돈이 손님에게 내드려야 할 액수를 초과하는지 확인. 초과한다면 마지막에 추가한 동전을 거스름돈에서 빼고, 1번으로 돌아가서 현재보다 한 단계 작은 단위의 동전을 추가
  3. 해 검사 : 거스름돈을 확인해서 액수에 모자라면 다시 1번으로 돌아가서 거스름돈에 추가할 동전을 고름



- Baby-gin을 완전검색 아닌 방법으로 풀어보자

  - 6개의 숫자는 6자리의 정수 값으로 입력됨
  - counts 배열의 각 원소를 체크하여 run과 triplet 및 baby-gin 여부를 판단

  ```python
  arr = list(map(int, input().split()))	# 4 4 4 3 4 5로 입력했을 때
  arr = list(map(int, input()))	# 444345로 입력했을 때
  arr = [int(x) for x in input()]	# 4 4 4 3 4 5로 입력했을 때
  ```

  [4, 4, 4, 3, 4, 5]



- 풀이

  arr			4 4 4 3 4 5

  ​				0 1 2 3 4 5 6 7 8 9

  counts	_ _ _ _ 1 4 1 _ _ _ _ _

  ```pseudocode
  for i: 0 -> 9
  	counts[arr[i]] += 1
  ```

  ```pseudocode
  for i: 0 -> 9
  	counts[i] >= 3
  ```

  ```python
  num = 456789	# Baby Gin 확인할 6자리 수
  c = [0] * 12	# 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트
  				# if문을 한번 덜 쓰기 위해 12개로 늘려서 만들어 씀
  
  for i in range(6):
      c[num % 10] += 1	# 맨 오른쪽에 있는 숫자의 개수를 셈
      num //= 10	# 맨 오른쪽에 있는 숫자를 버리고 나머지 숫자 살펴봄
  ```

  수의 크기를 모를 때는 for문 대신

  ```python
  while num > 0:
      c[num % 10] += 1
      num //= 10
  ```

  ```python
  i = 0
  tri = run = 0
  while  i < 10:
      if c[i] >= 3:	# triplete 조사 후 데이터 삭제
          c[i] -= 3
          tri += 1
          continue
      # 위의 if문과 별개->elif대신 if
      if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:	# run 조사 후 데이터 삭제
          c[i] -= 1
          c[i+1] -= 1
          c[i+2] -= 1
          run += 1
          continue
      i += 1
      
  if run + tri == 2 : print('Baby Gin')
  else: print("Lose")
  ```



- 자주 실수하는 오답

  - 입력받은 숫자를 정렬한 후, 앞 뒤 3자리씩 끊어서 run 및 triplet을 확인하는 방법

    ex) [1, 2, 3, 1, 2, ,3]

    정렬하면 [1, 1, 2, 2, 3, 3]이 되어서 오히려 baby-gin 확인을 실패할 수 있음