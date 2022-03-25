# SWEA 1226. 미로1

import sys
sys.stdin = open('input.txt')

dr = [1, 0, 0, -1]
dc = [0, -1, 1, 0]


def escape(r, c):
    stack = [(r, c)]

    while stack:
        r, c = stack.pop()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 1 <= nr < 14 and 1 <= nc < 14:       # 14, 15 행/열은 벽이라 1부터 14까지만 살펴봄
                if maze[nr][nc] == 3:               # 도착지에 도착했다면
                    return 1                        # 1을 반환함
                elif not maze[nr][nc]:              # 만약 0이라면(통로라면)
                    maze[nr][nc] = 5                # 방문표시로 5를 새겨놓고
                    stack.append((nr, nc))          # 해당 지점부터 다시 길 탐색함
    return 0                                        # stack에 남아있는 위치값이 없다 = 다 돌아봤다 근데 도착지에 못갔다면 0 반환


for _ in range(1, 11):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    print('#{} {}'.format(tc, escape(1, 1)))
