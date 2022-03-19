# SWEA 4875. 미로

def escape(matrix, r, c):
    global ans
    matrix[r][c] = 1            # 현재 위치 방문했다고 표시해주기
    dr = [-1, 0, 1, 0]          # 북, 동, 남, 서
    dc = [0, 1, 0, -1]          # 북, 동, 남, 서
    for i in range(4):          # 델타 방향 검색
        nr, nc = r + dr[i], c + dc[i]   # 새로운 방향 설정
        if 0 <= nr < n and 0 <= nc < n: # 만약 새 방향이 범위 안에 있고
            if matrix[nr][nc] == 3:     # 새로운 위치가 3이면
                ans = 1                 # ans를 1로 바꿔줌
            if not matrix[nr][nc]:      # 만약 새 위치가 0(통로)라면
                escape(matrix, nr, nc)  # 새로운 길 찾아 나섬

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    ans = 0
    for i in range(n):                  # 시작위치 잡기
        for j in range(n):
            if maze[i][j] == 2:
                escape(maze, i, j)
    print('#{} {}'.format(tc, ans))

