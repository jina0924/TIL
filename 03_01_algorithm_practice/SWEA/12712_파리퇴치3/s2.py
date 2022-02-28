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
            dr = [-1, -1, -1, 0, 1, 1, 1, 0]
            dc = [-1, 0, 1, 1, 1, 0, -1, -1]
            # kill_cross: +자모양, kill_diagonal: x자모양
            kill_cross = kill_diagonal = files[r][c]
            for k in range(8):
                for z in range(1, M):
                    nr = r + dr[k] * z
                    nc = c + dc[k] * z
                    if 0 <= nr < N and 0 <= nc < N:
                        if k % 2:
                            kill_cross += files[nr][nc]
                        else:
                            kill_diagonal += files[nr][nc]
            if kill_cross > ans:
                ans = kill_cross
            elif kill_diagonal > ans:
                ans = kill_diagonal

    print(f'#{tc} {ans}')