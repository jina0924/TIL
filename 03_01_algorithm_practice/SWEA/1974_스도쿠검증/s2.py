# SWEA 1974. 스도쿠 검증

num = [1 for _ in range(9)]
def check_sudoku(matrix):
    for r in range(9):
        visited = [0 for _ in range(9)]
        for c in range(9):
            visited[matrix[r][c]-1] = 1
        if visited != num:
            return 0
    for c in range(9):
        visited = [0 for _ in range(9)]
        for r in range(9):
            visited[matrix[r][c]-1] = 1
        if visited != num:
            return 0
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            visited = [0 for _ in range(9)]
            for i in range(3):
                for j in range(3):
                    visited[matrix[r+i][c+j]-1] = 1
            if visited != num:
                return 0
    return 1

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    ans = check_sudoku((sudoku))
    print('#{} {}'.format(tc, ans))