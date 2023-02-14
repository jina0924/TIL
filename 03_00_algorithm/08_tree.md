# 트리

[toc]

## 트리

### 트리의 개념

- 비선형 구조
- 원소들 간에 1 : n 관계를 가지는 자료구조
- 원소들 간에 계층관계를 가지는 계층형 자료구조
- 상위 원소에서 하위 원소로 내려가면서 확장되는 트리(나무)모양의 구조



### 트리 정의

- 한 개 이상의 노드로 이루어진 유한 집합
  - 루트(root) : 노드 중 최상위 노드
  - 나머지 노드들
- T1, ..., TN은 각각 하나의 트리가 되며(재귀적 정의) 루트의 부 트리(subtree)라 함
- 정점
- 단말노드 or 잎(leaf)노드 : 맨 아래 노드



### 트리 용어 정리

<img src="08_tree.assets/화면 캡처 2022-03-16 092017.jpg" alt="트리 그림" style="zoom:65%;" />

- 노드(node) : 트리의 원소
  - 트리 T의 노드 : A, B, C, D, E, F, G, H, I , J, K
- 간선(edge) : 노드를 연결하는 선. 부모 노드와 자식 노드를 연결
- 루트 노드(root node) : 트리의 시작 노드
  - 트리 T의 루트 노드 : A
- 형제 노드(sibling node) : 같은 부모 노드의 자식 노드들
  - B, C, D는 형제 노드
- 조상 노드 : 간선을 따라 루트 노드까지 이르는 경로에 있는 모드 노드들
  - K의 조상 노드 : F, B, A
- 서브 트리(subtree) : 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리
- 자손 노드 : 서브 트리에 있는 하위 레벨의 노드
  - B의 자손 노드 : E, F, K



- 차수(degree)
  - 노드의 차수 : 노드에 연결된 자식 노드의 수
  - 트리의 차수 : 트리에 있는 노드의 차수 중에서 가장 큰 값
  - 단말 노드(leaf node) : 차수가 0인 노드. 자식 노드가 없는 노드



- 높이
  - 노드의 높이 : 루트에서 노드에 이르는 간선의 수
    - B의 높이 = 1, F의 높이 = 2 (루트에서 0으로 시작하는지 1로 시작하는지에 따라 약간 다름)
  - 트리의 높이 : 트리에 있는 노드의 높이 중에서 가장 큰 값. 최대 레벨
    - 트리 T의 높이 = 3



## 이진트리

- 모든 노드들이 2개의 서브트리를 갖는 특별한 형태의 트리
- 각 노드가 자식 노드를 **최대한 2개**까지만 가질 수 있는 트리
  - 왼쪽 자식 노드(left child node)
  - 오른쪽 자식 노드(right child node)
  - 자식이 없을수도, 한 쪽 자식만 있을 수 있음



### 이진트리 특성

- 레벨 i에서의 노드의 최대 개수는 2^i개
- 높이가 h인 이진 트리가 가질 수 있는 노드
  - 최소 개수 = (h+1)개
  - 최대 개수 = (2^(h+1) -1)개



### 이진트리 종류

- 포화 이진 트리(Full Binary Tree) ★
  - 모든 레벨에 노드가 포화상태로 차 있는 이진 트리
    - 높이 3일 때 -> 15개의 노드
  - 루트를 1번으로 하여 2^(h+1)-1까지 정해진 위치에 대한 노드 번호를 가짐

- 완전 이진 트리(Complete Binary Tree)
  - 높이가 h이고 노드 수가 n개일 때 (단,2^h <= n < 2^(h+1)-1), 포화 이진 트리의 노드 번호 1번부터 n번까지 빈자리 없는 이진 트리
  - 자식이 없을 수는 있지만 왼쪽이 비어있고 오른쪽에만 자식이 있을 순 없음
- 편향 이진 트리(Skewed Binary Tree)
  - 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진 트리



