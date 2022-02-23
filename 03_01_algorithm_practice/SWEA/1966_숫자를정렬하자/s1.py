import sys
sys.stdin = open('input.txt')

def selection_sort(arr, n):
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bubble_sort(arr, n):
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def counting_sort(arr, n):
    cnt = [0] * (n+1)
    k = len(arr)
    new_arr = [0] * k
    for i in range(k):
        cnt[arr[i]] += 1

    for i in range(1, n+1):
        cnt[i] += cnt[i-1]

    for i in range(k-1, -1, -1):
        cnt[arr[i]] -= 1
        new_arr[cnt[arr[i]]] = arr[i]

    return new_arr

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    num_list = selection_sort(list(map(int, input().split())), n)

    print('#{}'.format(tc), *num_list)

