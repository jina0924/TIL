# SWEA 4861. 회문
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

T = int(input())

for tc in range(1, T+1):
    # nxn 크기의 글자판
    # 길이가 m인 회문 찾기
    n, m = map(int, input().split())
    matrix = [input() for _ in range(n)]
    for i in range(n):                          # 가로 방향 살펴보기
        for j in range(n-m+1):                  # 회문 길이만큼 잘라보기 위한 범위
            if palindrome(matrix[i][j:j+m]):    # 만약 자른 문자열이 회문이라면
                ans = matrix[i][j:j+m]          # 답에 해당 문자열 저장
                break
            col_word = ''                       # 세로 방향으로 살펴보기
            for k in range(m):                  # 세로로 길이 m만큼 내려가면서
                col_word += matrix[j+k][i]      # 세로방향 & 길이 m인 문자열 만들기
            if palindrome(col_word):            # 세로방향 문자열의 회문 판별
                ans = col_word

    print('#{} {}'.format(tc, ans))

