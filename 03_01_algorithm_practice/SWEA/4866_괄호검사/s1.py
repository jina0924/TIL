# SWEA 4866. 괄호검사

def check_pair(arr):
    my_stack = []                   # 괄호 담을 스택
    for i in range(len(arr)):       # 입력받은 값을 하나하나 살펴봄
        if arr[i] != '{' and arr[i] != '(' and arr[i] != ')' and arr[i] != '}': # 괄호가 아니라면
            continue                # 다음 요소로 넘어감
        elif arr[i] == '{' or arr[i] == '(':    # 만약 여는 괄호라면
            my_stack.append(arr[i])             # 스택에 해당 괄호 넣어줌
        elif arr[i] == ')':
            if len(my_stack):                   # 스택에 여는 괄호가 있다면
                if my_stack[-1] == '(':         # 쌍을 이루는 괄호인지 살펴보고 맞다면
                    my_stack.pop()              # 해당 여는 괄호를 빼내어줌
                else:                           # 스택 마지막 값이 쌍을 이루는 괄호가 아니라면
                    return 0                    # 0을 반환함
            else:
                return 0                        # 스택에 여는 괄호가 없다면 쌍을 이루지 못하므로 0 반환
        elif arr[i] == '}':
            if len(my_stack):
                if my_stack[-1] == '{':
                    my_stack.pop()
                else:
                    return 0
            else:
                return 0
    if my_stack:                                # 스택에 요소가 있다면 아직 쌍을 이루지 못한 괄호가 있으므로
        return 0                                # 0을 반환함
    return 1


import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    my_input = input()
    ans = check_pair(my_input)
    
    print('#{} {}'.format(tc, ans))

