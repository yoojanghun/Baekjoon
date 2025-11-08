T = int(input())

for i in range(T):
    n = int(input())
    s, t = map(int, input().split())  # s: 타이핑, t: 복붙
    time = 0
    while n > 0:
        if n % 2 == 1:
            n -= 1
            time += s
        else:
            if (n // 2) * s < t:  # 타이핑이 복붙보다 빠름
                time += (n // 2) * s
            else:                 # 복붙이 타이핑보다 빠름
                time += t
            n //= 2
    print(time)