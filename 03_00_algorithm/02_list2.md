# 배열 2 (Array 2)

[toc]



## 배열 : 2차원 배열

- 2차원 배열의 선언

  - 1차원 리스트를 묶어놓은 리스트
  - 2차원 이상의 다차원 리스트는 차원에 따라 index를 선언
  - 2차원 리스트의 선언 : 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함
  - python에서는 데이터 초기화를 통해 변수선언과 초기화가 가능함

  `arr = [[0, 1, 2, 3], [4, 5, 6, 7]]`

  | 0    | 1    | 2    | 3    |
  | ---- | ---- | ---- | ---- |
  | 4    | 5    | 6    | 7    |

  `arr[1][2]` = 6



- 참고 : 2차원 배열 입력받으려면

  ```python
  N = int(input())
  arr = [list(map(int, input().split())) for _ in range(N)]
  print(arr)
  ```

  input

  3

  1 2 3

  4 5 6

  7 8 9

  ```python
  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  ```

  

- 배열 순회
  - n x m 배열의 n*m개의 모든 원소를 빠짐없이 조사하는 방법



- 행 우선 순회

  <img src="02_list2.assets/화면 캡처 2022-02-14 103150.jpg" alt="행 우선 순회" style="zoom:50%;" />

  ```python
  # i 행의 좌표
  # j 열의 좌표
  for i in range(n):
      for j in range(m):
          arr[i][j]		# 필요한 연산 수행
  ```

  

- 열 우선 순회

  <img src="02_list2.assets/화면 캡처 2022-02-14 103940.jpg" alt="열 우선 순회" style="zoom:50%;" />

  ```python
  # i 행의 좌표
  # j 열의 좌표
  for j in range(m):		# 먼저 고정된 j가 열이기 때문에 열 우선순회 됨
      for i in range(n):
          arr[i][j]
  ```

  

- 지그재그 순회 -> 자주 쓰이지 x

  <img src="02_list2.assets/화면 캡처 2022-02-14 104129.jpg" alt="지그재그 순회" style="zoom:50%;" />

  ```python
  # i 행의 좌표
  # j 열의 좌표
  for i in range(n):
      for j in range(m):
          arr[i][j + (m-1-2*j) * (i%2)]	# i%2는 짝수 홀수행
          								# 짝수일 때는 j이므로 왼->오
              							# 홀수일 때는 m-1-j이므로 오->왼
  ```

  

  

  ※ 주의

  ```python
  arr = [[0]*3]*3	 # 이렇게 만들지 말 것 (why? 얕은 복사)
  print(arr)
  arr[0][1] = 1
  print(arr)
  ```

  ```python
  [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
  [[0, 1, 0], [0, 1, 0]. [0, 1, 0]]
  ```
  
  ↓ 해결
  
  ```python
  arr2 = [[0]*3 for _ in range(3)]	# [0]*3이 열, range(3)이 행
  print(arr2)
  arr[0][1] = 1
  print(arr2)
  ```
  
  ```python
  [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
  [[0, 1, 0], [0, 0, 0], [0, 0, 0]]
  ```
  
  



