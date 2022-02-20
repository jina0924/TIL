import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    sum_list = [0] * 202                # 행, 열, 대각선의 총합을 담을 리스트
    for i in range(100):
        row_sum, col_sum = 0, 0         # 행, 열의 총합 변수
        for j in range(100):
            row_sum += arr[i][j]        # 각 행의 합
            col_sum += arr[j][i]        # 각 열의 합
        sum_list[i] = row_sum           # 1~100번째까지는 각 행의 합을
        sum_list[i + 100] = col_sum     # 101~200번째까지는 각 열의 합을 담음
    nw_sum, ne_sum = 0, 0               # 북서방향 대각선, 북동방향 대각선의 총합 변수
    for i in range(100):
        nw_sum += arr[i][i]             # 북서방향 대각선 총합
        ne_sum += arr[i][99-i]          # 북동방향 대각선 총합
    sum_list[200] = nw_sum              # 총합 리스트의 뒤에서 두번째에 북서방향 총합을 담고
    sum_list[201] = ne_sum              # 총합 리스트 마지막에 북동방향 대각선 총합을 담음
    ans = max(sum_list)
    
    print('#{} {}'.format(tc, ans))

