# 백준 1012번 유기농 배추

def worm(r, c, m, n):
    global cnt
    queue = [(r, c)]

    while queue:
        r, c = queue.pop(0)
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if farm[nr][nc] == 1:
                    farm[nr][nc] = 5
                    queue.append((nr, nc))
    cnt += 1

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    m, n, k = map(int, input().split())
    farm = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        farm[y][x] = 1

    cnt = 0
    for r in range(n):
        for c in range(m):
            if farm[r][c] == 1:
                worm(r, c, m, n)

    print('{}'.format(cnt))

