# 큐(Queue)

[toc]

## 큐

- 큐의 특성
  - 선입선출구조(FIFO: First In First Out)

- 큐의 선입선출구조

  <img src="07_queue.assets/화면 캡처 2022-02-25 091449.jpg" alt="큐의 선입선출구조" style="zoom:50%;" />

- 큐의 기본 연산

  - 삽입 : enQueue
  - 삭제 : deQueue

  | 연산          | 기능                                                |
  | ------------- | --------------------------------------------------- |
  | enQueue(item) | 큐의 뒤쪽(rear 다음)에 원소를 삽입하는 연산         |
  | deQueue()     | 큐의 앞쪽(front)에서 원소를 삭제하고 반환하는 연산  |
  | createQueue() | 공백 상태의 큐를 생성하는 연산                      |
  | isEmpty()     | 큐가 공백상태인지를 확인하는 연산                   |
  | isFull()      | 큐가 포화상태인지를 확인하는 연산                   |
  | Qpeek()       | 큐의 앞쪽(front)에서 원소를 삭제 없이 반환하는 연산 |

  1. 공백 큐 생성
     - front : 마지막으로 삭제된 위치
     - rear : 마지막으로 저장된 위치
     - 최초엔 front, rear를 -1로 초기화
  2. 원소 삽입
     - rear += 1
  3. 원소 반환/삭제
     - front += 1



## 선형큐

- 1차원 배열을 이용한 큐
  - 큐의 크기 = 배열의 크기
  - front : 가장 마지막으로 꺼내진 위치
  - rear : 마지막으로 저장된 위치
- 상태 표현
  - 초기 상태 : front = rear = -1
  - 공백 상태 : front == rear
  - 포화 상태 : rear == n-1(n: 배열의 크기, n-1: 배열의 마지막 인덱스)



- 삽입 : enQueue(item)

  ```pseudocode
  def enQueue(item):
      global rear
      if isFull(): print('Queue_Full')
          else:
              rear <- rear + 1;		# 여기부터 밑에 두 줄만 있어도 됨
              Q[rear] <- item;
  ```

- 삭제 : deQueue()

  ```pseudocode
  def deQueue():
  	if(isEmpty()) then Queue_Empty();	# if(isEmpty대신 front == rear도 가능)
  	else{
  		front <- front + 1;
  		return Q[front];
  	}
  ```

- 공백상태 및 포화상태 검사 : isEmpty(), isFull()

  ```pseudocode
  def isEmpty():
  	return front == rear
  	
  def Full():
  return rear == len(Q) - 1
  ```

- 검색 : Qpeek()

  ```pseudocode
  def Qpeek():
  	if isEmpty():
  		print('Queue_Empty')
  	else:
  		return Q[front+1]
  ```



- 큐 규현

  ```python
  size = 4
  Q = [0] * size
  front = rear = -1
  
  def is_full():
      return rear == len(Q) - 1
  
  def is_empty():
      return rear == front
  
  def enQueue(item):
      global rear
      if is_full():
          print('Que is full')
      else:
          rear += 1
          Q[rear] = item
          
  def deQueue():
      global front
      if is_empty():
          print('Queue is empty')
      else:
          front += 1
          return Q.pop(0)
          # return Q[front]
      
  def Qpeek():
      global front
      if is_empty():
          print('Queue is empty')
      else:
          front += 1
          return Q[front]    
  ```

  

- 원형큐 구현

  ```python
  size = 4
  Q = [0] * size
  front = rear = -1
  
  def is_full():
      global front, rear
      return front == (rear + 1) % len(Q) ?????
  
  def is_empty():
      return rear == front
  
  def enQueue(item):
      global rear
      if is_full():
          print('Que is full')
      else:
          rear += 1
          Q[rear] = item
          
  def deQueue():
      global front
      if is_empty():
          print('Queue is empty')
      else:
          front += 1
          return Q.pop(0)
          # return Q[front]	# dQeek과 동일하게 해도 됨
      
  def Qpeek():
      global front
      if is_empty():
          print('Queue is empty')
      else:
          front += 1
          return Q[front]    
  ```



- 우선순위 큐

  ```python
  import queue
  q = queue.PriorityQueue()	# 잘 안씀 -> 힙으로 쓰게 됨
  ```

  ```python
  import heapq
  
  heap = [7, 2, 5, 3, 4, 6]
  
  print(*heap)	# 7 2 5 3 4 6
  heapq.heapify(heap)	# 2 3 5 7 4 6 (힙의 기본이 최소힙구조)
  ```

  



### 연습문제

