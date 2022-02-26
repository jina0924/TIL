# SWEA 2001_파리퇴치

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())    # n: nXn 영역, m: 파리채
    matrix = [list(map(int, input().split())) for _ in range(n)]
    # max_sum: 가장 많이 죽인 파리 수, kill: 매 스윙 별 죽은 파리 수
    max_sum, kill = 0, 0
    for i in range(n-m+1):              # 파리채 좌상단 좌표 설정
        for j in range(n-m+1):
            for k in range(m):          # 파리채 크기만큼 돌면서 파리 죽이기
                for l in range(m):
                    kill += matrix[i+k][j+l]
            if kill > max_sum:          # 이번 파리채 스윙에서 죽인 파리수가 max_sum보다 많다면
                max_sum = kill          # 이번 파리 수로 갱신해주기
            kill = 0                    # 새로운 시도를 위해 죽인 파리 수 리셋
    print('#{} {}'.format(tc, max_sum))

