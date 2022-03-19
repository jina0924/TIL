# SWEA 1224. 계산기

number = '0123456789'
icp = {'+': 1, '*': 2, '(': 3}      # icp: in-coming priority
isp = {'+': 1, '*': 2, '(': 0}      # isp: in-stack priority

def postfix(arr):                   # 후위표기식 반환할 함수
    result = ''                     # 결과값 담을 빈 문자열
    stack = []                      # 우선순위에 따라 넣고 뺄 스택
    for elem in arr:                # 넘겨받은 배열의 각 요소를 살펴봄
        if elem in number:          # 만약 해당 요소가 숫자라면
            result += elem          # 바로 결과값에 더해줌
        elif elem == '(':           # 만약 요소가 여는 괄호라면
            stack.append(elem)      # 스택에 쌓아줌
        elif elem == ')':           # 만약 닫는 괄호라면
            while stack[-1] != '(': # 여는 괄호를 만날때까지
                result += stack.pop()   # 스택의 요소들을 꺼내서 결과값에 더해줌
            stack.pop()             # 여는 괄호 버림
        else:                       # 해당 요소가 연산자라면
            while isp.get(stack[-1]) >= icp.get(elem):  # 우선순위가 낮은 연산자를 만날때까지
                result += stack.pop()   # pop한 값을 결과값에 더해줌
            stack.append(elem)      # while문을 만나지 않았다면 스택이 비어있다는 의미이므로 스택에 넣어줌
    while stack:                    # 스택에 아직 연산자가 남아있다면
        result += stack.pop()       # 결과값에 차례로 연산자 더해줌
    return result

def calc(arr):                      # 후위표기식 계산할 함수
    stack = []                      # 숫자 담을 빈 스택
    for elem in arr:                # 후위표기식 요소 앞에서부터 살펴봄
        if elem in number:          # 만약 요소가 숫자라면
            stack.append(int(elem)) # 숫자로 변환해서 스택에 쌓아줌
        else:                       # 만약 요소가 연산자라면
            b = stack.pop()         # 맨 위에 있는 요소를 먼저 꺼내고
            a = stack.pop()         # 두번째로 위에 있는 요소를 꺼내서
            if elem == '+':         # 연산자가 더하기일 땐
                stack.append(a + b) # 두 수를 더해서 스택에 다시 쌓아줌
            else:                   # 연산자가 곱하기라면
                stack.append(a * b) # 두 수를 곱해서 스택에 다시 쌓아줌
    return stack.pop()              # 스택에 마지막까지 남아있는 수를 반환해줌

import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    n = int(input())
    sentence = input()
    ans = calc(postfix(sentence))
    print('#{} {}'.format(tc, ans))

