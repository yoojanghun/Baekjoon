N = int(input())
mod = 1_000_000_000

# dp[숫자 길이][마지막 숫자][비트 마스크]
dp = [[[0] * 1024 for _ in range(10)] for _ in range(N + 1)]

# 숫자의 길이가 1일 때 가능한 계단 수의 갯수
for last_num in range(1, 10):
    dp[1][last_num][1 << last_num] = 1

for length in range(2, N + 1):
    for last_num in range(0, 10):
        for mask in range(0, 1024):
            if last_num > 0:
                dp[length][last_num][mask | 1 << last_num] += dp[length - 1][last_num - 1][mask]
            if last_num < 9:
                dp[length][last_num][mask | 1 << last_num] += dp[length - 1][last_num + 1][mask]

result = 0
for i in range(0, 10):
    result += dp[N][i][1023]       # 길이: N, 모든 수를 다 쓴 경우

print(result % mod)