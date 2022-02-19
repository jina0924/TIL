import sys
sys.stdin = open('input.txt')

def charging_cnt(k, n, m, arr):
    dx = [arr[0]] + [0] * (m-1) + [n-arr[-1]]   # 시작점, 정류장, 도착점까지 가야할 거리 리스트
    for i in range(1, m):   # 정류장 사이의 거리 구하기
        dx[i] = arr[i] - arr[i-1]
    cnt, i, battery = 0, 0, k   # cnt : 충전 횟수, i : 거리에 접근할 인덱스, battery : 충전할 배터리
    while i < m:    # 이동할 수 있는 거리가 남아있을 때까지 반복
        if dx[i] <= battery:    # 만약 배터리보다 이동거리가 짧거나 같다면
            battery -= dx[i]    # 배터리만큼 이동하고
            i += 1      # 다음 충전소까지의 거리를 살펴보기 위해 인덱스값 1 올려줌
            if dx[i] > battery:     # 만약 다음 이동거리가 남은 배터리 양보다 멀다면
                battery = k     # 배터리를 충전하고
                cnt += 1        # 충전 횟수를 1 더해줌
        else:       # 만약 배터리보다 더 많은 거리를 가야한다면 못가므로 0 반환
            return 0
    return cnt

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    stations = list(map(int, input().split()))
    ans = charging_cnt(K, N, M, stations)
    print('#{} {}'.format(tc, ans))