- 행렬을 0으로 둘러싸고 싶다면

  ```python
  N = int(input())
  arr1 = [0] list(map(int, input().split())) + [0]
  arr2 = [[0]*(N+1)] + [[0]+list(map(int, input().split()))+[0] for _ in range(N)] + [[0]*(N+2)]

​	

- 델타를 이용한 2차 배열 탐색

  - 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법
  - `arr[i][j]` 동서남북 살펴보고 싶을 때

  ```pseudocode
  arr[0...N-1][0...N-1]	# NxN 배열
  di[] <- [0, 0, -1, 1]	# 좌우상하. d : delta
  dj[] -< [-1, 1, 0, 0]
  for i: 0 -> N-1:
  	for j: 0 -> N-1:
  		for k in range(4):
  			ni <- i + di[k]
  			nj <- i + dj[k]
  			if 0 <= ni < N and 0 <= nj < N	# 유효한 인덱스면
  				test(arr[ni][nj])
  ```

  

- 전치 행렬 -> 자주 쓰임

  ```python
  # i : 행의 좌표, len(arr)
  # j : 열의 좌표, len(arr[0])
  arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]	# 3*3 행렬
  
  for i in range(3):
      for j in range(3):
          if i < j:
              arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
  ```
  
  <img src="02_list2.assets/화면 캡처 2022-02-14 140234.jpg" alt="전치 행렬" style="zoom:50%;" />





## 부분집합 생성

### 부분집합 합(Subset Sum) 문제

- 유한 개의 정수로 이루어진 집합이 있을 때, 이 집합의 부분집합 중에서 그 집합의 원소를 모두 더한 값이 0이 되는 경우가 있는지를 알아내는 문제
- 예를 들어 [-7, -3, -2, 5, 8]라는 집합이 있을 때, [-3, -2, 5]는 이 집합의 부분집합이면서 (-3)+(-2)+5=0 이므로 이 경우의 답은 참이 된다.



- 완전검색 기법으로 부분집합 합 문제를 풀기 위해서는, 우선 집합의 모든 부분집합을 생성한 후에 각 부분집합의 합을 계산해야 한다.
- 주어진 집합의 부분집합을 생성하는 방법에 대해 생각해보자.



### 부분집합의 수

- 집합의 원소가 n개일 때, 공집합을 포함한 부분집합의 수는 2^n개

  - 각 원소를 부분집합에 포함시키거나 포함시키지 않는 2가지 경우를 모든 원소에 적용한 경우의 수

  ```python
  bit = [0, 0, 0, 0]
  for i in range(2):
      bit[0] = i						# 0번째 원소
      for j in range(2):
          bit[1] = j					# 1번째 원소
          for k in range(2):
              bit[2] = k				# 2번째 원소
              for l in range(2):
                  bit[3] = 1			# 3번째 원소
                  print_subset(bit)	# 생선된 부분집합 출력
  ```



- 비트 연산자
  - `&` : 비트 단위로 AND 연산
  - `|` : 비트 단위로 OR 연산
  - `<<` : 피연산자의 비트 열을 왼쪽으로 이동
  - `>>` : 피연산자의 비트 열을 오른쪽으로 이동
  - 같은 비트 단위끼리 연산함
- `<<` 연산자
  - 1 << n : n번 비트가 1인 값. 원소가 n개일 경우 모든 부분집합의 수를 의미
- `&` 연산자
  - i & (i << j) : i 의 j번째 비트가 1인지 아닌지 검사



- 보다 간결하게 부분집합을 생성하는 방법

  ```python
  arr = [3, 6, 7, 1, 5, 4]
  
  n = len(arr)		# n : 원소의 개수
  
  for i in range(1<<n):					# 1<<n : 부분 집합의 개수
      for j in range(n):					# 원소의 수만큼 비트를 비교
          if i & (1<<j):					# i의 j번 비트가 1인 경우
              print(arr[j], end=", ")		# j번 원소 출력
      print()
  print()
  ```

  



## 바이너리 서치 (Binary Search)

### 검색

- 저장되어 있는 자료 중에서 원하는 항목을 찾는 작업
- 목적하는 탐색 키를 가진 항목을 찾는 것
  - 탐색 키(search key) : 자료를 구별하여 인식할 수 있는 키
- 검색의 종류
  - 순차 검색(sequential search)
  - 이진 검색(binary search)
  - 해쉬



### 순차 검색

- 일렬로 되어 잇는 자료를 순서대로 검색하는 방법
  - 가장 간단하고 직관적인 검색 방법
  - 배열이나 연결 리스트 등 순차구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용함
  - 알고리즘이 단순 but, 검색 대상의 수가 많은 경우에는 수행시간이 급격히 증가하여 비효율적
- 2가지 경우
  - 정렬되어 있지 않은 경우
  - 정렬되어 있는 경우



#### 정렬되어 있지 않은 경우

- 검색 과정

  - 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교하며 찾음
  - 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환
  - 자료주고의 마지막에 이를 때까지 검색 대상을 찾지 못하면 검색 실패

- 찾고자 하는 원소의 순서에 따라 비교회수가 결정됨

  - 첫 번재 원소를 찾을 때는 1번 비교, 두 번째 원소를 찾을 때는 2번 비교

  - 정렬되지 않은 자료에서의 순차 검색의 평균 비교 회수

    = (n+1)/2

  - 시간 복잡도 : O(n)

  ```pseudocode
  def sequentialSearch(a, n, key)
  	i <-0
  	while i < n and a[i] != key: # 항상 인덱스 범위 먼저 살펴봐야함(and는 앞이 거짓이면 뒤의 조건 살펴보지 않음)
  		i <- i+1
  	if i < n: return i
  	else: return -1
  ```
  
  ```python
  def unordered_sequential_search(numbers, target):
      pos = 0		# position
      found = False		# flag 변수
      while pos < len(numbers) and not found:
          if numbers[pos] == target:
              found = True
          else:
              pos += 1
      return found
  ```
  
  



#### 정렬되어 있는 경우

- 검색 과정

  - 자료가 오름차순으로 정렬된 상태에서 검색을 실시한다고 가정
  - 자료를 순차적으로 검색하면서 키 값을 비교
  - 원소의 키 값이 검색 대상의 키 값보다 크면 -> 찾는 원소 없음 -> 검색 종료

- 찾고자 하는 원소의 순서에 따라 비교회수가 결정됨

  - 정렬되어 있으므로, 검색 실패를 반환하는 경우 평균 비교 회수가 반으로 줄어듦
  - 시간 복잡도: O(n)

  ```pseudocode
  def sequentialSearch2(a, n, key)
  	i <- 0
  	while i < n and a[i] < key:
  		i <- i+1
  	if i < n and a[i] == key:
  		return i
  	else:
  		return -1
  ```
  
  ```python
  def ordered_sequential_search(numbers, target):
      pos = 0
      found = False
      stop = False
      while pos < len(numbers) and not found and not stop:
          if numbers[pos] == target:
              found = True
          else:
              if numbers[pos] > target:
                  stop = True
                  return found
              else:
                  pos += 1
      return found
  ```
  
  



### 이진 검색(Binary Search)

- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법

  - 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색범위를 반으로 줄여가면서 보다 빠르게 검색을 수행함

- 전제 조건 : 자료가 정렬된 상태

- 검색 과정

  - 자료의 중앙에 있는 원소 고름
  - 중앙 원소의 값과 찾고자 하는 목표 값을 비교
  - 목표 값이 중앙 원소의 값보다 작으면
    - 자료의 왼쪽 반에 대해서 새로 검색
  - 크다면
    - 오른쪽 반에 대해서 새로 검색을 수행

- 구현

  - 검색 범위의 시작점과 종료점을 이용하여 검색을 반복 수행
  - 이진 검색의 경우, 자료의 삽입이나 삭제가 발생했을 때 배열의 상태를 항상 정렬 상태로 유지하는 추가작업 필요

  ```python
  def binarySearch(a, N, key):
      start = 0
      end = N-1
      while start <= end:
          middle = (start + end) // 2
          if a[middle] == key:
              return True
          elif a[middle] < key:	# 살펴본 중앙값이 key보다 작다면
              end = middle - 1
          else:					# 살펴본 중앙값이 key보다 크다면
              start = middle + 1
      return False
  ```



- 재귀 함수 이용

  - 재귀함수에서 중요한 것 : base case(언제 종료할 것인가)
  
  ```python
  def binarySearch2(a, low, high, key):
      if low > high:
          return False
      else:
          middle = (low + high) // 2
          if key == a[middle]:
              return True
          elif key < a[middle]:
              return binarySearch2(a, low, middle-1, key)
          elif a[middle] < key:
              return binarySearch2(a, middle+1, high, key)
  ```
  
  ```python
  def recursive_binary_search(numbers: list, target: int):
      if len(numbers) == 0:
          return False
      med = len(numbers) // 2
      if numbers[mid] == target:
          return True
      if target < numbers[mid]:
          return recursive_binary_search(numbers[:mid], target)
      else:
          return recursive_binary_search(numbers[mid+1:], target)



