# SWEA 6485. 삼성시의 버스 노선

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())                    # 노선의 개수
    # i번째 노선 번호 Ai, Bi
    line_num = [list(map(int, input().split())) for _ in range(n)]
    p = int(input())                    # 버스 정류장 수
    cnt = [0] * p                       # 정류장을 지나가는 버스의 개수를 담을 리스트
    for j in range(p):                  # 정류장 수만큼 돌면서
        station = int(input())          # 정류장 번호를 받음
        for i in range(n):              # i번 버스가 해당 정류장을 다니는지 확인
            if station in range(line_num[i][0], line_num[i][1]+1):  # 다닌다면
                cnt[j] += 1             # cnt값 1 올려줌



    print('#{}'.format(tc), *cnt)
