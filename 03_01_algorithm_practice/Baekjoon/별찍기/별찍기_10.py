# 백준 2447번 별 찍기-10

'''
컨셉: 계속 3x3으로 쪼개가면서 가장 작은 패턴 찾아나가기
r: 사각형의 좌상단 행 좌표
c : 사각형의 좌상단 열 좌표
n : 사각형의 가로, 세로 길이
'''
def star(r, c, n):
    if n == 1:
        matrix[r][c] = '*'
        return
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            else:
                star(r + n//3*i, c + n//3*j, n//3)
                '''
                쪼개진 사각형의 좌상단 좌표를 다시 함수에 넣어 호출함
                ex) n이 9일 때 첫번째 행의 경우 쪼개진 사각형의 시작점
                -> (0, 0), (0, 4), (0, 7) & 가로, 세로의 길이  = 3
                '''

N = int(input())
matrix = [[' ' for _ in range(N)] for _ in range(N)]
star(0, 0, N)
for r in range(N):
    print(''.join(matrix[r]))