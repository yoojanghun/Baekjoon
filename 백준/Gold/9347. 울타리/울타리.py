import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
directions = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 10**9

T = int(input().strip())
for _ in range(T):
    R, C = map(int, input().split())
    garden = [list(map(int, input().split())) for _ in range(R)]
    
    # 방문 배열에 “깨야 하는 울타리(=1)을 최소로 부수고 도달 가능한 값”을 저장
    dist = [[INF]*C for _ in range(R)]
    hq = []
    
    # 테두리(침입 가능 위치)에서 초기화
    for x in range(C):
        # 위쪽 테두리 (0, x)
        dist[0][x] = garden[0][x]
        heapq.heappush(hq, (garden[0][x], 0, x))
        # 아래쪽 테두리 (R-1, x)
        dist[R-1][x] = garden[R-1][x]
        heapq.heappush(hq, (garden[R-1][x], R-1, x))
    for y in range(R):
        # 왼쪽 테두리 (y, 0)
        dist[y][0] = garden[y][0]
        heapq.heappush(hq, (garden[y][0], y, 0))
        # 오른쪽 테두리 (y, C-1)
        dist[y][C-1] = garden[y][C-1]
        heapq.heappush(hq, (garden[y][C-1], y, C-1))
    
    # 다익스트라(울타리 부수는 비용을 가중치로)
    while hq:
        cost, y, x = heapq.heappop(hq)
        if cost > dist[y][x]:
            continue
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C:
                new_cost = cost + (1 if garden[ny][nx] == 1 else 0)
                if new_cost < dist[ny][nx]:
                    dist[ny][nx] = new_cost
                    heapq.heappush(hq, (new_cost, ny, nx))
    
    # 부수어야 하는 최대 울타리 개수 + 그때 얻을 수 있는 꽃(0인 칸) 수
    # 꽃(0) 칸만 고려
    max_break = 0
    for y in range(R):
        for x in range(C):
            if garden[y][x] == 0:
                max_break = max(max_break, dist[y][x])
    
    count = 0
    for y in range(R):
        for x in range(C):
            if garden[y][x] == 0 and dist[y][x] == max_break:
                count += 1
    
    print(max_break, count)
