# NxM 배열
arr = [[1, 2, 3], [4, 5, 6], [7, 8,9]]
N = 3
for i in range(N):
    for j in range(N):
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M: # 유효 인덱스
                print(i, j, arr[ni][nj])    # 해당 인덱스 주변에 유효한 요소 프린트
        print()