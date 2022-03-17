# SWEA 4871. 그래프 경로

def dfs(v):                             # 넘겨받은 부분부터 차례로 방문할 함수
    stack = [v]                         # 스택에 넘겨받은 인자 담아둠

    while stack:                        # 스택이 비어있을 때까지 반복
        now = stack.pop()               # 현재 위치 = 스택 맨 위의 요소
        if not visited[now]:            # 만약 현재 위치에 방문하지 않았다면
            visited[now] = 1            # 방문 체크 먼저 하고
            for node in range(1, V+1):  # 모든 노드 중에서
                if Graph[now][node] == 1 and not visited[node]: # 현재 위치와 인접하고 아직 들르지 않은데가 있다면
                    stack.append(node)  # 스택에 쌓아두고 차례로 방문함
    if visited[end]:                    # 스택이 비어있다 = 방문할 곳 다 갔다왔다
        return 1                        # 원하는 도착지에 방문했다면 1 반환
    return 0                            # 다 방문해도 원하는 도착지에 못갔다면 0 반환

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())        # V: 노드 개수, E: 간선 개수
    Graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for _ in range(E):
        n1, n2 = map(int, input().split())  # n1: 출발 노드, n2: 도착 노드
        Graph[n1][n2] = 1
    visited = [0 for _ in range(V+1)]       # 방문 체크 리스트
    start, end = map(int, input().split())  # start: 경로 확인 출발지, end: 도착지
    ans = dfs(start)
    print('#{} {}'.format(tc, ans))

