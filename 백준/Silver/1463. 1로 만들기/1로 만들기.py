# 1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 2. X가 2로 나누어 떨어지면, 2로 나눈다.
# 3. 1을 뺀다.
# 연산을 사용하는 횟수의 최솟값을 출력

N = int(input())
dp = [-1] * (N+1)
dp[1] = 0

for num in range(2, N+1):
    if num % 2 == 0 and num % 3 == 0:
        dp[num] = min(dp[num//2] + 1, dp[num//3] + 1, dp[num-1]+1)
    else:
        if num % 2 == 0:
            dp[num] = min(dp[num//2] + 1, dp[num-1]+1)

        if num % 3 == 0:
            dp[num] = min(dp[num//3] + 1, dp[num-1]+1)

        if num % 2 != 0 and num % 3 != 0:
            dp[num] = dp[num-1] + 1

print(dp[N])