# SWEA 5099. 피자 굽기

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())                # n: 화덕이 크기, m: 피자의 개수
    pizza_list = list(map(int, input().split()))    # m개의 피자 리스트
    oven = [0 for _ in range(n)]
    for i in range(n):                              # n개 만큼 피자를 넣음 = 1바퀴 돌았다는 의미
        oven[i] = [i, pizza_list[i] // 2]           # 미리 치즈의 양을 반으로 줄여서 화덕에 넣어둠
    idx = n                                         # 다음 피자를 넣을 인덱스 준비
    while len(oven) > 1:                            # 오븐에 피자가 하나 남을 때까지
        num, pizza = oven.pop(0)                    # 1번 위치에서 피자 빼서 살펴보기
        if pizza:                                   # pizza에 치즈가 남아있다면
            oven.append([num, pizza//2])            # 화덕에 다시 넣어서 치즈 반만큼 녹임
        elif not pizza and idx < m:                 # 만약 치즈가 다 녹았거나 남아있는 피자를 모두 다 넣지 않았다면
            oven.append([idx, pizza_list[idx] // 2])    # 남아있는 피자 새로 넣기
            idx += 1                                # 피자 넣기 위해 인덱스값 올리기
    ans = oven[0][0] + 1                            # 마지막에 남아있는 피자 위치가 답
    print('#{} {}'.format(tc, ans))