import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())                            # 색칠할 영역의 개수
    coloring = [[0] * 10 for _ in range(10)]    # 백지 준비
    squares = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        x1, y1, x2, y2 = squares[i][:4]         # (x1, y1), (x2, y2)값 만들기
        for x in range(x1, x2+1):               # 가로의 길이만큼
            for y in range(y1, y2+1):           # 세로의 길이만큼
                coloring[x][y] += squares[i][4] # 정해진 색 칠하기
    cnt = 0                                     # 보라색 칸 수 담을 변수
    for i in range(10):
        for j in range(10):
            if coloring[i][j] >= 3:             # 색이 겹쳐지면 3 이상이므로
                cnt += 1
    print('#{} {}'.format(tc, cnt))

