# 스택2

[toc]

## 간단 정리

그래프 탐색

그래프 : 요소들을 연결

요소 : 정점(vertex), 노드(node)

요소를 연결한 선 : 간선(edge)

DFS(깊이우선탐색) Depth First Search : 그래프를 하나도 빠짐없이 탐색하는 방법

비선형탐색 방법을 쓰는 이유 : 2차원 배열로 보기 때문



## DFS

### DFS(깊이우선탐색)

- 깊이 : 시작 지점에서 가볼 수 있을 때까지 끝까지 가보는 것

- 그래프 구조(비선형구조) -> 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요
- 두 가지 방법
  - 깊이 우선 탐색(Depth First Search, DFS)
  - 너비 우선 탐색(Breadth First Search, BFS)



- 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색
  더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복
  결국 모든 정점을 방문하는 순회방법
  - 재귀
  - 반복
  - 스택 사용



### DFS 알고리즘

1. 시작 정점 v를 결정하여 방문
2. 정점 v에 인접한 정점중에서
   1. 방문하지 않은 정점 w가 있으면, 정점v를 스택에 push하고 정점 w를 방문.
      그리고 w를 v로 하여 다시 2를 반복
   2. 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2를 반복
3. 스택이 공백이 될 때까지 2를 반복

```pseudocode
visited[], stack[] 초기화
DFS(v)
	v 방문;
	visited[v] <- true;
	do {		# while True와 같은 기능
		if (v의 인접 정점 중 방문 안한 w 찾기)
			push(v);
			while(w) {
				w 방문;
				visited[w] <- true;
				push(w);
				v <- w;
				v의 인접 정점 중 방문 안한 w 찾기
			}
			v <- pop(stack);
	} while(v)
end DFS()
```



### DFS 예

- 초기 상태: 배열 visited를 False로 초기화하고, 공백 스택을 생성

1. 정점 a를 시작으로 깊이 우선 탐색을 시작
2. 정점 a를 방문하지 않은 정점 b, c가 있으므로 a를 스택에 push하고, 인점정점 b와 c 중에서 오름차순에 따라 b를 선택하여 탐색을 계속함
3. 정점 b를 방문하지 않은 정점 d, e가 있으므로 b를 스택에 push하고, 인점정점 d와 e 중에서 오름차순에 따라 d를 선택하여 탐색을 계속함
4. 정점 d에 방문하지 않은 정점 f가 있으므로 d를 스택에 push하고, 인점정점 f를 선택하여 탐색을 계속함
5. 정점 f를 방문하지 않은 정점 e, g가 있으므로 a를 스택에 push하고, 인점정점 e와 g 중에서 오름차순에 따라 e를 선택하여 탐색을 계속함
6. 정점 e에 방문하지 않은 정점 c가 있으므로 e를 스택에 push하고, 인점정점 c를 선택하여 탐색을 계속함
7. 정점 c에서 방문하지 않은 인접정점이 없으므로, 마지막 정점으로 돌아가기 위해 스택을 pop하여 받은 정점 e에 대해서 방문하지 않은 인접정점이 있는지 확인
8. 정점 e는 방문하지 않은 인접정점이 없으므로, 다시 스택을 pop하여 받은 정점 f에 대해서 방문하지 않은 인접정점이 있는지 확인
9. 정점 f에 방문하지 않은 정점 g가 있으므로 f를 스택에 push하고, 인접정점 g를 선택하여 탐색을 계속함
10. 정점 g에서 방문하지 않은 인접정점이 없으므로, 마지막 정점으로 돌아가기 위해 스택을 pop하여 받은 정점 f에 대해서 방문하지 않은 인접정점이 있는지 확인
11. 정점 c에서 방문하지 않은 인접정점이 없으므로, 마지막 정점으로 돌아가기 위해 스택을 pop하여 받은 정점 d에 대해서 방문하지 않은 인접정점이 있는지 확인
12. 정점 c에서 방문하지 않은 인접정점이 없으므로, 마지막 정점으로 돌아가기 위해 스택을 pop하여 받은 정점 b에 대해서 방문하지 않은 인접정점이 있는지 확인
13. 정점 c에서 방문하지 않은 인접정점이 없으므로, 마지막 정점으로 돌아가기 위해 스택을 pop하여 받은 정점 a에 대해서 방문하지 않은 인접정점이 있는지 확인
14. 현재 정점 a에 방문하지 않은 인접 정점이 없으므로 마지막 정점으로 돌아가기 위해 스택을 pop하는데, 스택이 공백이므로 깊이 우선 탐색을 종료





## 계산기

- 문자열로 된 계산식이 주어질 때, 스택을 이용하여 이 계산식의 값을 계산할 수 있다

