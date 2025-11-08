trains_num = int(input())                       # 객차의 수
passengers = list(map(int, input().split()))
max_train_num = int(input())                    # 최대 끌 수 있는 객차 수

passengers_sum = [0] * (trains_num + 1)

# 인덱스를 1부터 시작
for i in range(1, trains_num + 1):
    passengers_sum[i] += passengers_sum[i-1] + passengers[i-1]

# dp[i][j]: i번째 기관차가 j번째 객차까지 끌었을 때 최대 승객 수
dp = [[0] * (trains_num + 1) for _ in range(4)]

# 현재 객차를 태우지 않았을 때: dp[i][j] = dp[i][j-1]
# 현재 객차를 태웠을 때: dp[i][j] = dp[i-1][j-max_train_num] + current_passengers
for i in range(1, 4):                       # 기관차 1, 2, 3
    for j in range(1, trains_num + 1):      # 객차 수
        if j >= max_train_num:
            current_passengers = passengers_sum[j] - passengers_sum[j - max_train_num]
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-max_train_num] + current_passengers)

print(dp[3][trains_num])