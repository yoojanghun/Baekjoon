n, m = map(int, input().split())            # m: 연산의 개수

make_set = [n for n in range(n+1)]
results = []

def union(u, v):
    u = find_set(u)
    v = find_set(v)
    if u != v:                              # root끼리 서로 다르면
        make_set[v] = u                     # v의 root를 u로 덮어 씌움

def find_set(u):
    r = u
    while r != make_set[r]:
        r = make_set[r]                     # r: root node 로 변함
    while u != make_set[u]:
        temp = make_set[u]
        make_set[u] = r
        u = temp
    return r

for _ in range(m):
    op, u, v = map(int, input().split())
    if op == 0:
        union(u, v)
    elif op == 1:
        if find_set(u) == find_set(v):
            results.append("YES")
        else:
            results.append("NO")

for result in results:
    print(result)