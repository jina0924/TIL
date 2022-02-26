# 2001. 파리 퇴치

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    files = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for r in range(N-M+1):
        for c in range(N-M+1):
            kill = 0
            for w in range(M):
                for h in range(M):
                    kill += files[r+w][c+h]
            if ans < kill:
                ans = kill

    print('#{} {}'.format(tc, ans))