### 이진트리 순회(traversal)

> 트리에 특화된 탐색 방법

- 순회(traversal) : 트리의 각 노드를 중복되지 않게 전부 방문(visit)하는 것
  - 빠짐없이, 중복 없이
  - 트리의 노드들을 체계적으로 방문하는 것
- 트리는 비 선형 구조 → 선형구조에서와 같이 선후 연결 관계를 알 수 없음
- 3가지 기본적인 순회방법
  - 전위순회(preorder traversal) : VLR
    - 부모노드 방문 후, 자식노드를 좌, 우 순서로 방문
  - 중위순회(inorder traversal) : LVR
    - 왼쪽 자식노드, 부모노드, 오른쪽 자식노드 순으로 방문
  - 후위순회(postorder traversal) : LRV
    - 자식노드를 좌우 순서로 방문한 수, 부모노드로 방문



#### 전위 순회

- 수행 방법

  1. 현재 노드 n을 방문하여 처리 -> V
  2. 현재 노드 n의 왼쪽 서브트리로 이동 -> L
  3. 현재 노드 n의 오른쪽 서브트리로 이동 -> R

- 전위 순회 알고리즘

  ```pseudocode
  def preorder_traverse(T):
  	if T:
  		visit(T)
  		preorder_traverse(T.left)
  		preorder_traverse(T.right)
  ```

- 전위순회 예

  <img src="08_tree.assets/화면 캡처 2022-03-16 101300.jpg" alt="전위순회 예시 그림" style="zoom:50%;" />

  순서1 : T0 -> T1 -> T2

  순서2 : A -> B D (T3) -> C F G

  총 순서 : A B D E H I C F G



#### 중위 순회

- 수행 방법
  1. 현재 노드 n의 왼쪽 서브트리로 이동 : L
  2. 현재 노드 n을 방문하여 처리 : V
  3. 현재 노드 n의 오른쪽 서브트리로 이동 : R

- 중위 순회 알고리즘

  ```pseudocode
  def inorder_traverse(T):
  	if T:
  	inorder_traverse(T.left)
  	visit(T)					# 이부분이 전위 순회와 순서 다름
  	inorder_traverse(T.right)
  ```

- 중위 순회의 예

  <img src="08_tree.assets/화면 캡처 2022-03-16 101300-16473938841091.jpg" alt="중위 순회 예시 그림" style="zoom:50%;" />

  순서1 : T1 -> T0 -> T2

  순서2 : D B (T3) -> A -> F C G

  총 순서 : D B H E I A F C G





#### 후위 순회

- 수행 방법
  1. 현재 노드 n의 왼쪽 서브트리로 이동 : L
  2. 현재 노드 n의 오른쪽 서브트리로 이동 : R
  3. 현재 노드 n을 방문하여 처리 : V

- 후위 순회 알고리즘

  ```pseudocode
  def postorder_traverse(T):
  	if T:
  	postorder_traverse(T.left)
  	postorder_traverse(T.right)
  	visit(T)					# print(T.item)
  ```

- 후위 순회의 예

  <img src="08_tree.assets/화면 캡처 2022-03-16 101300-16473938841091.jpg" alt="후위 순회 예시 그림" style="zoom:50%;" />

  순서1 : T1 -> T2 -> T0

  순서2 : D (T3) B -> F G C -> A

  총 순서 : D H I E B F G C A

  - 루트가 가장 마지막에 처리됨



### 이진 트리의 표현

- 배열을 이용한 이진 트리의 표현
  - 이진 트리에 각 노드 번호를 다음과 같이 부여
  - 루트의 번호를 1로 함
  - 레벨 n에 있는 노드에 대하여 왼쪽부터 오른쪽으로 2^n부터 2^(n+1) - 1까지 번호를 차례로 부여
