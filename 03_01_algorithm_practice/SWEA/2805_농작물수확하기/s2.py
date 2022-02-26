# SWEA 2805. 농작물 수확하기

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    profit = 0
    r = 0
    left_end = N//2

    while left_end >= 0:
        if left_end:
            for c in range(left_end, N-left_end):
                profit += farm[r][c]
                profit += farm[N-1-r][c]
        elif not left_end:
            for c in range(N):
                profit += farm[r][c]
        r += 1
        left_end -= 1

    print(f'#{tc} {profit}')