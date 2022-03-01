# 백준 2304번 창고 다각형

import sys
sys.stdin = open('input.txt')

n = int(input())
pillar = [list(map(int, input().split())) for _ in range(n)]
pillar.sort()
storage = [0 for _ in range(pillar[-1][0]+2)]

for i in range(len(pillar)):
    storage[pillar[i][0]] = pillar[i][1]

top = max(storage)
left, right = pillar[0][0], pillar[-1][0]

while storage[left] < top:
    if storage[left-1] > storage[left]:
        storage[left] = storage[left-1]
    left += 1

while storage[right] < top:
    if storage[right+1] > storage[right]:
        storage[right] = storage[right+1]
    right -= 1

ans = sum(storage[:left]) + sum(storage[right+1:]) + top * (right - left + 1)
print(ans)