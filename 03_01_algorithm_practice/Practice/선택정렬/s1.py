# 선택 정렬

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

import sys
sys.stdin = open('input.txt')

numbers = list(map(int, input().split()))
print(selection_sort(numbers))