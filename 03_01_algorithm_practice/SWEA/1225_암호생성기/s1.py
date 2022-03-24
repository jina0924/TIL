# SWEA 1225. 암호 생성기

import sys
sys.stdin = open('input.txt')

cycle = [-1, -2, -3, -4, -5]
def change(data):
    idx = 0                                         # 인덱스 0부터 시작

    while True:                                     # return 만날 때까지 반복 시행
        front = data.pop(0)                         # 맨 앞에 있는 수 꺼내서
        front += cycle[idx]                         # 사이클에 해당하는 수 감소시킴
        if front <= 0:                              # 만약 계산한 수가 0보다 작거나 같으면
            data.append(0)                          # 0으로 유지해서 배열 뒤에 넣어줌
            return data                             # 암호화 완료된 배열 반환
        data.append(front)                          # return을 만나지 않았다면 배열 뒤에 계산한 값 넣어줌
        idx = (idx + 1) % 5                         # 5를 한 사이클로 돌기위해 인덱스 계산

for _ in range(1, 11):
    tc = int(input())
    pwd_list = list(map(int, input().split()))      # 입력받은 암호 배열
    ans = change(pwd_list)                          # ans: 암호화 완료된 암호 배열
    print('#{}'.format(tc), *ans)