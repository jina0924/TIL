# 백준 1244번 스위치 켜고 끄기

def switch_boy(arr, pos):                   # 남학생의 스위치 바꾸기
    for i in range(pos-1, len(arr), pos):   # 남학생이 받은 번호의 배수만큼 반복돌기
        if arr[i]:                          # 만약 스위치가 1이라면
            arr[i] = 0                      # 스위치 끄기
        else:                               # 스위치가 꺼져있다면
            arr[i] = 1                      # 스위치 켜기
    return arr

def switch_girl(arr, pos):                  # 여학생의 스위치 바꾸기
    left = right = pos-1                    # 왼쪽과 오른쪽 인덱스를 가운데로 설정
    while left >= 0 and right < len(arr):   # 양쪽 인덱스가 입력받은 배열 밖으로 넘지 않을때까지 반복
        if arr[left] and arr[right]:        # 만약 왼쪽과 오른쪽 모두 1이라면
            arr[left] = arr[right] = 0      # 모든 스위치 끄기
            left -= 1                       # 왼쪽으로 한 칸 이동
            right += 1                      # 오른쪽으로 한 칸 이동
        elif arr[left] == 0 and arr[right] == 0:    # 만약 왼쪽과 오른쪽 모두 꺼져있다면
            arr[left] = arr[right] = 1      # 모두 켜기
            left -= 1                       # 왼쪽으로 한 칸 이동
            right += 1                      # 오른쪽으로 한 칸 이동
        else:                               # 왼쪽과 오른쪽의 값이 서로 다르다면
            break                           # 반복문 탈출
    return arr

import sys
sys.stdin = open('input.txt')

n = int(input())                            # n: 스위치 개수
switch = list(map(int, input().split()))    # 스위치 상태
for _ in range(int(input())):               # 입력받은 학생 수 만큼 반복 시행
    gender, position = map(int, input().split())
    if gender == 1:                         # 남학생이라면
        switch = switch_boy(switch, position)   # 남학생의 스위치 변경 함수 호출
    else:                                   # 여학생이라면
        switch = switch_girl(switch, position)  # 여학생의 스위치 변경 함수 호출

for i in range(0, n, 20):                   # 한 줄에 20개씩 출력하랬음
    print(*switch[i:i+20])                  # 스위치 사이에 빈칸 하나씩 두고 리스트 풀어서 출력