# SWEA 1234. 비밀번호

def short_pwd(arr, n):                  # 짧은 비밀번호 반환하는 함수
    my_stack = []                       # 빈 스택
    for i in range(n):                  # 인덱스로 접근해서 각 요소 살펴봄
        if my_stack:                    # 만약 스택에 요소가 있고
            if arr[i] == my_stack[-1]:  # 스택의 마지막 요소와 지금 살펴보는 값이 같다면
                my_stack.pop()          # 스택에서 해당 요소를 빼냄
            else:                       # 스택의 마지막 요소와 지금 살펴보는 값이 다르다면
                my_stack.append(arr[i]) # 스택에 해당 요소를 집어넣음
        else:                           # 만약 스택이 비어있다면 반복되는 숫자가 없다는 뜻이므로
            my_stack.append(arr[i])     # 스택에 해당 숫자를 쌓아줌
    return ''.join(my_stack)            # 리스트를 문자열로 붙여서 반환


import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n, password = input().split()
    n = int(n)
    ans = short_pwd(password, n)
    print('#{} {}'.format(tc, ans))

