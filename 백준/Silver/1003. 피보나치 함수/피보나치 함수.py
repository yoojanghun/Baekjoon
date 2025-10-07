# dp[0]: n = 0일 때의 결과
# dp[1]: n = 1일 때의 결과
dp = [(1, 0), (0, 1)]       # (0 호출 수, 1 호출 수)

# 0 <= n <= 40 인 자연수
for i in range(2, 41):
    a0, a1 = dp[i-1]
    b0, b1 = dp[i-2]
    dp.append((a0 + b0, a1 + b1))

T = int(input())
for i in range(T):
    n = int(input())
    print(dp[n][0], dp[n][1])