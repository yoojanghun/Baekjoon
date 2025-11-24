import sys
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N
answer = float('inf')

def dfs(start, now, cost, cnt):
    global answer

    # 모든 도시를 다 방문한 경우
    if cnt == N:
        if W[now][start] != 0:  # 시작점으로 돌아가는 길이 있는 경우만
            answer = min(answer, cost + W[now][start])
        return

    # 다음 도시 탐색
    for i in range(N):
        if not visited[i] and W[now][i] != 0:
            # 가지치기(현재 비용이 최소 answer보다 이미 큰 경우 중단)
            if cost + W[now][i] >= answer:
                continue

            visited[i] = True
            dfs(start, i, cost + W[now][i], cnt + 1)
            visited[i] = False


# 모든 도시를 출발점으로 해서 최소 비용 찾기
for i in range(N):
    visited[i] = True
    dfs(i, i, 0, 1)
    visited[i] = False

print(answer)
