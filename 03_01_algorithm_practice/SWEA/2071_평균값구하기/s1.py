import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    my_list = list(map(int, input().split()))
    total = 0
    for num in my_list:
        total += num
    ans = round(total / 10)
    print('#{} {}'.format(tc, ans))

