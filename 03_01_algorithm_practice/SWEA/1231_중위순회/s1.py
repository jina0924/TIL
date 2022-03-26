# SWEA 1231. 중위순회

import sys
sys.stdin = open('input.txt')

def in_order(node):
    global ans
    if node:
        in_order(tree[node][0])
        ans += tree[node][1]
        in_order(tree[node][2])
    return

for tc in range(1, 11):
    n = int(input())        # n: 정점의 총 수
    tree = [[0 for _ in range(3)] for _ in range(n+1)]      # 트리
    for _ in range(n):
        data = input().split()
        idx, letter = int(data[0]), data[1]                 # idx: 정점 번호, letter: 정점의 알파벳
        tree[idx][1] = letter
        if len(data) >= 3:                                  # data 길이가 3이상이다 = 왼쪽 자식이 있다
            left = int(data[2])
            tree[idx][0] = left
            if len(data) == 4:                              # data 길이가 4다 = 오른쪽 자식도 있다
                right = int(data[3])
                tree[idx][2] = right
    ans = ''
    in_order(1)
    print(tree)
    print('#{} {}'.format(tc, ans))