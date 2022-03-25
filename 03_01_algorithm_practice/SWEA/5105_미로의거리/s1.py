# SWEA 5105. 미로의 거리

import sys
from collections import deque
sys.stdin = open('input.txt')

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]          # 아래, 오른쪽, 위, 왼쪽 방향
def escape(r, c):
    queue = deque([(r, c)])                         # 처음 넘겨받은 매개변수 큐에 넣고 시작

    while queue:                                    # 큐에 위치값이 남아있을 때까지 반복
        r, c = queue.popleft()                      # 맨 앞에 있는 위치값이 현재 살펴볼 위치
        for d in range(4):
            nr, nc = r + delta[d][0], c + delta[d][1]
            if 0 <= nr < n and 0 <= nc < n:         # 만약 미로 범위 안에 있고
                if not maze[nr][nc]:                # 아직 지나오지 않은 통로라면(0이라면)
                    maze[nr][nc] = maze[r][c] + 1   # 지난 방문 수를 누적해서 1 더해줌
                    queue.append((nr, nc))          # 새로 방문할 곳 큐에 넣기
                elif nr == end_r and nc == end_c:   # 이번에 살펴본 범위가 도착지라면
                    return maze[r][c] - 2           # 지금까지 이동한 칸 수가 누적되어 있으므로 2 빼서 반환(2는 출발지 값)
    return 0                                        # 다 방문해도 도착지까지 못갔으므로 0 반환

T = int(input())

for tc in range(1, T+1):
    n = int(input())                    # n: 미로의 가로, 세로 길이
    maze = [list(map(int, input())) for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if maze[r][c] == 2:
                start_r, start_c = r, c
            elif maze[r][c] == 3:
                end_r, end_c = r, c
    ans = escape(start_r, start_c)
    print('#{} {}'.format(tc, ans))

