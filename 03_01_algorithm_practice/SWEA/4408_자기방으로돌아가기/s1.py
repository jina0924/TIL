# SWEA 4408. 자기 방으로 돌아가기

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())                            # n: 학생 수
    move = [0] * 201                            # 이동할 복도 개수(인덱스처리를 위해 1개 더 추가)
    for _ in range(n):
        a, b = map(int, input().split())
        # 복도를 공유하는 방을 묶기 위해 (a+1)//2와 같이 설정해줌
        # (1, 2), (3, 4), (5, 6) ... 이런식이어서 (a+1)//2를 해줬을 때 서로 같은 값이 나옴
        if a < b:
            for j in range((a+1)//2, (b+1)//2 + 1):
                move[j] += 1
        elif a > b:
            for j in range((b+1)//2, (a+1)//2 + 1):
                move[j] += 1
    cnt = max(move)
    
    print('#{} {}'.format(tc, cnt))

