# 델타검색
# 25개의 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 절대값을 구하시오
# 25개의 요소에 대해서 모두 조사하여 총합을 구하시오

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    dr = [-1, 1, 0, 0]      # 상, 하, 좌, 우
    dc = [0, 0, -1, 1]
    ans = 0
    for i in range(n):
        for j in range(n):
            for k in range(4):
                nr = i + dr[k]      # nr: new row
                nc = j + dc[k]      # nc: new column
                if 0 <= nr < n and 0 <= nc < n:
                    ans += abs(matrix[i][j] - matrix[nr][nc])

    print(f'# {ans}')