> 큐를 구현하여 다음 동작을 확인
>
> 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
>
> 큐에서 세 개의 데이터를 차례로 꺼내서 출력
>
> 1, 2, 3이 출력되어야 함

```python
front = -1
reat = -1
Q = [0] * 10		# 크기는 문제 조건에 따라 달리할 것
rear += 1
Q[rear] = 1
front += 1
print(Q[front])
```



```python
def bfs(v):
    Q = [v]
    
    while Q:		# queue가 비어있기 전까지 어떤 행동을 반복
        Q.pop(0)
        if not visited[v]:
            visited[v] = 1	# 방문 체크
            for w in range(1, V+1):
                if G[v][w] == 1 and not visited[w]:
                    Q.append(w)
    
import sys
sys.stdin = open('input.txt')
V, E = map(int, input().split())
temp = list(map(int, input().split()))
G = [[0 for _ in range(V+1)] for _ in range(V+1)]
for i in range(len(temp)//2):
    G[temp[i*2]][temp[i*2+1]] = 1
    G[temp[i*2+1]][temp[i*2]] = 1
visited = [0] * (V+1)
bfs(0)
```

```python
def bfs(v):
    Q = [0] * V
    front = rear = -1
    rear += 1
    Q[rear] = v
    visited[v] = 1
    
    while front != rear:
        front += 1
        v = Q[front]
        for w in range(1, V+1):
            if G[v][w] == 1 and not visited[w]:
                rear += 1
                Q[rear] = w		# enQueue
                visited[w] = 1
```









### 선형 큐 이용시의 문제점

- 잘못된 포화상태 인식
  - 앞이 비어있어도 rear가 n-1이면 포화상태로 인식함



- 해결방법
  - 원형 큐 : 배열의 처음과 끝이 연결되어 원형 형태로 가정하고 사용



## 원형큐

- 1차원 배열을 사용하되, **논리적으로는** 배열의 처음과 끝이 연결되어 원형 형태의 큐를 이룬다고 가정하고 사용

- 초기 공백 상태

  - front = rear = 0

- index의 순환

  - front와 rear의 위치가 배열의 마지막 인덱스인 n-1가리킨 후
    -> 그 다음엔 처음 인덱스인 0으로 이동

  - 이를 위해 나머지 연산자 mod 사용

    rear <= (rear + 1) % Qsize

- front 변수

  - 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 둠

- 삽입 위치 및 삭제 위치

  |        | 삽입 위치             | 삭제 위치               |
  | ------ | --------------------- | ----------------------- |
  | 선형큐 | rear = rear + 1       | front = front + 1       |
  | 원형큐 | rear = (rear + 1) % n | front = (front + 1) % n |

- 공백상태 및 포화상태 검사 : isEmpty(), isFull()

  - 공백 상태 : front == rear

  - 포화 상태 : 삽입할 rear의 다음 위치 == 현재 front

    `(rear + 1) % n == front`



- 삽입 : enQueue(item)

  ```python
  def enQueue(item):
      global rear
      if isFull():		# (rear + 1) % n == front:
          print('Queue_Full')
      else:
          rear = (rear + 1) % len(cQ)		# cQ : 원형큐
          cQ[rear] = item
  ```

- 삭제 : deQueue(), delete()

  ```python
  def deQueue():
      global front
      if isEmpty():
          print('Queue_Empty')
      else:
          front = (front + 1) % len(cQ)
          return cQ[front]
  ```

  ```python
  def isEmpty():
      return front == rear
  
  def isFull():
      return (rear + 1) % len(cQ) == front
  ```

  



## 우선순위 큐

- 우선순위 큐의 특성
  - 우선순위를 가진 항목들을 저장하는 큐
  - FIFO순서 x -> 우선순위가 높은 순서대로
- 우선순위 큐의 적용 분야
  - 시뮬레이션 시스템
  - 네트워크 트래픽 제어
  - 운영체제의 테스크 스케줄링
- 우선순위 큐의 구현
  - 배열을 이용한 우선순위 큐
  - 리스트(링크드 리스트)를 이용한 우선순위 큐
- 배열을 이용하여 우선순위 큐
  - 가장 앞에 최고 우선순위의 원소가 위치하게 됨(트리구조 이용)



## 큐의 활용 : 버퍼

- 버퍼

  - 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역
  - 버퍼링 : 버퍼를 활용하는 방식 or 버퍼를 채우는 동작

- 버퍼의 자료 구조

  - 입출력 및 네트워크와 관련된 기능에서 이용
  - 순서대로 입력/출력/전달 -> 큐 활용

