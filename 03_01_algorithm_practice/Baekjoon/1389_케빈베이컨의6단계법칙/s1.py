# 백준 1389번 케빈 베이컨의 6단계 법칙

# 너비우선탐색인 이유: 해당 사람의 친구들을 모두 살펴보고(너비우선)
# 그 친구들의 친구들을 살펴보기 때문
def kevin_bacon(person):
    queue = [person]
    visited = [0] * (n+1)
    visited[person] = 1

    while queue:
        person = queue.pop(0)
        for i in range(n+1):
            if Graph[person][i] and not visited[i]: # 인자값인 사람과 친구면서 아직 방문하지 않았다면
                queue.append(i)                     # 방문 리스트에 올려주고
                visited[i] = visited[person] + 1    # 방문 깊이 적어둠

    return sum(visited) - n

import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())        # n: 유저의 수, m: 친구 관계의 수
Graph = [[0 for _ in range(n+1)] for _ in range(n+1)]   # 친구 관계 그래프
for _ in range(m):
    a, b = map(int, input().split())
    Graph[a][b] = Graph[b][a] = 1
total = kevin_bacon(1)                  # 케빈 베이컨의 수 첫 번째 사람의 값으로 초기화
ans = 1                                 # 케빈 베이컨의 수가 가장 작은 사람 초기값
for i in range(2, n+1):                 # 두 번째 사람부터 반복하면서
    total2 = kevin_bacon(i)
    if total > total2:                  # 만약 더 작은 케빈 베이컨 수가 나온다면
        total = total2                  # 비교할 케빈 베이컨 값을 저장하고
        ans = i                         # 해당 인덱스 값이 케빈 베이컨이 가장 작은 사람
print(ans)