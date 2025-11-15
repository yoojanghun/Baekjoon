N = int(input())
planet = []
for i in range(N):                                     # i: 행성의 node 번호
    x, y, z = map(int, input().split())
    planet.append((i, x, y, z))

x_sorted_planet = sorted(planet, key=lambda x: x[1])
y_sorted_planet = sorted(planet, key=lambda x: x[2])
z_sorted_planet = sorted(planet, key=lambda x: x[3])

edges = []
for i in range(N-1):
    a, x1, _, _ = x_sorted_planet[i]
    b, x2, _, _ = x_sorted_planet[i+1]
    edges.append((abs(x1-x2), a, b))

    c, _, y1, _ = y_sorted_planet[i]
    d, _, y2, _ = y_sorted_planet[i+1]
    edges.append((abs(y1-y2), c, d))

    e, _, _, z1 = z_sorted_planet[i]
    f, _, _, z2 = z_sorted_planet[i+1]
    edges.append((abs(z1-z2), e, f))

def find_set(u):
    r = u
    while r != nodes[r]:
        r = nodes[r]
    while u != nodes[u]:
        temp = nodes[u]
        nodes[u] = r
        u = temp
    return nodes[u]

def union(u, v):
    u = find_set(u)
    v = find_set(v)
    if u != v:
        nodes[v] = u

nodes = [None] * N
for i in range(N):
    nodes[i] = i

mst = []
edges.sort()
for w, u, v in edges:
    if find_set(u) != find_set(v):
        mst.append(w)
        union(u, v)

print(sum(mst))