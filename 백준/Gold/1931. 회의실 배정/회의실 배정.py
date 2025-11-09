N = int(input())            # 회의의 수

meeting_list = list()
for _ in range(N):
    start, end = map(int, input().split())
    meeting_list.append((start, end))

meeting_list.sort(key=lambda x: (x[1],x[0]))

result = [meeting_list[0]]
for meeting in meeting_list[1:]:
    if meeting[0] >= result[-1][1]:
        result.append(meeting)

print(len(result))