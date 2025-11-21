N, S, E, M = map(int, input().split())

graph = []
adj = [[] for _ in range(N)]
for _ in range(M):
    start, end, price = map(int, input().split())
    graph.append((start, end, -price))
    adj[start].append(end)

money = list(map(int, input().split()))

dist = [-float("inf")] * N
def bellmanford(graph, s):
    dist[s] = money[s]
    weighted_graph = []
    for (u, v, w) in graph:
        weighted_graph.append((u, v, w + money[v]))

    for _ in range(N-1):
        for (u, v, w) in weighted_graph:
            if dist[u] + w > dist[v]:
                dist[v] = dist[u] + w

    # 만약 마지막 노드에 도착 못 했다면, 마지막 노드의 dist는 무한대일 것이다
    if dist[E] == -float("inf"):
        print("gg")
        return

    # 마지막 노드가 무한대가 아니더라도 cycle에 빠져버리면 gg가 나올 수 있다
    for (u, v, w) in weighted_graph:
        if dist[u] + w > dist[v]:
            DFS(v)

    print(dist[E])

visited = [False] * N
stack = []
def DFS(start):
    stack.append(start)
    while stack:
        node = stack.pop()
        if node == E:
            print("Gee")
            exit()
        if not visited[node]:
            visited[node] = True
        for v in adj[node]:
            if not visited[v]:
                stack.append(v)

bellmanford(graph, S)