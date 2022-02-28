# 백준 2448번 별 찍기-11

def triangle_star(r, c, n):
    if n == 3:
        matrix[r][c] = '*'
        matrix[r+1][c-1] = matrix[r+1][c+1] = '*'
        for i in range(-2, 3):
            matrix[r+2][c+i] = '*'
        return
    triangle_star(r, c, n//2)
    triangle_star(r + n//2, c - n//2, n//2)
    triangle_star(r + n//2, c + n//2, n//2)

N = int(input())
matrix = [[' ' for _ in range(2*N-1)] for _ in range(N)]
triangle_star(0, N-1, N)
# print(matrix)
for r in matrix:
    print(''.join(r))