# SWEA 4880. 토너먼트 카드게임

lose = {1 : 2, 2 : 3, 3 : 1}                    # 1 = 가위, 2 = 바위, 3 = 보 => 각각을 냈을 때 반드시 지는 조합

def rps(arr):                                   # 가위바위보 승자 반환 함수
    n = len(arr)
    if n == 1:                                  # 만약 혼자 남았다면
        return arr                              # 자기 자신이 승자
    else:                                       # 둘 이상 남았다면
        mid = (n+1) // 2                        # 둘을 반으로 쪼갬(n+1인 이유 => 3일 때 2/1로 나누기 위해)
        left = rps(arr[:mid])                   # 왼쪽 그룹과
        right = rps(arr[mid:])                  # 오른쪽 그룹으로 나눔

        if lose.get(left[0][1]) == right[0][1]: # 만약 왼쪽이 지는 조합이라면
            return right                        # 오른쪽이 승자
        return left                             # 왼쪽이 이겼거나 번호가 작으므로 왼쪽 반환

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())                            # n: 인원수
    cards = list(map(int, input().split()))     # n명이 고른 각각의 카드
    for idx, card in enumerate(cards):          # 각 학생의 번호순으로 카드 매칭시켜서 담기
        cards[idx] = [idx+1, card]
    ans = rps(cards)[0][0]                      # 승자의 번호 담기
    print('#{} {}'.format(tc, ans))

