import sys
sys.stdin = open('input.txt')

def binary_search(num, goal):
    start, end, cnt = 1, num, 0     # 시작 페이지, 끝 페이지, 탐색 횟수
    while start <= end:             # 시작 페이지가 끝 페이지 이하일 경우
        mid = int((start + end)/2)
        cnt += 1                    # 중간 페이지 찾을때마다 횟수 1 증가
        if mid == goal:             # 중간 페이지가 지정된 페이지와 같다면
            return cnt              # 함수 끝내기
        elif mid < goal:            # 중간 페이지가 지정 페이지보다 앞에 있다면
            start = mid             # 중간 페이지부터 다시 시작
        else:                       # 중간 페이지가 지정 페이지보다 뒤에 있다면
            end = mid               # 중간 페이지까지 다시 시작
    return cnt

T = int(input())

for tc in range(1, T+1):
    # p: 책 전체 쪽 수, pa: a가 찾을 쪽 번호, pb: b가 찾을 쪽 번호
    p, pa, pb = map(int, input().split())
    cnt_a, cnt_b = binary_search(p, pa), binary_search(p, pb)
    if cnt_a < cnt_b:
        ans = 'A'
    elif cnt_a > cnt_b:
        ans = 'B'
    else:
        ans = 0
    print('#{} {}'.format(tc, ans))

