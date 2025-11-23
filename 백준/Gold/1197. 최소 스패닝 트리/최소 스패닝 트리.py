V, E = map(int, input().split())
edges = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

edges.sort(key=lambda x: x[2])

make_set = [i for i in range(V+1)]

def union(u, v):
    u = find_set(u)
    v = find_set(v)
    if u != v:
        make_set[v] = u

def find_set(u):
    r = u
    while r != make_set[r]:
        r = make_set[r]
    while u != make_set[u]:
        temp = make_set[u]
        make_set[u] = r
        u = temp
    return r

total_weight = 0
for (u, v, w) in edges:
    if find_set(u) != find_set(v):
        total_weight += w
        union(u, v)

print(total_weight)