# 백준 2444번 별 찍기-7

N = int(input())
for i in range(1, N):
    print(' ' * (N-i) + '*' * (2*i-1))
print('*' * (2*N-1))
for j in range(N-1, 0, -1):
    print(' ' * (N-j) + '*' * (2*j-1))