- 노드 번호의 성질
  - 노드 번호가 i인 노드의 부모 노드 번호 = i//2
  - 노드 번호가 i인 노드의 왼쪽 자식 노드 번호 = 2*i
  - 노드 번호가 i인 노드의 오른쪽 자식 노드 번호 = 2*i + 1
  - 레벨 n의 노드 번호 시작 번호 = 2^n(level 0 부터 시작할 때)
- 노드 번호를 배열의 인덱스로 사용(배열의 길이 = 노드 개수+1)
- 높이가 h인 이진 트리를 위한 배열의 크기 = 2^(h+1) -1



#### [참고] 이진 트리의 저장

- 부모 번호를 인덱스로 자식 번호를 저장

  - 간선의 개수 = 정점의 개수 - 1

  [일차원 배열]

  ```pseudocode
  for i : 1 -> N
  	read p, c
  	if (c1[p] == 0)
  		c1[p] = c
  	else
  		c2[p] = c
  ```

  ```python
  '''
  4
  1 2 1 3 3 4 3 5
  '''
  E = int(input())	# E: 간선의 개수
  arr = list(map(int, input().split()))
  V = E + 1			# V: 정점의 개수
  
  # 부모번호를 인덱스로 자식번호 저장
  ch1 = [0]*(V+1)		# 왼쪽 자식
  ch2 = [0]*(V+1)		# 오른쪽 자식
  for i in range(E):
      p, c = arr[i*2], arr[i*2+1]
      if ch1[p] == 0:	# 아직 자식이 없는 경우
          ch1[p] = c
      else:
          ch2[p] = c        
  ```

  ```python
  # 전위 순회
  def preorder(v):
      if v:	# 0번 정점이 없으므로 0번은 자식이 없는 경우를 의미
          print(v)	# visit(v)
          preorder(ch1[v])
          preorder(ch2[v])
  ```

  ```python
  # 중위 순회
  def inorder(v):
      if v:
          inorder(ch1[v])
          print(v)
          inorder(ch2[v])
  ```

  ```python
  # 후위 순회
  def postorder(v):
      if v:
          postorder(ch1[v])
          postorder(ch2[v])
          print(v)    
  ```

  ```python
  preorder(1)		# 1 2 3 4 5
  preorder(3)		# 3 4 5(subtree에서만 순회)
  inorder(1)		# 2 1 4 3 5
  postorder(3)	# 4 5 3
  postorder(1)	# 2 4 5 3 1
  ```

  

  [이차원 배열]

  ```python
  V = int(input())
  E = V - 1
  tree = [[0 for _ in range(3)] for _ in range(V+1)]	# 왼쪽, 오른쪽, 부모
  temp = list(map(int, input().split()))
  cnt = 0
  for i in range(E):
      parent, child = temp[i*2], temp[i*2+1]
      if not tree[parent][0]:
          tree[parent][0] = child
      else:
          tree[parent][1] = child
      tree[child][2] = parent
  print('전위 순회: ', end='')
  pre_order(1)
  print()
  
  ```

  ```python
  def preorder(node):
      global cnt
      if node != 0:
          cnt += 1
          print('{}'.format(node), end=' ' )
          preorder(tree[node][0])
          preorder(tree[node][1])
          
  def inorder(node):
      if node != 0:
          inorder(tree[node][0])
          print('{}'.format(node, end=' '))
          inorder(Tree[node][1])
          
  def postorder(node):
      if node != 0:
          postorder(tree[node][0])
          postorder(Tree[node][1])12
          print('{}'.format(node, end=' '))
  ```

  

- 자식 번호를 인덱스로 부모번호를 저장

  ```python
  par = [0]*(V+1)
  for i in range(E):
      p, c = arr[i*2], arr[i*2+1]
      par[c] = p
  
  '''
  4
  2 1 2 4 4 3 4 5
  '''
  print(*par)		# 0 2 0 4 2 4 -> root = 2
  # root 찾기
  root = 0
  for i in range(1, V+1):
      if par[i] == 0:
          root = 3
          break
  print(root)		# 2
  in_order(2)		# 1 2 3 4 5
  # 조상 찾기
  c = 5			# 정점 c의 조상 찾기
  anc = []
  while par[c] != 0:
      anc.append(par[c])
      c = par[c]
  print(*anc)		# 4 2
  ```

  

