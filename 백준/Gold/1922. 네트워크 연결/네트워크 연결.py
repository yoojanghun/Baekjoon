# prim algorithm
import heapq

N = int(input())                            # 컴퓨터의 수
M = int(input())                            # edge의 수

edges = []
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))
    graph[u].append((v, w))
    graph[v].append((u, w))

visited = [False] * (N+1)
def prim(graph, start):
    heap = [(0, start)]                      # (weight, node)
    total_weight = 0
    while heap:
        weight, node = heapq.heappop(heap)
        if visited[node]:
            continue
        visited[node] = True
        total_weight += weight
        for v, weight in graph[node]:
            if not visited[v]:
                heapq.heappush(heap, (weight, v))       # heapq는 (weight, v)에서 첫 번째 요소 weight를 기준으로 min heap 구성

    return total_weight

print(prim(graph, 1))