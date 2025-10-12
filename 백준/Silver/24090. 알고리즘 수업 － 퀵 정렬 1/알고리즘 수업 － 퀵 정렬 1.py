import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def quick_sort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q - 1)
        quick_sort(arr, q + 1, r)

def partition(arr, p, r):
    pivot = arr[r]

    i = p - 1
    for j in range(p, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            count[0] += 1
            if count[0] == K:
                print(arr[i], arr[j])
                sys.exit(0)
    if i+1 != r:
        arr[i+1], arr[r] = arr[r], arr[i+1]
        count[0] += 1
        if count[0] == K:
            print(arr[i+1], arr[r])
            sys.exit(0)

    return i+1

A, K = map(int, input().split())            # A: 배열 크기, K: 교환 횟수
arr = list(map(int, input().split()))

count = [0]
quick_sort(arr, 0, A-1)
if count[0] < K:
    print(-1)