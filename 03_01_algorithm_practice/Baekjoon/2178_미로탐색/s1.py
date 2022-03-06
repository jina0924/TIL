# 백준 2178번 미로 탐색

def escape(r, c):
    queue = [(r, c)]

    while r != n or c != m:     # 도착지에 다다를 때까지 반복
        r, c = queue.pop(0)     # 큐 맨 앞에 있는 좌표 꺼내기
        dr = [-1, 0, 1, 0]      # 상, 우, 하, 좌
        dc = [0, 1, 0, -1]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 < nr <= n and 0 < nc <= m and maze[nr][nc] == 1:   # 값이 1이다 = 길이지만 아직 들르지 않았다
                maze[nr][nc] = 1 + maze[r][c]   # 이동한 칸 수를 해당 칸에 입력해줌
                queue.append((nr, nc))

    return maze[n][m]

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())    # n: 행의 크기, m: 열의 크기
    # 인덱스 접근 쉽게하기 위해 사방에 0으로 패딩 주기
    maze = [[0]*(m+2)] + [[0] + list(map(int, input())) + [0] for _ in range(n)] + [[0]*(m+2)]
    ans = escape(1, 1)  # (1, 1)에서 시작
    print(ans)