- 키보드 버퍼

  <img src="07_queue.assets/화면 캡처 2022-02-25 101949.jpg" alt="키보드 버퍼" style="zoom:50%;" />



- Queue를 이용하여 마이쮸 나눠주기 시뮬레이션





## BFS(Breadth First Search, 너비우선탐색)

- 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문

- 방문했던 정점을 시작점으로 해서 다시 인접한 정점들을 차례로 방문

  <img src="07_queue.assets/화면 캡처 2022-02-25 103444.jpg" alt="BFS 예제 그래프" style="zoom:50%;" />



- BFS 알고리즘

  ```python
  def BFS(G, v):				# 그래프 G, 탐색 시작점 v
      visited = [0] * (n+1)	# n: 정점의 개수
      queue = []				# 큐 생성
      queue.append(V)			# 시작점 v를 큐에 삽입(enQueue)
      while queue:			# 큐가 비어있지 않은 경우
          t = queue.pop(0)	# 큐의 첫 번째 원소 반환(deQue)
          if not visited[t]:	# 방문되지 않은 곳이라면
              				# (방문된 곳 다시 큐에 들어와도 무시)
              visited[t] = 1	# 방문한 것으로 표시
              # visit(t)		# 정점 t에서 할 일
          for i in G[t]:		# t와 연결된 모든 정점에 대해
              if not visited[i]:	# 방문되지 않은 곳이라면
                  queue.append(i)	# 큐에 넣기
  ```

  - BFS 구조
    - while 전
      - visited 배열 초기화
      - Q 생성
      - 시작점 enQueue
    - while 후 : 
      - deQueue
      - 방문 표시
      - 인접점 enQueue

  

  ↓ 방문한 곳 다시 Q에 넣지 않으려면(visited = Q에 줄 선 적이 있는지 없는지 확인)

  ```python
  def BFS(G, v, n):			# 그래프 G, 탐색 시작점 v
      visited = [0] * (n+1)	# n: 정점의 개수
      queue = []				# 큐 생성
      queue.append(V)			# 시작점 v를 큐에 삽입(enQueue)
      visited[v] = 1			# 시작점 방문 표시
      while queue:			# 큐가 비어있지 않은 경우
          t = queue.pop(0)	# 큐의 첫 번째 원소 반환(deQue)
          # visited[t](탐색 목표를 여기다 적어둘 것)
          for i in G[t]:		# t와 연결된 모든 정점에 대해
              if not visited[i]:	# 방문되지 않은 곳이라면
                  queue.append(i)	# 큐에 넣기
                  visited[i] = visited[t] + 1	# n으로 부터 1만큼 이동
                  # B: 2, E: 3이 됨 -> 깊이 알 수 있게 됨 
  ```

  BFS 구조

  - while 전
    - visited 배열 초기화
    - Q 생성
    - 시작점 enQueue
    - 시작점 방문 표시
  - while 후 : 
    - deQueue
    - 인접점 enQueue



## [미로탐색]

