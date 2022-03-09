# 백준 1012번 유기농 배추

def worm(r, c):
    global cnt                              # 전역에 있는 지렁이 마리 수 변경할 예정
    queue[0][0], queue[0][1] = r, c         # queue 맨 앞에 매개변수 r, c 할당
    farm[r][c] = 5                          # 5 = 해당 배추를 살펴봤다는 의미
    top, rear = -1, 0                       # queue에 값을 빼고 넣을 인덱스값

    while top != rear:                      # top과 rear가 같다 = queue에 더 이상 넣을 요소가 없다
        top += 1                            # queue의 있는 요소들 살펴보러 가기 위해 인덱스값 1 올림
        r, c = queue[top][0], queue[top][1] # queue 맨 앞에 있는 값을 행과 열에 할당
        dr = [-1, 0, 1, 0]                  # 상, 우, 하, 좌
        dc = [0, 1, 0, -1]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m: # 새롭게 살펴본 위치가 농장 안에 있고
                if farm[nr][nc] == 1:       # 그 위치에 배추가 있다면
                    farm[nr][nc] = 5        # 방문(할 예정) 표시해둠
                    rear += 1               # queue에 해당 위치값 넣기 위해 인덱스값 1 올림
                    queue[rear][0], queue[rear][1] = nr, nc # 새롭게 살펴본 위치값 queue에 저장
    cnt += 1        # while문 다 돌았다 = queue에 더 이상 볼 요소 없다 = 근처에 배추 없다 = 지렁이 1마리 추가

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    m, n, k = map(int, input().split())     # m: 가로길이, n: 세로길이, k: 배추 개수
    farm = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        farm[y][x] = 1                      # y: 행, x:열

    queue = [[0, 0] for _ in range(k)]
    cnt = 0                                 # 매 농장마다 지렁이 마리 수 0으로 초기화
    for r in range(n):
        for c in range(m):
            if farm[r][c] == 1:             # 만약 해당 행렬의 요소가 배추라면
                worm(r, c)            # 지렁이 배치하러 감

    print('{}'.format(cnt))