- 문자열 수식 계산의 일반적 방법

  - **중위표기법(infix notation)** : 수식 평소에 표기하는 방법과 동일

    ex) A + B

  - **후위표기법(postfix notation)** : 연산자를 피연산자 뒤에 표기

    ex) AB+

- step1. 중위표기식의 후위표기식 변환 방법1

  - 수식의 각 연산자에 대해서 우선순위에 따라 괄호를 사용하여 다시 표현

  - 각 현산자를 그에 대응하는 오른쪽괄호의 뒤로 이동시킴

  - 괄호 제거

    ```pseudocode
    A*B-C/D
    1. ((A*B) - (C/D))
    2. ((AB(* (CD)/)-
    3. AB*CD/-
    ```

    | 토큰 | isp  | icp  |
    | ---- | ---- | ---- |
    | )    | -    | -    |
    | *, / | 2    | 2    |
    | +, - | 1    | 1    |
    | ()   | 0    | 3    |

    뭔소린지 1도 모르겠다(isp: 스택 안 / icp: 스택 밖)

- step1. 중위표기식의 후위표기식 변환 알고리즘(스택 이용)2
  1. 입력 받은 중위 표기식에서 토큰을 읽는다
  2. 토큰이 피연산자이면 토큰을 출력
  3. 토큰이 연산자일 때, 이 토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면 스택에 push
     그렇지 않다면 스택 top의 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 pop한 후 토큰의 연산자를 push
     만약 top에 연산자가 없으면 push



- step2. 후위 표기법의 수식을 스택을 이용하여 계산



## 백트래킹

- 해를 찾는 도중 '막히면' (즉, 해가 아니면) 되돌아가서 다시 해를 찾아 가는 기법
- 최적화(optimization) 문제와 결정(decision)문제를 해결할 수 있음
- 결정 문제 : 문제의 조건을 만족하는 해가 존재하는지의 여부를 yes 도는 no가 답하는 문제
  - 미로 찾기
  - n-Queen 문제
  - Map coloring
  - 부분 집합의 합(Subset Sum) 문제 등



### 미로 찾기

- 백트래킹과 깊이우선탐색과의 차이
  - 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임 (prunning 가지치기)
  - 깊이우선탐색이 모든 경로를 추적하는데 비해 백트래킹은 불필요한 경로를 조기에 차단
  - 깊이우선탐색을 가하기에는 경우의 수가 너무 많음
    n!가지의 경우의 수를 가진 문제에 대해 깊이우선탐색을 가하면 처리 불가능한 문제
  - 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 여전히 지수함수 시간(exponential time)을 요하므로 처리 불가능



- 모든 후보를 검사?
  - no

- 백트래킹 기법
  - 어떤 노드의 유망성을 점검한 후 유망하지 않다고 결정되면 그 노드의 부모로 되돌아가 다음 자식 노드로 감
  - 어떤 노드를 방문하였을 때, 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 하며, 반대로 해답의 가능성이 있으면 유망하다고 함
  - 가지치기 : 유망하지 않는 노드가 포함되는 경로는 더 이상 고려하지 않음
- 백트래킹을 이용한 알고리즘은 다음과 같은 절차로 진행
  - 상태 공간 트리의 깊이 우선 검색을 실시
  - 각 노드가 유망한지를 점검
  - 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색을 계속함



- 일반 백트래킹 알고리즘 (N-Queen)

  ```pseudocode
  def checknode(v):	# node
      if promising(v):	# 놓을 수 있는지 없는지 확인
          if there is a solution at v:
              wrtie the solution
          else:
              for u in each child of v:
                  checknode(u)
  ```

  



## [참고] 부분집합, 순열

### 부분집합 구하기

- 백트래킹 기법으로 powerset을 구해보자

  - n개의 원소가 들어있는 집합의 2^n개의 부분집합을 만들 때는, true 또는 false값을 가지는 항목들로 구성된 n개의 배열을 만드는 방법을 이용
  - 여기서 배열의 i번째 항목은 i번째의 원소가 부분집합의 값인지 아닌지를 나타내는 값이다.

- 각 원소가 부분집합에 포함되었는지를 loop 이용하여 확인하고 부분집합을 생성하는 방법

  ```python
  bit = [0, 0, 0, 0]
  for i in range(2):
      ...
  ```

- {1, 2, 3}의 부분집합의 표현

  ```python
  def bacttrack(a, k input):
      global MAXCANDIDATES
      c = [0] * MAXCANDIDATES
      
      if k == input:
          process_solution(a, k)	# 답이면 원하는 작업을 한다
      else:
          k += 1
          ncandidates = construct_candidates(a, k, input, c)
          for i in range(ncandidates):
              a[k] = c[i]
              bactrack(a, k, input)
  ```

  ```python
  def construct_candidates(a, k, input, c):
      c[0] = True
      c[1] = False
      return 2
  
  MAXCANDIDATES = 2
  NMAX = 4
  a = [0] * NMAX
  backtrack(a, 0, 3)
  ```



