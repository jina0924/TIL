# SWEA 4836. 색칠하기

def coloring(lr, lc, rr, rc, color):        # 색칠하는 함수
    for r in range(lr, rr+1):               # 행 범위만큼
        for c in range(lc, rc+1):           # 열 범위 만큼
            paper[r][c] += color            # 해당 색깔 칠해주기

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    paper = [[0 for _ in range(10)] for _ in range(10)] # 10x10의 빈 종이
    for _ in range(n):                                  # 칠할 영역의 개수만큼 반복
        # r1: 왼쪽 위 모서리 행 좌표, c1: 왼쪽 위 열 좌표, r2: 오른쪽 아래 행 좌표, c2: 오른쪽 아래 열 좌표
        # color: 1 - 빨강, 2 - 파랑
        r1, c1, r2, c2, color = map(int, input().split())
        coloring(r1, c1, r2, c2, color)
    purple = 0
    for i in range(10):                             # 모든 곳을 돌아다니면서
        for j in range(10):
            if paper[i][j] == 3:                    # 합이 3일 때 = 빨강(1) + 파랑(2) => 보라일 때
                purple += 1
    print(f'#{tc} {purple}')