import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    r, c = 99, 0                        # 출발점 찾을 초기 변수
    for i in range(100):
        if ladder[99][i] == 2:          # 출발점 좌표 찾기
            c = i
            break

    while r > 0:                        # 맨 위에 도착할 때까지 반복
        turn = False                    # 좌우 살피기 위한 변수
        while 0 < c < 100 and ladder[r][c-1] == 1:  # 왼쪽으로 갈 수 있다면
            c -= 1                      # 왼쪽으로 한 칸 옮기고
            turn = True                 # 오른쪽으로 다시 옮기지 않기 위한 장치

        while not turn and 0 <= c < 99 and ladder[r][c+1] == 1: #오른쪽으로 갈 수 있다면
            c += 1                      # 오른쪽으로 한 칸 옮기기
            # 왼쪽으로 가는 길은 이미 살펴봤으므로 turn을 Ture로 바꿀 필요 x
        r -= 1                          # while문의 조건을 만족하지 않는다면 위로 올라가기

    print('#{} {}'.format(n, c))

