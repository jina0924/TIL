# SWEA 2805. 농작물 수확하기

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())                    # NxN 크기의 농장
    farm = [list(map(int, input())) for _ in range(N)]
    profit = 0                          # 농장 수익 0으로 초기화
    # width = 위에서부터 아래로 갈때 더해지는 행의 길이
    width = [x for x in range(0, N, 2)] + [x for x in range(N-3, -1, -2)]
    # left_end = 더할 행의 시작점
    left_end = [x for x in range(N//2, -1, -1)] + [x for x in range(1, N//2+1)]
    for i in range(N):
        for w in range(width[i]+1):
            profit += farm[i][left_end[i]+w]
    print(f'#{tc} {profit}')