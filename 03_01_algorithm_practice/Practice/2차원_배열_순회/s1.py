import sys
sys.stdin = open('input.txt')

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# 행 우선
for row in matrix:
    print(*row)

print('----------------')

# 열 우선
for j in range(n):
    for i in range(n):
        print(matrix[i][j], end=' ')
    print()

print('----------------')

# 지그재그
for i in range(n):
    for j in range(n):
        print(matrix[i][j + (n - 2*j -1) * (i % 2)], end=' ')
    print()

print('----------------')

# 전치행렬1
print(list(zip(*matrix)))

print('----------------')

# 전치행렬2
for i in range(n):
    for j in range(n):
        if i < j:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
print(matrix)
