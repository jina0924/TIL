# SWEA 13994. 새로운 버스 노선

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())                            # N: 노선의 수
    cnt = [0 for _ in range(1001)]              # 노선 개수 셀 리스트
    for _ in range(N):
        bus, A, B = map(int, input().split())   # bus: 벼스 유형, A: 시작점, B: 종점
        if bus == 1:                            # 일반 버스일 때
            for i in range(A, B+1):             # 모든 정류장 다 정차
                cnt[i] += 1
        elif bus == 2:                          # 급행 버스일 때
            for i in range(A, B, 2):            # A 홀짝 여부와 같은 정류장에만 정차 & B는 나중에 추가
                cnt[i] += 1
            cnt[B] += 1                         # A와 B에 모두 정차해야하므로 B에 정차하도록
        elif bus == 3:                          # 광역 버스일 때
            cnt[A] += 1                         # 출발점과
            cnt[B] += 1                         # 종점 모두 정차
            for i in range(A+1, B):             # 출발점과 종점 사이의 정류장 중에서
                if A % 2:                       # A가 홀수인 경우
                    if not i % 3 and i % 10:    # 3의 배수이면서 10의 배수가 아닌 정류장에 정차
                        cnt[i] += 1
                else:                           # A가 짝수인 경우
                    if not i % 4:               # 4의 배수 번호 정류장에 정차
                        cnt[i] += 1
        ans = 0
        for i in range(1, 1001):                # 최대 노선 수 구하기
            if ans < cnt[i]:
                ans = cnt[i]

    print(f'#{tc} {ans}')