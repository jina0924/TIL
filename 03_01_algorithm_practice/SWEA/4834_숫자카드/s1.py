import sys
sys.stdin = open('input.txt')

def max_card(arr, n):
    cnt = [0] * 10
    for i in range(n):
        cnt[arr[i]] += 1
    cnt_max = max(cnt)
    for j in range(9, -1, -1):
        if cnt[j] == cnt_max:
            return j, cnt_max

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input()))
    card, number = max_card(nums, n)
    
    print('#{} {} {}'.format(tc, card, number))

