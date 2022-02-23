import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    sorted_arr = [0] * 10                               # 정렬된 값 담을 리스트
    for i in range(n-1):                                # 선택 정렬
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    start, end = 0, n-1                                 # start: 가장 작은 값, end: 가장 큰 값 인덱스
    for i in range(0, 10, 2):                           # 큰 순서대로 퐁당퐁당 담기
        sorted_arr[i] = arr[end]
        end -= 1
    for j in range(1, 10, 2):                           # 작은 순서대로 퐁당퐁당 담기
        sorted_arr[j] = arr[start]
        start += 1

    print('#{}'.format(tc), *sorted_arr)