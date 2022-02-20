import sys
sys.stdin = open('input.txt')

T = int(input())
dr = [0, 1, 0, -1]      # 움직일 방향: 동, 남, 서, 북
dc = [1, 0, -1, 0]

for tc in range(1, T+1):
    n = int(input())
    snail = [[0] * n for _ in range(n)]
    r, c, d = 0, 0, 0
    for num in range(1, n*n+1):
        snail[r][c] = num
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < n and 0 <= nc < n and snail[nr][nc] == 0:
            r, c = nr, nc
        else:
            d = (d + 1) % 4
            r += dr[d]
            c += dc[d]

    print('#{}'.format(tc))
    for i in range(n):
        for j in range(n):
            print(snail[i][j], end=' ')
        print()

