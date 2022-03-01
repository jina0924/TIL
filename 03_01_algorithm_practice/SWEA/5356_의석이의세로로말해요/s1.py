# SWEA 5356. 의석이의 세로로 말해요

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    words = [[0] * 15 for _ in range(5)]        # 주어진 문자열의 길이는 1이상 15이하. 5개의 문자
    for i in range(5):                          # 5개의 문자열에 대해
        word = input()                          # 문자열을 입력받고
        for j in range(len(word)):              # 문자열의 길이만큼 반복하면서
            words[i][j] = word[j]               # 전체를 입력할 2차원 배열에 배치함
    vertical_word = ''                          # 세로 읽기를 최종 출력할 변수
    for c in range(15):                         # 세로로 보기 위해 열을 먼저 기준잡고
        for r in range(5):                      # 행을 옮겨가면서
            if words[r][c]:                     # 만약 해당 요소가 0이 아니라면
                vertical_word += words[r][c]    # 세로 읽기 변수에 더해줌
    print('#{} {}'.format(tc, vertical_word))

