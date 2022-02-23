import sys
sys.stdin = open('input.txt')

T = int(input())
a = [x for x in range(1, 13)]

for tc in range(1, T+1):
    n, k = map(int, input().split())    # n : 부분집합 원소의 수, k : 부분집합의 합
    ans = 0                             # 조건을 만족하는 부분집합의 개수
    for i in range(1 << 12):            # a의 부분집합의 개수만큼 살펴보기
        cnt, sum_subset = 0, 0          # cnt: 부분집합 원소의 개수, sum_subset: 부분집합의 합
        for j in range(12):             # 원소의 수 만큼 비트를 비교
            if i & (1 << j):            # 해당 원소가 부분집합에 들어갈 수 있다면
                sum_subset += a[j]      # 부분집합의 합에 더해주고
                cnt += 1                # 부분집합 원소의 개수를 1개 세어줌
        # 만약 부분집합의원소의 개수와 그 합이 조건을 만족한다면
        if cnt == n and sum_subset == k:
            ans += 1                    # 부분집합 개수를 1개 더해줌

    print('#{} {}'.format(tc, ans))

