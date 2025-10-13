import sys
sys.setrecursionlimit(10**4)
def select(arr, p, r, q):                    # arr에서 q번째 작은 원소 찾음
    if p == r:
        return arr[p]
    t = partition(arr, p, r)
    k = t - p + 1                            # k: p에서 t까지 길이
    if q < k:
        return select(arr, p, t-1, q)               # 왼쪽 그룹
    if q == k:
        return arr[t]                        # 찾는 원소
    else:
        return select(arr, t+1, r, q-k)

def partition(arr, p, r):
    pivot = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            count[0] += 1
            if count[0] == K:
                print(*arr)
                sys.exit(0)
    if i+1 != r:
        arr[i+1], arr[r] = arr[r], arr[i+1]
        count[0] += 1
        if count[0] == K:
            print(*arr)
            sys.exit(0)
            
    return i+1

A, Q, K = map(int, input().split())
arr = list(map(int, input().split()))

count = [0]
select(arr, 0, len(arr)-1, Q)
if count[0] < K:
    print(-1)