# make-set(u): u를 유일한 원소로 갖는 집합
#              arr[u] = u로 초기화
# find-set(u): u가 속한 집합 return
#              return arr[u]
# union(u, v): 원소 u가 속한 집합과 원소 v가 속한 집합을 합집합
#              arr[v]를 arr[u]의 값으로 변경

# arr 배열을 트리 구조로 구현
# arr[u]는 u의 부모를 나타냄
# arr[u] = u 이면 u가 루트 노드

n, m = map(int, input().split())

def union(u, v):
    u = find_set(u)
    v = find_set(v)
    if u != v:
        arr[v] = u

def find_set(u):
    r = u
    while r != arr[r]:      # root 노드 찾음
        r = arr[r]
    while u != arr[u]:      # u는 r과 같은 과정을 거침
        temp = arr[u]
        arr[u] = r
        u = temp            # temp대신 그냥 arr[u]넣으면 안됨
                            # 이미 arr[u] = r로 코드가 업데이트 되었기 때문
    return arr[u]

arr = [-1] * (n+1)
for u in range(n+1):
    arr[u] = u              # 원소 0 => 집합 0, 원소 1 => 집합 1 ...

results = []
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

# 재귀 버전: arr[u]로 u의 부모를 재귀적으로 찾는다
# def find_set(u):
#     if arr[u] == u:
#         return u
#     arr[u] = find_set(arr[u])