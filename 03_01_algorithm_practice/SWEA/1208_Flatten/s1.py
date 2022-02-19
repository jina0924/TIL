import sys
sys.stdin = open('input.txt')

def dump(arr, n):
    while n:
        arr.sort()
        if arr[-1] - arr[0] <= 1:
            return arr[-1] - arr[0]
        else:
            arr[-1] -= 1
            arr[0] += 1
            n -= 1
    arr.sort()
    return arr[-1] - arr[0]

for tc in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))
    ans = dump(boxes, N)
    print('#{} {}'.format(tc, ans))

