# SWEA 1219. 길찾기

def dfs(v):                                 # 깊이우선탐색
    stack = [v]                             # 넘겨받은 인자를 스택에 넣어주기

    while stack:                            # 스택이 비어있을 때까지 반복
        now = stack.pop()                   # 현재 위치 = 스택 가장 위 요소
        if now == 99:                       # 만약 현재 위치가 도착점(99)라면
            return 1                        # 1을 반환하고 함수 끝냄
        if not visited[now]:                # 만약 현재 위치를 방문하지 않았다면
            visited[now]                    # 방문했다는 표시 남기고
            for neighbor in adj_list[now]:  # 인접한 위치들 살펴봄
                if not visited[neighbor]:   # 살펴본 위치에 아직 방문하지 않았다면
                    stack.append(neighbor)  # 스택에 쌓아놓고 차례로 방문함
    return 0                                # 스택이 비어있을 동안 99를 만나지 못했다면 길 존재하지 않음

import sys
sys.stdin = open('input.txt')

for _ in range(1, 11):
    tc, E = map(int, input().split())
    temp = list(map(int, input().split()))
    adj_list = [[] for _ in range(100)]
    for i in range(E):
        n1, n2 = temp[i*2], temp[i*2+1]
        adj_list[n1].append(n2)
    visited = [0 for _ in range(100)]
    ans = dfs(0)

    print('#{} {}'.format(tc, ans))

