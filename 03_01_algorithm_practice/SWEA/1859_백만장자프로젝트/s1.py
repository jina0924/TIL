# SWEA 1859. 백만 장자 프로젝트

def millionaire(arr, n):
    cnt = [0] * n                           # 오늘보다 저렴한 가격 개수를 세어줄 리스트
    for i in range(1, n):
        for j in range(0, i):               # 현재 살펴볼 요소 앞까지 보기위한 범위
            if arr[j] < arr[i]:             # 만약 앞의 요소가 지금 보는 요소보다 작다면
                cnt[i] += 1                 # 횟수를 1 올려줌
            else:                           # 만약 앞 요소가 지금 요소보다 크거나 같다면
                cnt[i] = 0                  # 횟수를 다시 세기 위해 0으로 리셋
    profit, i = 0, n-1                      # profit: 전체 이익, i: 요소를 뒤에서부터 살펴보기 위한 인덱스
    while i > 0:                            # 둘째날까지 살펴보도록 반복문 시행
        if cnt[i]:                          # 만약 이익을 볼 수 있다면
            for j in range(i-1, i-cnt[i]-1, -1):    # 해당 횟수만큼 앞으로 넘어가면서
                profit += arr[i] - arr[j]   # 이익을 전체 이익에 더해줌
            i -= cnt[i] + 1                 # 인덱스를 횟수 만큼 전으로 돌림
        else:                               # 이익을 볼 수 없다면(0이라면)
            i -= 1                          # 인덱스를 하나 빼서 앞 요소로 넘어감
    return profit


import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    ans = millionaire(price, N)

    print('#{} {}'.format(tc, ans))

