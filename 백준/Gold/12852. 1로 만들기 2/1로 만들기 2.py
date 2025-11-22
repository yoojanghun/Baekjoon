# 1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 2. X가 2로 나누어 떨어지면, 2로 나눈다.
# 3. 1을 뺀다.
# 연산을 사용하는 횟수의 최솟값을 출력

N = int(input())
dp = [-1] * (N+1)
dp[1] = 0

prev_num = [-1] * (N+1)
prev_num[0] = 0

for num in range(2, N+1):
    if num % 2 == 0 and num % 3 == 0:
        min = dp[num // 2]
        idx = num // 2
        if dp[num // 3] < min:
            min = dp[num // 3]
            idx = num // 3
        if dp[num - 1] < min:
            min = dp[num - 1]
            idx = num - 1
        dp[num] = min + 1
        prev_num[num] = idx
    else:
        if num % 2 == 0:
            min = dp[num // 2]
            idx = num // 2
            if dp[num - 1] < min:
                min = dp[num - 1]
                idx = num - 1
            dp[num] = min + 1
            prev_num[num] = idx

        if num % 3 == 0:
            min = dp[num // 3]
            idx = num // 3
            if dp[num - 1] < min:
                min = dp[num - 1]
                idx = num - 1
            dp[num] = min + 1
            prev_num[num] = idx

        if num % 2 != 0 and num % 3 != 0:
            dp[num] = dp[num - 1] + 1
            prev_num[num] = num - 1

print(dp[N])

i = N
print(i, end=" ")
while prev_num[i] >= 0:
    print(prev_num[i], end=" ")
    i = prev_num[i]