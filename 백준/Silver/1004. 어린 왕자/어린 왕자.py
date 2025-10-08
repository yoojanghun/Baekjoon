import math

T = int(input())
count = 0
results = []
for i in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    for _ in range(n):
        x, y, r = map(int, input().split())
        if (math.sqrt((x1-x)**2 + (y1-y)**2) < r and math.sqrt((x2-x)**2 + (y2-y)**2) > r) or (math.sqrt((x1-x)**2 + (y1-y)**2) > r and math.sqrt((x2-x)**2 + (y2-y)**2) < r):
            count += 1
    results.append(count)
    count = 0

for result in results:
    print(result)