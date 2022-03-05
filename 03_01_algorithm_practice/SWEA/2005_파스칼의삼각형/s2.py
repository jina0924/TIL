# SWEA 2005. 파스칼의 삼각형

# 삼각형 n번째 행에 해당하는 리스트를 반환하는 함수
def pascal(n):
    if n == 1:
        return [1]
    else:
        arr = [1] + [0] * (n-2) + [1]                   # 양 옆을 1로 두고 위에서 더해줄 공간을 0으로 초기화
        for i in range(1, n-1):                         # 양 옆 한 칸씩을 제외하고 반복하면서
            arr[i] = pascal(n-1)[i-1] + pascal(n-1)[i]  # n-1번째 수열의 값들을 더해서 리스트에 저장해줌
        return arr

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    print('#{}'.format(tc))
    for i in range(1, n+1):
        print(*pascal(i))

