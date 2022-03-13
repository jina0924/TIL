# SWEA 4869. 종이붙이기

def tape(n):            # 붙일 수 있는 종이 개수 구하는 함수
    if n == 1:          # 만약 가로의 길이가 10이라면
        return 1        # 10*20 1개 붙이는 방법만 있음
    elif n == 2:        # 만약 가로의 길이가 20이라면
        return 3        # 10*2개, 20*1개, 10(눕혀서)*2개 -> 총 3가지 경우 있음
    else:               # 가로의 길이가 20을 넘어선다면
        '''
        10하나 넣었을 때 나머지 채우는 방법의 수
        + 20 하나 넣었을 때 나머지 채우는 방법의 수 * 2
        (* 2인 이유 : 20을 10을 눕힌 2개로 표현할 수 있으므로 경우의 수가 2배)
        '''
        return tape(n-1) + tape(n-2) * 2
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input()) // 10
    ans = tape(n)
    print('#{} {}'.format(tc, ans))

