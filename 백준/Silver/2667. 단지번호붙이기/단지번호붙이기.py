from collections import deque

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[False] * n for _ in range(n)]

def bfs(i, j):
    cnt = 0
    queue = deque([(i, j)])
    visited[i][j] = True
    cnt += 1
    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1

    return cnt

results = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1 and not visited[i][j]:
            results.append(bfs(i, j))

results.sort()
print(len(results))
for result in results:
    print(result)