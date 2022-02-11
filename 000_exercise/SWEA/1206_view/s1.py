import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    # 가로의 길이를 변수 row에 담음 -> 나중에 for문으로 각 건물들을 살펴보기 위해
    row = int(sys.stdin.readline())
    # 건물 높이들을 담은 리스트를 만듦
    buildings = list(map(int, sys.stdin.readline().split()))
    # 조망권이 확보된 건물수를 담을 초기 변수 cnt를 0으로 설정해둠
    cnt = 0
    # 보고자 하는 건물 양 옆 두 건물씩 봐야함
    # 인덱스 값을 2부터 row-3까지 보기 위해 range(2, row-2)로 둠
    for i in range(2, row-2):
        # 해당 건물의 왼쪽 두 번째 건물과의 차이
        left2 = buildings[i] - buildings[i-2]
        # 해당 건물의 왼쪽 첫 번째 건물과의 차이
        left1 = buildings[i] - buildings[i-1]
        # 해당 건물의 오른쪽 첫 번째 건물과의 차이
        right1 = buildings[i] - buildings[i+1]
        # 해당 건물의 오른쪽 두 번째 건물과의 차이
        right2 = buildings[i] - buildings[i+2]
        # 해당 건물의 조망권을 한번에 비교하기 위해 한 리스트에 담아둠
        views = [left2, left1, right1, right2]
        # 각각의 조망권을 살펴보는데
        for view in views:
            # 조망권의 값이 음수라면 해당 건물근처에 더 높은 건물이 있다는 의미이므로
            if view < 0:
                # for문을 탈출한다
                break
        # for문 탈출 조건을 만나지 않았다 = 조망권을 해치는 경우가 없었다
        else:
            # views 리스트에서 가장 작은 값이 해당 건물에 확보된 조망권이다
            cnt += min(views)

    print('#{} {}'.format(tc, cnt))