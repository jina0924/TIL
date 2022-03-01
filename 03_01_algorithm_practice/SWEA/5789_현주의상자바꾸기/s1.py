# SWEA 5890.현주의 상자 바꾸기

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, q = map(int, input().split())        # n: 상자의 개수, q: 숫자 변경 횟수
    box = [0] * n                           # 상자 번호 초기값
    for i in range(q):                      # q번 반복함
        l, r = map(int, input().split())    # l번 상자부터 r번 상자까지 변경할 것
        for j in range(l-1, r):             # l번 상자이므로 인덱스는 l-1부터
            box[j] = i + 1                  # 상자번호보다 인덱스값이 1작으므로 +1

    print('#{}'.format(tc), *box)
