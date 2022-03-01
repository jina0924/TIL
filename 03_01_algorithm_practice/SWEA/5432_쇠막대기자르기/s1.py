# SWEA 5432. 쇠막대기 자르기

def lazer_cut(arr):                 # 쇠막대기 자를 함수
    n = len(arr)                    # n: 막대기와 레이저 배치 길이
    cnt, pieces = 0, 0              # cnt: 쌓여있는 막대 수, pieces: 잘린 막대 도막들
    for i in range(n):
        if arr[i] == '(':           # '(': 막대기 하나씩 더해지는 구조
            cnt += 1
            pieces += 1
        elif arr[i] == ')':
            if arr[i-1] == '(':     # '()'이면 레이저
                cnt -= 1            # '('를 막대기로 보고 더해줬으므로 1빼줌
                pieces += cnt - 1   # pieces도 막대기로 보고 1 더해줬으므로 1 빼줌 & 두 동강
            elif arr[i] == ')':     # '))'이면 쌓여있는 막대 하나 줄어듬
                cnt -= 1
    return pieces

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    position = input()
    ans = lazer_cut(position)
    print('#{} {}'.format(tc, ans))

