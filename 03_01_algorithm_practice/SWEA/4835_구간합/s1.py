import sys

def prefix_sum(arr, n, m):
    a = [0] * (n - m + 1)
    for i in range(len(a)):
        a[i] = sum(arr[i:i+m])
    max_sum = max(a)
    min_sum = min(a)
    ans = max_sum - min_sum
    return ans

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    my_list = list(map(int, input().split()))
    result = prefix_sum(my_list, N, M)
    
    print('#{} {}'.format(tc, result))

