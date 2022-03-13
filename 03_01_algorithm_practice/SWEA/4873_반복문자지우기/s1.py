# SWEA 4873. 반복문자 지우기

def no_repeat(arr):                     # 반복문자 지운 문자열의 길이 구하는 함수
    my_stack = []                       # 빈 스택
    for elem in arr:                    # 입력받은 매개변수 하나씩 살펴보기
        if my_stack:                    # 만약 스택에 요소가 있다면
            if my_stack[-1] == elem:    # 현재 살펴보는 요소가 스택에 있다면 반복되는 문자이므로
                my_stack.pop()          # 스택에서 요소를 빼주고 다음 반복 시행함
            else:                       # 만약 스택에 없다면
                my_stack.append(elem)   # 스택에 해당 문자 넣어줌
        else:                           # 만일 스택이 비어있다면 반복되는 문자가 없다는 뜻이므로
            my_stack.append(elem)       # 스택에 요소를 채워줌
    return len(my_stack)

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    my_input = input()
    ans = no_repeat(my_input)
    print('#{} {}'.format(tc, ans))

