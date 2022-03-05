# 백준 7562번 나이트의 이동

def knight(r, c):
    queue=[(r, c)]

    while r != goal_r or c != goal_c:
        r, c = queue.pop(0)
        dr = [-2, -1, 1, 2, 2, 1, -1, -2]   # 1시, 2시, 4시, 5시 7시, 8시, 10시, 11시 방향
        dc = [1, 2, 2, 1, -1, -2, -2, -1]
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < l and 0 <= nc < l and not chess[nr][nc]:
                chess[nr][nc] = 1 + chess[r][c]
                queue.append((nr, nc))
    return chess[goal_r][goal_c]

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    l = int(input())
    chess = [[0 for _ in range(l)] for _ in range(l)]
    r, c = map(int, input().split())
    goal_r, goal_c = map(int, input().split())
    ans = knight(r, c)
    print(ans)