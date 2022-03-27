# SWEA 5174. subtree

import sys
sys.stdin = open('input.txt')

def subtree(node):
    global cnt
    cnt += 1                                    # 함수로 넘겨받은 매개변수부터 subtree의 시작이므로 cnt에 1 더해줌
    if tree[node][0]:                           # 왼쪽 자식이 있다면 그걸 부모로 하는 subtree로 감
        subtree(tree[node][0])
    if tree[node][2]:                           # 오른쪽 자식이 있다면 그걸 부모로 하는 subtree로 감
        subtree(tree[node][2])
    if not tree[node][0] and not tree[node][2]: # 자식이 없다면 함수끝냄
        return

T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())            # E: 간선의 개수, N: subtree의 부모 노드
    V = E + 1                                   # V: 정점의 개수
    tree = [[0, 0, 0] for _ in range(V+1)]      # 인덱스 0: 왼쪽자식 / 인덱스 1: 부모 / 인덱스 2: 오른쪽 자식
    arr = list(map(int, input().split()))
    for i in range(E):
        parent, child = arr[i*2], arr[i*2+1]
        tree[parent][1] = parent
        if not tree[parent][0]:
            tree[parent][0] = child
        else:
            tree[parent][2] = child
    cnt = 0
    subtree(N)

    print('#{} {}'.format(tc, cnt))