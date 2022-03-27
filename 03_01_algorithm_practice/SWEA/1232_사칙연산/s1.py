# SWEA 1232. 사칙연산

import sys
sys.stdin = open('input.txt')

def calc(node):
    if node:
        left = calc(tree[node][0])
        right = calc(tree[node][2])
        if tree[node][3] == '+':
            tree[node][3] = left + right
        elif tree[node][3] == '-':
            tree[node][3] = left - right
        elif tree[node][3] == '*':
            tree[node][3] = left * right
        elif tree[node][3] == '/':
            tree[node][3] = left / right
    return tree[node][3]

for tc in range(1, 11):
    n = int(input())
    tree = [[0, 0, 0, 0] for _ in range(n+1)]       # 왼쪽, 부모, 오른쪽, 자기 값
    for i in range(n):
        data = input().split()
        parent, value = int(data[0]), data[1]
        if len(data) == 2:
            value = int(value)
        tree[parent][3] = value
        if len(data) == 4:
            left, right = int(data[2]), int(data[3])
            tree[parent][0], tree[parent][2] = left, right
            tree[left][1] = tree[right][1] = parent

    ans = calc(1)

    print('#{} {}'.format(tc, int(ans)))

