# SWEA 1232. 사칙연산

import sys
sys.stdin = open('input.txt')

def calc(node):
    if node:                                        # 만약 해당 정점이 0이 아니라면
        left = calc(tree[node][0])                  # 왼쪽 자식(재귀로 파고들어서 해당 값 꺼냄)
        right = calc(tree[node][2])                 # 오른쪽 자식
        if tree[node][1] == '+':                    # 연산자에 맞춰 연산하고 부모에 그 값 저장함
            tree[node][1] = left + right
        elif tree[node][1] == '-':
            tree[node][1] = left - right
        elif tree[node][1] == '*':
            tree[node][1] = left * right
        elif tree[node][1] == '/':
            tree[node][1] = left / right
    return tree[node][1]                            # 루트에 저장된 값 반환

for tc in range(1, 11):
    n = int(input())
    tree = [[0, 0, 0] for _ in range(n+1)]          # 왼쪽, 자기 값, 오른쪽
    for i in range(n):
        data = input().split()
        parent, value = int(data[0]), data[1]       # 첫 번째 값: 정점, 두 번째 값: 연산자 혹은 수
        if len(data) == 2:                          # 데이터가 2개만 주어졌다면 연산자 없음
            value = int(value)                      # 두 번째 값 정수로 변환
        tree[parent][1] = value                     # 자기 자리에 해당 값 넣어줌
        if len(data) == 4:                          # 데이터가 4개라면 2개의 자식 주어짐
            left, right = int(data[2]), int(data[3])
            tree[parent][0], tree[parent][2] = left, right
            tree[left][1] = tree[right][1] = parent

    ans = calc(1)

    print('#{} {}'.format(tc, int(ans)))

