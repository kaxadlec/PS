N = int(input())
rooms = [tuple(map(int, input().split())) for _ in range(N)]
rooms_sorted = sorted(rooms, key=lambda x: (x[1], x[0]))
cnt = 0
for i in range(len(rooms_sorted)):
    if i == 0:
        current = rooms_sorted[i]
        cnt += 1
    else:
        if current[1] <= rooms_sorted[i][0]:
            current = rooms_sorted[i]
            cnt += 1

print(cnt)
