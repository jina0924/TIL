# SWEA 4865. 글자수
def max_cnt(s1, s2):            # 포함된 글자 중 가장 많은 글자의 개수를 찾는 함수
    n, m = len(s1), len(s2)     # n: s1의 길이, m: s2의 길이
    ans, cnt = 0, 0             # ans: 최종적으로 반환할 값, cnt: 글자수를 셀 변수
    for i in range(n):          # s1의 글자를 하나씩 뽑아서
        for j in range(m):      # s2의 글자와 하나하나 비교해줌
            if s2[j] == s1[i]:  # 만약 해당 글자가 서로 같다면
                cnt += 1        # cnt를 1 더해줌
        if ans < cnt:           # 최종 값보다 지금까지 센 글자 수가 더 크다면
            ans = cnt           # 최종 값에 지금까지의 글자수를 더해줌
        cnt = 0                 # 다음 글자수를 세기 위해 0으로 리셋함
    return ans

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    str1, str2 = input(), input()
    result = max_cnt(str1, str2)
    print('#{} {}'.format(tc, result))

