# SWEA 3143. 가장 빠른 문자열 타이핑
def fastest(str1, str2):            # 가장 빠른 문자열 찾을 함수
    n, m = len(str1), len(str2)
    i, cnt = 0, n                   # i: 문자열 인덱스, cnt: 타이핑 횟수(초기값: str1의 길이)
    while i <= n-m:                 # 저장되어있는 문자열 길이 전까지 살펴보기
        if str1[i : i+m] == str2:   # 만약 해당 범위의 문자열이 저장된 문자열과 같다면
            cnt -= m-1              # str2길이만큼 타이핑 안해도 되므로 1회 남기고 cnt에서 빼줌
            i += m                  # 인덱스를 str2만큼 뛰어넘음
        else:                       # 만약 같은 문자열이 아니라면 하나하나 타이핑 해야하므로
            i += 1                  # 다음 칸으로 넘어감
    return cnt

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    A, B = input().split()
    ans = fastest(A, B)
    print('#{} {}'.format(tc, ans))

