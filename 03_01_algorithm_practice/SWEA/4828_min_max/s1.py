import sys

sys.stdin = open('input.txt')
T = int(input())

def bubble_sort(arr, n):
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    sorted_nums = bubble_sort(nums, N)
    ans = sorted_nums[-1] - sorted_nums[0]

    print('#{} {}'.format(tc, ans))

