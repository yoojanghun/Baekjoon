# 피로도, 처리량, 회복량, 최대 피로도
# A    , B    , C    , M
tired = 0
totalWork = 0

A, B, C, M = map(int, input().split())
for i in range(24):
    if A > M:
        break
    if tired + A <= M:
        totalWork += B
        tired += A
    else:
        tired -= C
        if tired < 0:
            tired = 0

print(totalWork)