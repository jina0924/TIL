# SWEA 2005. 파스칼의 삼각형 -> 시간초과

def pascal(n):
    if n == 1:
        arr = [0, 1, 0]
        return arr
    else:
        arr = [0] * (n+2)
        for i in range(1, n+1):
            arr[i] = pascal(n-1)[i-1] + pascal(n-1)[i]
        return arr

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    print('#{}'.format(tc))
    for i in range(1, n+1):
        print(*pascal(i)[1:-1])

