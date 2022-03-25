# SWEA 5102. 노드의 거리

import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(v):
    queue = deque([(v)])                            # 매개변수로 받은 값 큐에 넣어주기
    visited[v] = 1

    while queue:                                    # 갈 수 있는 곳 전부다 돌아보기
        v = queue.popleft()                         # 큐에 있는 첫 번째값이 현재 살펴볼 위치
        if v == G:                                  # 만약 지금 위치가 도착지라면
            return visited[v] - 1                   # 지금까지 거쳐온 경로의 수 반환함
        for i in range(V+1):
            if Graph[v][i] and not visited[i]:      # 이웃한 정점이고 아직 방문하지 않은 곳이라면
                queue.append(i)                     # 큐에 담아두고 나중에 방문함
                visited[i] = visited[v] + 1         # 지금까지 움직인 경로 누적해서 저장
    return 0

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())                # V: 정점의 개수, E: 간선의 개수
    Graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for _ in range(E):
        n1, n2 = map(int, input().split())
        Graph[n1][n2] = Graph[n2][n1] = 1
    visited = [0 for _ in range(V+1)]               # 도착하기 위해서 돌아가지 않기위해 visited 여부 확인해주기
    S, G = map(int, input().split())                # S: 출발 노드, G: 도착 노드
    ans = bfs(S)
    print('#{} {}'.format(tc, ans))

