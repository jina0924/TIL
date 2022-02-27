# 백준 2445번 별 찍기-8

N = int(input())

for i in range(1, N+1):
    print('*' * i + ' ' * (2*N - 2*i) + '*' * i)
for j in range(N-1, 0, -1):
    print('*' * j + ' ' * (2*N - 2*j) + '*' * j)