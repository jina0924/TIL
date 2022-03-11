# SWEA 4613. 러시아 국기 같은 깃발

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())            # n: 가로 길이, m: 세로 길이
    matrix = [list(input()) for _ in range(n)]  # 색칠되어 있는 입력값
    color = [[0] * 3 for _ in range(n)]         # 색깔별로 해당 색을 칠하기 위해 필요한 횟수 담을 리스트
    for i in range(n):
        color[i][0] = m - matrix[i].count('W')  # 행을 흰색으로 채우기 위해 칠해야 할 횟수
        color[i][1] = m - matrix[i].count('B')  # 행을 파란색으로 채우기 위해 칠해야 할 횟수
        color[i][2] = m - matrix[i].count('R')  # 행을 빨간색으로 채우기 위해 칠해야 할 횟수
    min_cnt = n * m                             # 최소 횟수를 n*m으로 초기화
    for i in list(range(1, n-1)):               # i: 파란색으로 덮을 행의 시작
        for j in list(range(i+1, n)):           # j: 빨간색으로 덮을 행의 시작
            total = 0                           # 총합 변수 0으로 초기화
            for w in range(i):                  # 흰색 칠하기
                total += color[w][0]
            for b in range(i, j):               # 파란색 칠하기
                total += color[b][1]
            for r in range(j, n):               # 빨간색 칠하기
                total += color[r][2]
            if min_cnt > total:                 # 칠해서 나온 총 합이 최소값보다 작다면
                min_cnt = total                 # 최소값 갱신하기

    print('#{} {}'.format(tc, min_cnt))

