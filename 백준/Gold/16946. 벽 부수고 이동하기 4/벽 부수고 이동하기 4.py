# deque에서 append하고 popleft하면 queue로 사용 가능
from collections import deque

N, M = map(int, input().split())            # n행 m열
board = []
for _ in range(N):
    row = list(map(int, str(input())))
    board.append(row)

area_id = [[-1] * M for _ in range(N)]      # 영역의 번호 저장
area_size = []                              # 각 영역의 크기

# BFS로 영역 크기 탐색
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(sx, sy, id):
    q = deque([(sx, sy)])
    area_id[sx][sy] = id
    cnt = 1

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 0 and area_id[nx][ny] == -1:
                    area_id[nx][ny] = id
                    cnt += 1
                    q.append((nx, ny))
    return cnt

# 영역 모두 탐색
id = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 0 and area_id[i][j] == -1:
            size = bfs(i, j, id)
            area_size.append(size)
            id += 1

# 결과 배열 생성
result = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:                # 벽이면 인접 영역 크기 합산
            near_ids = set()
            total = 1                       # 부순 곳 포함

            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < N and 0 <= ny < M:
                    aid = area_id[nx][ny]
                    if aid != -1 and aid not in near_ids:
                        near_ids.add(aid)
                        total += area_size[aid]

            result[i][j] = total % 10

# 출력
for i in range(N):
    print("".join(map(str, result[i])))