#### 이진트리의 표현 - 배열

- 배열을 이용한 이진 트리의 표현의 단점
  - 편향 이진 트리의 경우에 사용하지 않는 배열 원소에 대한 메모리 공간 낭비 발생
  - 트리의 중간에 새로운 노드를 삽입하거나 기존의 노드를 삭제할 경우 배열의 크기 변경 어려워 비효율적



#### 트리의 표현 - 연결리스트

- 위의 단점을 보완하기 위해 연결리스트를 이용하여 트리를 표현
- 연결 자료구조를 이용한 이진트리의 표현
  - 이진트리의 모든 노드는 최대 2개의 자식 노드를 가지므로 일정한 구조의 단순 연결 리스트 노드를 사용하여 구현



### 수식 트리

- 수식을 표현하는 이진 트리
- 수식 이진 트리(Expression Binary Tree)
- 연산자는 루트 노드 or 가지 노드(root와 leaf 중간)
- 피연산자는 모두 잎 노드
- 기본적으로 후위 순회를 이용



## 이진탐색 트리

- 탐색작업을 효율적으로 하기 위한 자료구조
- 모든 원소는 서로 다른 유일한 키를 가짐
- key(왼쪽 서브트리) < key(루트 노드) < key(오른쪽 서브트리)
- 왼쪽 서브트리와 오른쪽 서브트리도 이진탐색트리
- 중위 순회하면 오름차순으로 정렬된 값을 얻을 수 있음



### 이진 탐색 트리 - 연산

- 탐색 연산
  - 루트에서 시작
  - 탐색할 키 값 x를 루트 노드의 키 값과 비교
    - 키 값x = 루트노드의 키 값 : 원하는 원소 찾음
    - 키 값x < 루트노드의 키 값 : 루트노드의 왼쪽 서브트리에 대해서 탐색연산 수행
    - 키 값x > 루트노드의 키 값 : 루트노드의 오른쪽 서브트리에 대해서 탐색연산 수행
  - 서브트리에 대해서 순환적으로 탐색 연산 반복



- 삽입 연산
  1. 먼저 탐색 연산을 수행
     - 삽입할 원소와 같은 원소가 트리에 있으면 삽입x ->  같은 원소가 트리에 있는지 탐색
     - 탐색에서 탐색 실패가 결정되는 위치가 삽입 위치
  2. 탐색 실패한 위치에 원소를 삽입



### 이진 탐색 트리 - 성능

- 탐색, 삽입, 삭제 시간 - 트리의 높이 만큼 시간이 걸림
  - O(h), h : BST의 깊이(height)
- 평균의 경우
  - 이진 트리가 균형적으로 생성되어 있는 경우
  - O(log n)
- 최악의 경우
  - 한쪽으로 치우친 경사 이진트리의 경우
  - O(n)
  - 순차탐색과 시간복잡도가 같음

- 검색 알고리즘 비교



### 이진 탐색 트리 - 연산 연습

- 삭제 연산
  - 연결 리스트로 해야 쉽게 풀릴 것



## 힙(heap)

- 완전 이진 트리에 있는 노드 중에서 키 값이 가장 큰 노드나 키 값이 가장 작은 노드를 찾기 위해서 만든 자료구조

- 최대 힙(max heap)

  - 키 값이 가장 큰 노드를 찾기 위한 완전 이진 트리
  - 부모노드의 키 값 > 자식 노드의 키 값
  - 루트 노드 : 키 값이 가장 큰 노드

