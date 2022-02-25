# SWEA 1216. 회문2

def palindrome(elem):                           # 회문 판별 함수
    if elem == elem[::-1]:                      # 입력받은 요소를 뒤집었을 때 원본과 같은지 판별
        return True
    return False

import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    tc_num = int(input())
    matrix_row = [input() for _ in range(100)]  # 가로줄 회문 판별 용도
    matrix_col = list(zip(*matrix_row))         # 세로줄 회문 판별 용도
    max_pal = 1                                 # 가장 긴 회문 길이 담을 변수
    for i in range(100):                        # i: 행(또는 열)을 차례로 방문할 인덱스
        for l in range(2, 101):                 # l: 판별할 단어의 길이
            for j in range(100-l+1):            # j: 단어 길이의 시작 인덱스
                if palindrome(matrix_row[i][j:j+l]):    # 가로 방향
                    if max_pal < l:             # 만약 기존의 값보다 더 긴 회문을 찾았다면
                        max_pal = l             # 회문값을 현재 회문 길이로 바꿔줌
                        continue                # 이미 l에 해당하는 길이의 회문을 찾았으므로 세로방향 볼 필요 없음
                elif palindrome(matrix_col[i][j:j+l]):  # 세로 방향
                    if max_pal < l:
                        max_pal = l
                    break

    print('#{} {}'.format(tc, max_pal))

