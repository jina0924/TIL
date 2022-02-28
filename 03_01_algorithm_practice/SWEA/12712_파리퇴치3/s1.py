# SWEA 12712. 파리퇴치3

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    files = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for r in range(N):
        for c in range(N):
            dr = [-1, 0, 1, 0]
            dc = [0, 1, 0, -1]
            kill = files[r][c]
            for k in range(4):
                for z in range(1, M):
                    nr = r + dr[k] * z
                    nc = c + dc[k] * z
                    if 0 <= nr < N and 0 <= nc < N:
                        kill += files[nr][nc]
            if kill > ans:
                ans = kill
            dr = [-1, -1, 1, 1]
            dc = [-1, 1, -1, 1]
            kill = files[r][c]
            for k in range(4):
                for z in range(1, M):
                    nr = r + dr[k] * z
                    nc = c + dc[k] * z
                    if 0 <= nr < N and 0 <= nc < N:
                        kill += files[nr][nc]
            if kill > ans:
                ans = kill

    print(f'#{tc} {ans}')
