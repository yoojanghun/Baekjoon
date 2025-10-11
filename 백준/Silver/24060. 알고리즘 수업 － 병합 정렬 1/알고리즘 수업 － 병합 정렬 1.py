def merge_sort(arr, p, r):
    if p < r:                           # p: 첫 인덱스, q: 마지막 인덱스
        q = (p + r) // 2                # q: 중간 인덱스
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)

def merge(arr, p, q, r):
    tmp = [0] * (r - p + 2)
    i, j, t = p, q+1, 1
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp[t] = arr[i]
            t += 1
            i += 1
        else:
            tmp[t] = arr[j]
            t += 1
            j += 1
    while i <= q:
        tmp[t] = arr[i]
        t += 1
        i += 1
    while j <= r:
        tmp[t] = arr[j]
        t += 1
        j += 1

    i = p
    t = 1
    while i <= r:
        arr[i] = tmp[t]
        count[0] += 1
        if count[0] == K:
            print(arr[i])
        i += 1
        t += 1

count = [0]
N, K = map(int, input().split())        # N: 배열 크기, K: 저장 횟수
arr = list(map(int, input().split()))

merge_sort(arr, 0, N-1)
if count[0] < K:
    print(-1)