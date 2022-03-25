# SWEA 5097. 회전

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(m):
        front = arr.pop(0)
        arr.append(front)
    ans = arr[0]
    print('#{} {}'.format(tc, ans))