def bubble_sort(arr, N, K):
    count = 0
    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1
            if count == K:
                return arr
    if count < K:
        return [-1]

N, K = map(int, input().split())            # N: 배열 크기, K: 교환 횟수
arr = list(map(int, input().split()))       # arr: 입력 배열

results = bubble_sort(arr, N, K)
print(" ".join(map(str, results)))