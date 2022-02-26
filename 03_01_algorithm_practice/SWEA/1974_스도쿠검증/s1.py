# SWEA 1974. 스도쿠 검증

def check_line(matrix):                     # 일렬로 검증하기
    check = [1] * 9                         # count와 비교할 단서
    for i in range(9):                      # 스도쿠 행별로 살펴보기
        count = [0] * 9                     # 각 숫자를 셀 count 리스트 마련
        for j in range(9):
            count[matrix[i][j]-1] += 1      # 스도쿠 숫자를 인덱스로 삼아 count에 1 더해줌
        if count != check:                  # 만약 check처럼 모든 숫자의 개수가 1이 아니라면
            return 0                        # 0을 반환하고 함수를 끝냄
    else:                                   # 모든 for문을 돌았다 = 모든 숫자가 겹치지 않게 있었다
        return 1                            # 1을 반환함

def check_square(matrix):                   # 3x3 검증하기
    check = [1] * 9
    for i in range(0, 7, 3):                # 좌상단 좌표(0, 3, 6) 살펴보기 위한 범위
        for j in range(0, 7, 3):
            count = [0] * 9
            for k in range(3):
                for l in range(3):
                    count[matrix[i+k][j+l]-1] += 1  # 3x3에 있는 숫자들 개수 세기
            if count != check:                      # 만약 이번에 살펴본 3x3이 숫자가 겹친다면
                return 0                            # 0 반환하고 함수 끝냄
    else:
        return 1

import sys
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]    # 행 별로 살펴볼 matrix
    sudoku2 = list(zip(*sudoku))                                    # 열 별로 살펴볼 matrix
    # 모든 검증에서 1이 나오면 전체 스도쿠가 숫자 정렬이 겹치지 않다는 의미
    total = check_line(sudoku) + check_line(sudoku2) + check_square(sudoku)
    if total == 3:
        ans = 1
    else:
        ans = 0
    print('#{} {}'.format(tc, ans))

