# SWEA 1961. 숫자 배열 회전

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    matrix = [list(input().split()) for _ in range(n)]
    # new_matrix = [[0] * 3 for _ in range(n)]
    # for i in range(n):
    #     num_90, num_180, num_270 = '', '', ''
    #     for j in range(n):
    #         num_90 += matrix[n-j-1][i]
    #         num_180 += matrix[n-i-1][n-j-1]
    #         num_270 += matrix[j][n-i-1]
    #     new_matrix[i][0] = num_90
    #     new_matrix[i][1] = num_180
    #     new_matrix[i][2] = num_270
    # print(f'#{tc}')
    # for row in new_matrix:
    #     print(*row)
    print(f'#{tc}')
    for i in range(n):                          # 중심축
        num_90, num_180, num_270 = '', '', ''   # 90도, 180도, 270도 회전한 숫자 담을 변수
        for j in range(n):                      # 빠르게 회전할 인덱스
            num_90 += matrix[n-j-1][i]          # 행을 거꾸로 거슬러 올라감
            num_180 += matrix[n-i-1][n-j-1]     # 행과 열을 거꾸로 거슬러 올라감
            num_270 += matrix[j][n-i-1]         # 열을 거꾸로 거슬러 올라감
        print(num_90, num_180, num_270)