## 선택 정렬 (Selection Sort) ★

### 인덱스

- Database 분야가 아닌 곳에서는 Look up table등의 용어를 사용하기도 함
- 배열을 사용한 인덱스
  - 대량의 데이터를 매번 정렬하면, 프로그램의 반응 느려짐
    -> 대량 데이터의 성능 저하 문제를 해결하기 위해 배열 인덱스를 사용



- 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식

- 정렬 과정(오름차순)

  - 주어진 리스트 중에서 최소값을 찾음
  - 그 값을 리스트의 맨 앞에 위치한 값과 교환
  - 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복

- 시간 복잡도

  - O(n^2) : 이중 for문을 쓰게 되므로

  ```pseudocode
  def SelectionSort(a[], n)
  	for i from 0 to n-2
  		a[i],..., a[n-1] 원소 중 최소값 a[k] 찾음
  		a[i]와 a[k] 교환
  ```

  ```python
  def selectionSort(a, N):
      for i in range(N-1):
          minIdx = i					# 임의로 잡아둔 최소값의 인덱스
          for j in range(i+1, N):		# 구간의 시작이 하나씩 늘어남
              if a[minIdx] > a[j]:
                  minIdx = j			# 더 작은 값 찾으면 인덱스 바꾸기
          a[i], a[minIdx] = a[minIdx], a[i]
  ```





