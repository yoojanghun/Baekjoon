N, S = map(int, input().split())
arr = list(map(int, input().split()))
start = 0
end = 0
current_sum = arr[0]
min_length = N + 1
while end < N:
    if current_sum < S:
        end += 1
        if end < N:
            current_sum += arr[end]
    else:                                   # 부분합이 S 이상
        if end - start + 1 < min_length:
            min_length = end - start + 1
        if start < end:
            current_sum -= arr[start]
            start += 1
        else:
            end += 1
            if end < N:
                current_sum += arr[end]

if min_length > N:
    print(0)
else:
    print(min_length)