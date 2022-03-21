# SWEA 4881. 배열최소합

total = 0                           # 배열 합을 담을 변수
def min_sum(data, r):               # 배열 최소합을 구할 함수
    global ans, total               # ans: 최종 최소합, total: 현재 배열 합
    if r == n:                      # r이 n까지 오면 더 이상 행렬 방문하지 않고 배열합 조사함
        if total < ans:             # 만약 지금 구한 합이 전에 저장한 최소값보다 작다면
            ans = total             # 최소값을 갱신해줌
        return                      # 함수 빠져나감
    elif total >= ans:              # 만약 r이 아직 n까지 안왔는데 배열합이 최소값보다 크다면
        return                      # 함수 빠져나가고 다음 함수로 넘어감
    for c in range(n):              # 행을 고정하고 열 위주로 탐색
        if not visited[c]:          # 만약 방문하지 않은 열이라면
            visited[c] = 1          # 해당 열 모두 방문했다고 표시해야함
            total += data[r][c]     # 배열합에 해당 요소값 더해줌
            min_sum(data, r+1)      # 다음 행 살펴보러 넘어감
            visited[c] = 0          # 위에 함수에서 return을 만나 돌아왔으면 현재 방문한 곳을 취소하고
            total -= data[r][c]     # 배열합도 전으로 되돌려줌

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n               # 열마다 하나씩만 방문해야 되므로 1차원 리스트
    ans = 90                        # 10 이하의 자연수만 주어지므로 최대값 30으로 초기화
    min_sum(matrix, 0)
    print('#{} {}'.format(tc, ans))