- 출발-도착 최소 이동거리

  ```pseudocode
  def BFS(G, v, n):			# G: 그래프, v: 탐색 시작점
      visited = [0] * (n+1)	# 정점의 개수
      queue = []				# 큐 생성
      queue.append(V)			# 시작점 v를 큐에 삽입
      visited[v] = 1
      while queue:			# 큐가 비어있지 않은 경우
          t = queue.pop(0)	# 큐의 첫 번째 원소 반환
          visit(t)
          # 현재 위치에서 해줄 일 작성(do(t))
          # 목적지인지 판단
          for i in G[t]:		# t와 연결된 모든 정점에 대해
              if not visited[i]:	# 방문되지 않은 곳이라면
                  queue.append(i)	# 큐에 넣기
                  visited[i] = visited[t] + 1	# n으로부터 1만큼    



- SWEA 5105. 미로의 거리 - BFS

  - 출구만 찾고 끝낼경우 or 최단거리 찾을 때 BFS가 유리
  - 출발지 좌표가 여러개여도 BFS로 풀이 가능 

  ```python
  def fstart(N):
      for i in range(N):
          for j in range(N):
              if maze[i][j] == 2:
                  return i, j
      return -1, -1
  
  def bfs(i, j, N):
      visited = [[0] * (N) for _ in range(N)]	# 미로의 크기만큼 생성
      queue = []
      queue.append(i, j)
      visited[i][j] = 1
      while queue:
          i, j = queue.pop(0)
          if maze[i][j] == 3:					# visit(t)에 해당하는 부분(밑의 줄까지)
              return visited[i][j] - 2		# 출발 , 도착 칸 제외
          for ji, jd in [[0, 1],[1, 0][0, -1],[-1, 0]]:	# i, j에 인접한 칸에 대해
              ni, nj = i + di, j + dj			# 주변 칸 좌표
              if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:	# 주변 칸 좌표이면서 미로를 벗어나지 않고, 인접(벽이 아님)
                  queue.append((ni, nj))
                  visited[ni][nj] = visited[ni][nj] + 1
      return 0	# 도착지를 찾지 못한 경우
                  
  
  T = int(input())
  for tc in range(1, T+1):
      N = int(input())
      maze = [list(map(int, iput())) for _ in range(N)]
      sti, stj = fstart(N)
      # bfs로 최단거리 찾기
      ans = bfs(sti, stj, N)
      print(f'#{tc} {ans}')
  ```



- SWEA 5105. 미로의 거리 - DFS

  ```python
  def fstart(N):
      for i in range(N):
          for j in range(N):
              if maze[i][j] == 2:
                  return i, j
      return -1, -1
  
  def dfs(i, j, N, c):	# c: 지나온 칸 수
      global minV
      if maze[i][j] == 3:	# 목적지에 도착하면 기존의 최소거리와 비교
          if minV > c:
              minV = c
      elif c > minV:
          return
      else:
          maze[i][j] = 1	# 지금 있는 자리 방문 체크(벽으로 메움)
          for di, dj in [[0,1], [1,0], [0, -1], [-1, 0]]:	# 주변 칸 검색
              ni, nj = i + di, j + dj
              if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1:
                  dfs(ni, nj, N, c+1)
          maze[i][j] = 0		# 돌아갈 때 왔던 길 초기화
  
  T = int(input())
  for tc in range(1, T+1):
      N = int(input())
      maze = [list(map(int, iput())) for _ in range(N)]
      sti, stj = fstart(N)
      minV = N * N
      # 재귀 dfs로 최단거리 찾기
      dfs(sti, stj, N, 0)		# 현재 위치부터 도착지까지 칸 수 세려면 0(출발 제외하려면 1)
      if minV == 10000:
          minV = 1
      print(f'#{tc} {minV - 1}')
  ```



- SWEA 4875. 미로의 거리 - DFS

  ```python
  def fstart(N):
      for i in range(N):
          for j in range(N):
              if maze[i][j] == 2:
                  return i, j
      return -1, -1
  
  def bfs(i, j, N):
      visited = [[0] * (N) for _ in range(N)]	# 미로의 크기만큼 생성
      queue = []
      queue.append(i, j)
      visited[i][j] = 1
      while queue:
          i, j = queue.pop(0)
          if maze[i][j] == 3:					# visit(t)에 해당하는 부분(밑의 줄까지)
              return 1
          for ji, jd in [[0, 1],[1, 0][0, -1],[-1, 0]]:	# i, j에 인접한 칸에 대해
              ni, nj = i + di, j + dj			# 주변 칸 좌표
              if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:	# 주변 칸 좌표이면서 미로를 벗어나지 않고, 인접(벽이 아님)
                  queue.append((ni, nj))
                  visited[ni][nj] = visited[ni][nj] + 1
      return 0	# 도착지를 찾지 못한 경우
  
  T = int(input())
  for tc in range(1, T+1):
      N = int(input())
      maze = [list(map(int, iput())) for _ in range(N)]
      sti, stj = fstart(N)
      
      ans = bfs(sti, stj, N)
      print(f'#{tc} {ans}')
  ```

  ```python
  def fstart(N):
      for i in range(N):
          for j in range(N):
              if maze[i][j] == 2:
                  return i, j
      return -1, -1
  
  def dfs(i, j, N):
      if maze[i][j] == 3:	# 목적지에 도착하면 기존의 최소거리와 비교
          return 1		# 찾으면 중단하는 경우
      else:
          maze[i][j] = 1	# 지금 있는 자리 방문 체크(벽으로 메움)
          for di, dj in [[0,1], [1,0], [0, -1], [-1, 0]]:	# 주변 칸 검색
              ni, nj = i + di, j + dj
              if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1:
                  if dfs(ni, nj, N):	# 이미 1이 return되면 1 return 해
                      return 1
                  
          return 0
  
  T = int(input())
  for tc in range(1, T+1):
      N = int(input())
      maze = [list(map(int, iput())) for _ in range(N)]
      sti, stj = fstart(N)
      minV = N * N
      # 재귀 dfs로 최단거리 찾기
      dfs(sti, stj, N)		# 현재 위치부터 도착지까지 칸 수 세려면 0(출발 제외하려면 1)
      ans = 0
      print(f'#{tc} {ans}')
  ```

  