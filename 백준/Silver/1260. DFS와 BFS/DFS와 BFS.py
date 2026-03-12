import sys
from collections import deque
sys.setrecursionlimit(10**6)

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for edge in graph:
    edge.sort()

visited_dfs = [False] * (N+1)
result_dfs = []
def dfs(start):
    visited_dfs[start] = True
    result_dfs.append(start)
    for neighbor in graph[start]:
        if not visited_dfs[neighbor]:
            dfs(neighbor)

dfs(V)
print(*result_dfs)

visited_bfs = [False] * (N+1)
result_bfs = []
def bfs(start):
    queue = deque([start])
    visited_bfs[start] = True
    result_bfs.append(start)
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited_bfs[neighbor]:
                queue.append(neighbor)
                visited_bfs[neighbor] = True
                result_bfs.append(neighbor)

bfs(V)
print(*result_bfs)