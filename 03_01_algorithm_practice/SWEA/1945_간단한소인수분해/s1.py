# SWEA 1945. 간단한 소인수분해

def prime(num):                     # 소인수분해할 함수
    prime_num = [2, 3, 5, 7, 11]    # 소인수
    cnt = [0] * 5                   # 각 소인수의 지수를 담을 리스트
    i = 0                           # 인덱스 접근하기 위한 초기값
    while i < 5:                    # 소인수가 총 5개이므로 인덱스가 4일때까지
        if not num % prime_num[i]:  # 만약 해당 소인수로 나누어 떨어진다면
            num //= prime_num[i]    # 매개변수로 받은 값을 소인수로 나눠서 저장하고
            cnt[i] += 1             # 지수값을 1 더해줌
        else:                       # 만약 소인수로 나누어지지 않는다면
            i += 1                  # 인덱스를 1 올려줌
    return cnt                      # 소인수 지수를 담은 리스트 반환

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    ans = prime(n)
    print('#{}'.format(tc), *ans)

