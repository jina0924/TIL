# SWEA 1215. 회문1

def palindrome(my_str):                         # 회문 판별 함수
    if len(my_str) < 2:                         # 2글자 미만의 문자열이면 회문
        return True
    else:                                       # 2글자 이상이라면
        if my_str[0] == my_str[-1]:             # 처음 문자와 마지막 문자가 같다면
            return palindrome(my_str[1:-1])     # 해당 문자들을 제외하고 다시 회문 판별
        else:                                   # 처음 문자와 마지막 문자가 다르다면
            return False                        # 회문 아님

import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())                            # 찾아야 하는 회문의 길이
    matrix = [input() for _ in range(8)]        # 8x8만큼의 글자판 만들기
    cnt = 0                                     # cnt: 회문의 총 개수
    for i in range(8):
        for j in range(8-n+1):                  # 가로방향 단어
            if palindrome(matrix[i][j:j+n]):    # 만약 길이가 n만큼의 회문이라면
                cnt += 1                        # 회문 개수 1 더해줌
            col_word = ''                       # 세로방향 단어
            for k in range(n):
                col_word += matrix[j+k][i]
            if palindrome(col_word):
                cnt += 1
    ans = cnt

    print('#{} {}'.format(tc, ans))

