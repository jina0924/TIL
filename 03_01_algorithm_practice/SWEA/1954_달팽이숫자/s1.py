import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    snail = [[0] * n for _ in range(n)]
    num = 1
    r, c = 0, -1                    # 처음 이동을 위해 c를 -1로 시작
    move = n
    while move > 0:
        for _ in range(move):       # 왼쪽에서 오른쪽으로 이동
            c += 1                  # 오른쪽으로 한 칸 움직임
            snail[r][c] = num
            num += 1
        move -= 1                   # 남쪽으로 이동할 횟수
        for _ in range(move):       # 위에서 아래로 이동
            r += 1                  # 아래로 한 칸 움직임
            snail[r][c] = num
            num += 1
        for _ in range(move):       # 오른쪽에서 왼쪽으로 이동
            c -= 1                  # 왼쪽으로 한 칸 움직임
            snail[r][c] = num
            num += 1
        move -= 1                   # 북쪽으로 이동할 횟수
        for _ in range(move):       # 아래에서 위로 이동
            r -= 1                  # 위쪽으로 한 칸 움직임
            snail[r][c] = num
            num += 1
    print('#{}'.format(tc))
    for i in range(n):
        for j in range(n):
            print(snail[i][j], end=' ')
        print()

