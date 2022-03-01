# SWEA 1979. 어디에 단어가 들어갈 수 있을까

# 0: 검은색 -> 단어 적을 수 없음
# 1: 흰색 -> 단어 적을 수 있음
# 단어 길이와 흰색의 칸 수가 정확히 맞아야 해당 단어 적을 수 있음
def cnt_word_space(matrix, n, k):       # 단어가 들어갈 자리 수 세는 함수
    ans = 0                             # 최종 자리수 담을 변수
    for row in matrix:                  # 행 별로 반복하면서 살펴볼 것
        cnt = 0                         # 1의 개수 셀 변수
        cnt_list = []                   # 0과 1의 개수를 담을 리스트
        for i in range(n):
            if row[i] == 1:             # 해당 요소가 1이면
                cnt += 1                # cnt에 1을 더해줌
            elif row[i] == 0:           # 해당 요소가 0이면
                cnt_list.append(cnt)    # 앞에서 센 cnt를 리스트에 담아주고
                cnt = 0                 # 1을 셀 cnt를 초기화해줌
        cnt_list.append(cnt)            # for문을 다 돌면 cnt를 리스트에 담아줌
        ans += cnt_list.count(k)        # 단어 길이와 같은 자리 개수를 세서 최종 변수에 더해줌
    return ans


import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())    # n: 가로 세로 길이, k: 단어 길이
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    puzzle2 = list(zip(*puzzle))
    result = cnt_word_space(puzzle, n, k) + cnt_word_space(puzzle2, n, k)
    
    print('#{} {}'.format(tc, result))

