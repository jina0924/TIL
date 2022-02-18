# NxM 배열
di = [0, 1, 0, -1]  # 우하좌상(시계방향)
dj = [1, 0, -1, 0]
for k in range(4):
    ni = i + di[k]  # 현재 위치가 ni일 때 사방의 위치
    nj = j + dj[k]  # 현재 위치가 nj일 때 사방의 위치
    if 0 <= ni < N and 0 <= nj < M: # 유효 인덱스
        arr[ni][nj]