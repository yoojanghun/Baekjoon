from math import sqrt

N, M = map(int, input().split())
nodes = [None] * (N+1)
for i in range(1, N+1):
    x, y = map(int, input().split())
    nodes[i] = (i, x, y)

edges = []
connected = []
for _ in range(M):
    node1, node2 = map(int, input().split())
    node1_x = nodes[node1][1]
    node1_y = nodes[node1][2]
    node2_x = nodes[node2][1]
    node2_y = nodes[node2][2]
    edges.append((0, node1, node2))
    connected.append((node1, node2))

for i in range(1, N+1):
    for j in range(i+1, N+1):
        if (i, j) in connected or (j, i) in connected:
            continue
        node1_x = nodes[i][1]
        node1_y = nodes[i][2]
        node2_x = nodes[j][1]
        node2_y = nodes[j][2]
        weight = sqrt((node1_x - node2_x)**2 + (node1_y - node2_y) ** 2)
        edges.append((weight, i, j))

set = [None] * (N+1)
for i in range(1, N+1):                         # make_set
    set[i] = i

def find_set(u):
    r = u
    while r != set[r]:
        r = set[r]
    while u != set[u]:
        temp = set[u]
        set[u] = r
        u = temp
    return r

def union(u, v):
    u = find_set(u)
    v = find_set(v)
    if u != v:
        set[v] = u

for i, j in connected:
    union(i, j)

edges.sort()
total_weight = 0
node_cnt = 0
for w, u, v in edges:
    if find_set(u) != find_set(v):
        total_weight += w
        union(u, v)
        node_cnt += 1
        if node_cnt == N-1:
            break

print(f"{total_weight:.2f}")