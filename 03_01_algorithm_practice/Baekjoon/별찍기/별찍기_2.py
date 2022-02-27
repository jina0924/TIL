# 백준 2439번 별 찍기-2

N = int(input())
for i in range(1, N+1):
    stars = '*' * i
    print(stars.rjust(N))       # str.rjust(width): 문자열 길이 width만큼 오른쪽 정렬