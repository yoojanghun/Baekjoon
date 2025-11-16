# N: 아이 수, M: 친구 관계 수, K: 시끄럽기 위한 최소 아이 수
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
candy = list(map(int, input().split()))
candy.insert(0, 0)

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# Union-Find
arr = [i for i in range(N+1)]

def find_set(u):
    # path compression
    if arr[u] != u:
        arr[u] = find_set(arr[u])
    return arr[u]

def union(u, v):
    u = find_set(u)
    v = find_set(v)
    if u != v:
        arr[v] = u

# union 수행 (그래프 순회로)
for i in range(1, N+1):
    for j in graph[i]:
        union(i, j)

# 그룹별 합 계산 — 반드시 find_set(i)로 root를 얻어야 함
group_size = [0] * (N+1)
group_candy = [0] * (N+1)
for i in range(1, N+1):
    root = find_set(i)           # <-- 여기 수정됨 (arr[i]가 아님)
    group_size[root] += 1
    group_candy[root] += candy[i]

# items: (그룹 인원수, 그룹 사탕수) — root인 것만
items = []
for i in range(1, N+1):
    if arr[i] == i and group_size[i] > 0:   # i가 root인지 확인
        items.append((group_size[i], group_candy[i]))

# dp[x]: x명 아이 사용해서 얻을 수 있는 최대 사탕 수, x in [0 .. K-1]
dp = [0] * K

for w, v in items:
    # w > K-1 이면 이 아이템은 넣을 수 없음(범위를 벗어나므로 루프 자체가 동작하지 않음)
    for x in range(K-1, w-1, -1):
        dp[x] = max(dp[x], dp[x-w] + v)

print(dp[K-1])
