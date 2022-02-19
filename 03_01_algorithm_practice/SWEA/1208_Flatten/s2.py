import sys
sys.stdin = open('input.txt')

def dump(arr, n):
    arr.sort()      # 가장 큰 값과 가장 작은 값 찾기 위해 리스트 정렬
    if arr[-1] - arr[0] <= 1 or n < 1:      # 평탄화가 완료되거나 평탄화 횟수가 남지 않았을 때
        return arr[-1] - arr[0]     # 최고점과 최저점의 높이 차를 반환
    else:
        arr[-1] -= 1    # 가장 높은 상자에서 하나를 빼서
        arr[0] += 1     # 가장 낮은 높이의 상자에 하나를 더해줌
    return dump(arr, n-1)       # 위와 같은 식을 n번만큼 반복함

for tc in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))
    ans = dump(boxes, N)
    print('#{} {}'.format(tc, ans))