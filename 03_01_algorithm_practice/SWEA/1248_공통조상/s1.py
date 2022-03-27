# SWEA 1248. 공통조상

import sys
sys.stdin = open('input.txt')

def subtree_cnt(v):                 # 서브트리의 크기 구하는 함수
    global cnt
    if v:                           # v(현재 살펴보는 정점)이 값을 갖고 있다면
        cnt += 1
        subtree_cnt(tree[v][0])
        subtree_cnt(tree[v][2])

T = int(input())

for tc in range(1, T+1):
    V, E, v1, v2 = map(int, input().split())    # V: 정점, E: 간선, v1, v2: 공통 조상 찾는 두 개의 정점
    tree = [[0, 0, 0] for _ in range(V+1)]      # 왼쪽 자식, 부모, 오른쪽 자식
    data = list(map(int, input().split()))
    for i in range(E):
        parent, child = data[i*2], data[i*2+1]
        if not tree[parent][0]:                 # 왼쪽 자식 자리가 비었다면
            tree[parent][0] = child             # 왼쪽 자식에 채워주기
        else:
            tree[parent][2] = child
        tree[child][1] = parent
    arr = set()                                 # 조상들 담을 set
    node1, MRCA = v1, v2                        # node1 : v1의 조상찾을 변수, MRCA: Most Recent Common Ancestor
    while tree[node1][1]:                       # 거슬러 올라가면서 조상들 set에 담음
        arr.add(tree[node1][1])
        node1 = tree[node1][1]
    while True:
        if tree[MRCA][1]:
            if tree[MRCA][1] in arr:            # v2의 조상 중에 set에 이미 담겨있는게 있다면 그게 공통조상
                MRCA = tree[MRCA][1]
                break
            else:
                MRCA = tree[MRCA][1]
    cnt = 0
    subtree_cnt(MRCA)
    # print(f'{node2}')
    print(f'#{tc} {MRCA} {cnt}')