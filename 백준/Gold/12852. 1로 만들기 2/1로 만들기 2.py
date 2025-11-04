import sys
N = int(sys.stdin.readline())
dp = [0] * (N + 1)
dp2 = [0] * (N + 1)

dp[1] = 0
dp2[1] = 0
for i in range(2, N + 1):
    minLoc = i - 1
    dp[i] = dp[minLoc] + 1
    dp2[i] = minLoc

    if i % 2 == 0:
        minLoc = i - 1 if dp[i - 1] < dp[i // 2] else i // 2
        dp[i] = dp[minLoc] + 1
        dp2[i] = minLoc

    if i % 3 == 0:
        minLoc = i - 1 if dp[i - 1] < dp[i // 3] else i // 3
        dp[i] = dp[minLoc] + 1
        dp2[i] = minLoc

    if i % 2 == 0 and i % 3 == 0:
        minLoc = i // 2 if dp[i // 2] < dp[i // 3] else i // 3
        dp[i] = dp[minLoc] + 1
        dp2[i] = minLoc 

print(dp[N])
print(N, end=" ")
while dp2[N] >= 1:
    print(dp2[N], end=" ")
    N = dp2[N]
