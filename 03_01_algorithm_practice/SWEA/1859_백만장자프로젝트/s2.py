# SWEA 1859. 백만 장자 프로젝트

# 이익을 계산하려면 미래에서 과걸로 회귀해야함
# 미래에서 하나씩 과거로 돌아오면서 최고가를 갱신할 수 있다면 갱신해줌
def millionaire(arr, n):                    # 총 이익 계산할 함수
    max_price = arr[-1]                     # 초기 최고가 = 가장 먼 미래의 매매가
    profit = 0                              # 총 이익을 담을 변수
    for i in range(n-2, -1, -1):            # 두번째로 먼 미래부터 하루씩 앞당겨 살펴보기
        if arr[i] > max_price:              # 만약 과거에 좀 더 높은 매매가가 있다면
            max_price = arr[i]              # 최고가를 갱신해줌
        else:                               # 지금 매매가가 최고가라면
            profit += max_price - arr[i]    # 판매해서 이익 남겨줌
    return profit


import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    ans = millionaire(price, N)

    print('#{} {}'.format(tc, ans))