### 순열 구하기

- 백트래킹을 이용하여 순열 구하기

  ```python
  def bactrack(a, k, input):
      global MAXCANDIDATES
      c = [0] * MAXCANDIDATES
      
      if k == input:
          for i in range(1, k+1):
              print(a[i], end=' ')
          print()
      else:
          k += 1
          ncandidates = construct_candidates(a, k, input, c)	# 후보 넘겨주기
          for i in range(ncandidates):
              a[k] = c[i]
              backtrack(a, k, input)
  ```





#### 부분집합의 합

- {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 powerset 중 원소의 합이 10인 부분집합을 구하시오.

  - 집합 {1, 2, 3}의 원소에 대해 각 부분집합에서의 포함 여부를 트리로 표현

    ```python
    def f(i, n):	# i: 부분집합에 포함될지 결정할 원소의 인덱스, n: 전체 원소 개수
        if i == n:	# 한 개의 부분집합 완성
            # print(bit)
            for j in range(n):
                if bit[j]:
                    print(a[j], end=' ')
            print()
        else:
            bit[i] = 1
            f(i+1, n)
            bit[i] = 0
            f(i+1, n)
        return
    
    a = [1, 2, 3]
    bit = [0, 0, 0]	# 원소가 부분집합에 들어갈 수 있는지 없는지 체크
    f(0, 3)
    ```

    ```python
    def f(i, n, k):	# i: 부분집합에 포함될지 결정할 원소의 인덱스, n: 전체 원소 개수, k: 찾는 부분집합의 합
        if i == n:	# 한 개의 부분집합 완성
            # print(bit)
            s = 0
            for j in range(n):
                if bit[j]:
                    s += a[j]
            if s == k:	# 찾고자 하는 합이면
                for j in range(n):
                if bit[j]:
                    print(a[j], end=' ')    
            print()
        else:
            bit[i] = 1
            f(i+1, n, k)
            bit[i] = 0
            f(i+1, n, k)
        return
    
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]	# 원소가 부분집합에 들어갈 수 있는지 없는지 체크
    f(0, 10, 10)
    ```

  - i원소의 포함 여부를 결정하면 i 까지의 부분 집합의 합 si를 결정할 수 있음

  - si-1이 찾고자 하는 부분집합의 합보다 크면 남은 원소를 고려할 필요 없음

  - A[i] 원소를 부분 집합의 원소로 고려하는 개쥐 함수 (A는 서로 다른 자연수의 집합)

    ```pseudocode
    # i-1 원소까지 고려한 합s, 찾으려는 합 t
    
    f(i, N, s, t)
    	if s == t	# i-1원소까지의 합이 찾는 값이 경우
        	...
        elif i == N	# 모든 원소에 대한 고려가 끝난 경우
        	...
        elif s > t	# 남은 원소를 고려할 필요가 없는 경우
        	...
        else		# 남은 원소가 있고 s < t인 경우
        	subset[i] = 1
            f(i+1, N, s + A[i], t)	# i 원소 포함
            subset[i] = 0			# i 원소 미포함
            f(i_1, N, s, t)
    ```

    ```python
    # subset2
    def f(i, n, s, t):	# i: 부분집합에 포함될지 결정할 원소의 인덱스, n: 전체 원소 개수, s: 이전까지 고려된 원소의 합, t: 목표값
        global cnt
        cnt += 1
        if s == t:		# 목표값을 찾으면
            for j in range(N):
                if bit[j]:
                    print(a[j], end=' ')
            print()
        elif i == N:	# 더이상 고려할 원소가 없으면
            return 
        elif s > t:		# 고려한 원소의 합 s가 이미 목표를 초과한 경우
            return 
        else:
            bit[i] = 1
            f(i+1, n, s + a[i], t)
            bit[i] = 0
            f(i+1, n, s, t)
        return
    
    N = 10
    a = [x for x in range(1, N+1)]
    bit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]	# 원소가 부분집합에 들어갈 수 있는지 없는지 체크
    cnt = 0
    t = 10
    f(0, 10, t)	# 합이 10인 경우를 찾음
    print('cnt = ', cnt)
    ```

    

- 추가 고려 사항

  - 고려한 구간의 합 s / 남은 구간의 합 rs
    - s > t이면 중단 / s + rs < t(남은 원소의 합을 다 더해도 찾는 값 t미만인 경우 중단)

  ```python
  #subset3.py
  def f(i, n, s, t, rs):	# i: 부분집합에 포함될지 결정할 원소의 인덱스, n: 전체 원소 개수, s: 이전까지 고려된 원소의 합, t: 목표값
      global cnt
      cnt += 1
      if s == t:		# 목표값을 찾으면
          for j in range(N):
              if bit[j]:
                  print(a[j], end=' ')
          print()
      elif i == N:	# 더이상 고려할 원소가 없으면
          return 
      elif s > t:		# 고려한 원소의 합 s가 이미 목표를 초과한 경우
          return 
      elif s + rs < t:
          return
      else:
          bit[i] = 1
          f(i+1, n, s + a[i], t, rs-a[i])
          bit[i] = 0
          f(i+1, n, s, t, rs-a[i])
      return
  
  N = 10
  a = [x for x in range(1, N+1)]
  bit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]	# 원소가 부분집합에 들어갈 수 있는지 없는지 체크
  cnt = 0
  t = 10
  f(0, 10, t, sum(a))	# 합이 10인 경우를 찾음
  print('cnt = ', cnt)
  ```

  

#### 순열

- A[1, 2, 3]의 모든 원소를 사용한 순열

  ```python
  def f(i, n):
      if i == n:
          print(p)
      else:
          for j in range(i, n):	# 자기 자신부터 자리 바꿈
              p[i], p[j] = p[j], p[i]
              f(i+1, n)
              p[i], p[j] = p[j], p[i]
  
  p = [x for x in range(1, n+1)]
  n = 5
  f(0, n)
  ```

  



## 분할정복

- 설계 전략
  - 분할
  - 정복
  - 통합



- 거듭 제곱 : O(n)

  ```python
  def power(base, exponent):
      if base == 0:
          return 1
      result = 1	# base^0은 1이므로
      for i in range(exponent):
          result * = base
      retrun result
  ```

- 분할 정복 기반 알고리즘 : O(logn)

  - n이 짝수일 때 C^n = C^(n/2) * C^(n/2)

  - n이 홀수일 때 C^n = C^(n-1/2) * C^(n-1/2) * C

    ```python
    def power(base, exponent):
        if exponent == 0 or base == 0:
            return 1
        if exponent % 2:
            newbase = power(base, (exponent-1)/2)
            return (newbase * newbase) * base
        else:
            newbase = power(base, (exponent-1)/2)
            return (newbase * newbase) * base
    ```



### 퀵 정렬

- 임의의 원소를 기준으로 잡음

- 주어진 배열을 두 개로 분할하고, 각각을 정렬

  - 합병정렬과 동일?
  - 다른점1 : 합병정렬은 그냥 두 부분으로 나누는 반면, 퀵정렬은 분할할 때, 기준 아이템 중심으로 이보다 작은것은 왼편, 큰 것은 오른편에 위치
  - 다른점2: 각부분 정렬이 끝난 후, 합병정렬은 합병이란 후처리 작업이 필요 but, 퀵정렬은 필요하지 않음

- 알고리즘

  ```python
  def quick_sort(a, begin, end):
      if begin < end:
          p = partition(a, begin, end)	# 기준값 정함
          # 피봇 기준으로 왼쪽에 있는 애들끼리 다시 정렬
          quick_sort(a, begin, p-1)
          # 피봇 기준으로 오른쪽에 있는 애들끼리 다시 정렬
          quick_sort(a, p+1, end)
          
  def partition(a, begin, end):
      pivot = (begin + end) // 2
      l = begin
      r = end
      while l < r:
          # 피봇값보다 큰값까지 or l과 r이 만날 때까지
          while l < r and a[l] < a[pivot]:
              l += 1
          # 피봇값보다 작은 값까지 or l과 r이 만날 때까지
          while l < r and a[r] >= a[piviot]:
              r -= 1
          if l < r:
              if l == pivot:
                  pivot = r
                  a[l], a[r] = a[r], a[l]
      a[pivot], a[r] = a[r], a[pivot]	# r = l이니까 하나만 쓰면 됨
      return r	# 최종적으로 결정된 자리 인덱스를 반환함?????
  ```

  ```python
  a = [69, 10, 3, 2, 6, 5, 76, 9]
  quick_sort(a, 0, 7)
  print(a)
  ```

  

- 퀵정렬의 최악의 시간 복잡도는 O(n^2)
- 평균 복잡도는 nlogn



### 인접행렬 만들기

```python
'''
V = 7, E = 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
V, E = map(int, input().split())
arr = list(map(int, input().split()))
adj = [[0] * (V+1) for _ in range(V+1)]		# 인접행렬
adjList = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adj[n1][n2] = 1		# n1과 n2는 인접(이어져있음)
    adj[n2][n1] = 1		# 방향 표시가 없는 경우(무방향, 양방향)
    
    adjList[n1].append(n2)
    adjList[n2].append(n1)
```

adjList = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]

-> 각 인덱스과 그 안에 있는 요소가 서로 이어져있음