## 셀렉션 알고리즘

- 저장되어 있는 자료로부터 K번째로 큰 혹은 작은 원소를 찾는 방법
  - 최소값, 최대값 혹은 중간값을 찾는 알고리즘
- 선택 과정
  - 정렬 알고리즘을 이용하여 자료 정렬
  - 원하는 순서에 있는 원소 가져오기



- K번째로 작은 원소를 찾는 알고리즘

  - k가 비교적 작을 때 유용
  - 시간 복잡도: O(kn)

  ```python
  def select(arr, k):
      for i in range(0, k):		# k-1번째까지만 하면 k번째로 작은 원소 찾을 수 있음
          minIndex = i
          for j in ragen(i+1, len(arr)):
              if arr[minIndex] > arr[j]:
                  minIndex = j
          arr[i], arr[minIndex] = arr[minIndex], arr[i]
      return arr[k-1]
  ```

  

| 알고리즘    | 평균 수행시간 | 최악 수행시간 | 알고리즘 기법 | 비고                                 |
| ----------- | ------------- | ------------- | ------------- | ------------------------------------ |
| 버블 정렬   | O(n^2)        | O(n^2)        | 비교와 교환   | 코딩 쉬움                            |
| 카운팅 정렬 | O(n+k)        | O(n+k)        | 비교환 방식   | n이 비교적 작을때만 가능             |
| 선택 정렬   | O(n^2)        | O(n^2)        | 비교와 교환   | 교환 횟수가 버블, 삽입 정렬보다 작음 |
| 퀵 정렬     | O(nlogn)      | O(n^2)        | 분할 정복     | 평균적으로 가장 빠름                 |
| 삽입 정렬   | O(n^2)        | O(n^2)        | 비교와 교환   | n의 개수가 작을 때 효과적            |
| 병합 정렬   | O(nlogn)      | O(nlogn)      | 분할 정복     | 연결리스트이 경우 가장 효율적        |

