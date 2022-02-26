import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    n, m = len(str1), len(str2)     # n: str1의 길이, m: st2의 길이
    for i in range(m-n+1):          # str2를 돌면서 str1이 있는지 살펴 볼 것
        if str2[i:i+n] == str1:     # 만약 슬라이싱한 문자열이 str1이랑 같다면
            ans = 1                 # ans에 1을 담고
            break                   # 반복문을 끝낸다
    else:                           # for문을 다 돌때까지 같은 문자열을 찾지 못했다면
        ans = 0                     # ans에 0을 담는다

    print('#{} {}'.format(tc, ans))