- 최소 힙(min heap)

  - 키 값이 가장 작은 노드를 찾기 위한 완전 이진 트리
  - 부모노드의 키 값 < 자식 노드의 키 값
  - 루트 노드 : 키 값이 가장 작은 노드

  

### 힙 연산 - 삽입

```python
'''
최대 100개의 정수가 키로 입력
최대힙
'''
def enq(n):
    global last
    last += 1
    tree[last] = n		# 완전이진트리 유지
    c =last				# 새로 추가된 정점을 자식으로
    p = c//2			# 완전이진트리에서 부모 정점 번호
    while p >= 1 and tree[p] < tree[c]:	# 부모가 있고, 자식의 키 값이 더 크면 교환
        tree[p], tree[c] = treee[c], tree[p]
        c = p
        p = c//2

# 포화이진트리의 정점 번호 1~100
tree = [0] * 101
last = 0		# 마지막 정점 번호
enq(3)
enq(2)
enq(4)
enq(7)
enq(5)
enq(9)
print(tree[1])	# 9
```



### 힙 연산 - 삭제

- 힙에서는 루트 노드의 원소만을 삭제할 수 있음
- 루트 노드의 원소를 삭제하여 반환
- 힙의 종류에 따라 최대값 또는 최소값을 구할 수 있음
  1. 루트 노드의 원소 삭제
  2. 마지막 노드 삭제해서 루트에 자리잡음
  3. 삽입 노드 < 자식노드 : 자리바꾸기
  4. 자리 확정

```python
def deq():
    global last
    tmp = tree[1]			# 루트의 key값
    tree[1] = tree[last]	# 마지막 정점의 키를 루트에 복사
    last -= 1				# 마지막 정점 삭제
    # 부모 > 자식 규칙 유지
    p = 1
    c = p*2					# 왼쪽 자식 노드 번호
    while c <= last:		# 왼쪽 자식이 있으면
        if c + 1 <= last and tree[c] < tree[c+1]:	# 오른쪽 자식 노드도 있고 더 크면
            c += 1			# 오른쪽 자식 선택
        if tree[p] < tree[c]:	# 자식의 키 값이 더 크면 교환
            tree[p], tree[c] = tree[c], tree[p]
            p = c
            c = p * 2
        else:
            break
    return tmp

while last > 0:
    print(deq(), tree[1])
```

- 힙의 키를 우선순위로 활용하여 우선순위 큐를 구현할 수 있음



- 완전이진트리에서의 순회

  ```python
  def preorder(v):
      global last
      if v <= last:	# 마지막 정점번호 이내
          print(v)	# visit(v)
          preorder(v*2)	# 왼쪽 자식 정점 방문
          preorder(v*2+1)	# 오른쪽 자식 정점 방문
  ```

  

```python
def heap_push(value):
    global heap_count
    heap_count += 1
    heap[heap_count] = value
    child = heap_count
    parent = child //  2
    
    while parent and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child // 2
    
def heap_pop():
    global heap_count
    return_value = heap[1]
    heap[1] = heap[heap_count]
    heap[heap_count] = 0
    heap_count -= 1
    
    parent = 1
    child = parent * 2	# 왼쪽 자식
    
    if child + 1 <= heap_count:				# 오른쪽 자식이 있는지
        if heap[child] > heap[child+1]:		# 왼쪽 자식이 더 크다면
            child = child + 1				# 오른쪽 자식으로 비교할 것
            
    while child <= heap_count and heap[parent] > heap[child]:	# 자식이 존재하는지 & 
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent * 2
        
        if child + 1 <= heap_count:
            if heap[child] > heap[child + 1]:
                child = child + 1
    return return_value
    
heap_count = 0
nums = [7, 2, 5, 3, 4, 6]
N = len(nums)
heap = [0] * (N+1)    
    
for i in range(N):
    heap_push(nums[i])
print(*heap)

for i in range(N):
    print(heap_pop(), end=' ')