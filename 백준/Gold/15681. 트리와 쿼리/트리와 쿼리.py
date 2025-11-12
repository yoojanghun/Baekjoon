import sys
sys.setrecursionlimit(100000)

N, R, Q = map(int, input().split())         # N: 노드 수, R: 루트 번호, Q: 쿼리 수
edges = []
for _ in range(N-1):
    edge = tuple(map(int, input().split()))
    edges.append(edge)

sub_root = []
for root in range(Q):
    root = int(input())
    sub_root.append(root)

graph = [[] for _ in range(N+1)]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

size = [0] * (N+1)
def makeTree(currentNode, parent):
    if parent in graph[currentNode]:
        graph[currentNode].remove(parent)

    size[currentNode] = 1
    for child in graph[currentNode]:
        makeTree(child, currentNode)
        size[currentNode] += size[child]

makeTree(R, -1)
for root in sub_root:
    print(size[root])