import sys
sys.setrecursionlimit(10**6)

node_num = int(input())
edge_num = int(input())
graph = [[] for _ in range(node_num + 1)]
for _ in range(edge_num):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (node_num + 1)
cnt = 0
def dfs(start):
    global cnt
    visited[start] = True
    for neighbor in graph[start]:
        if not visited[neighbor]:
            cnt += 1
            dfs(neighbor)

dfs(1)
print(cnt)