# SWEA 1234. 비밀번호

def short_pwd(arr, n):                  # 짧은 비밀번호 반환하는 함수
    my_stack = [None] * n
    top = -1
    for i in range(n):                  # 인덱스로 접근해서 각 요소 살펴봄
        if top != -1 and arr[i] == my_stack[top]:
            my_stack[top] = None
            top -= 1
        else:
            top += 1
            my_stack[top] = arr[i]
    # return ''.join(my_stack)


import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n, password = input().split()
    n = int(n)
    ans = short_pwd(password, n)
    print('#{} {}'.format(tc, ans))