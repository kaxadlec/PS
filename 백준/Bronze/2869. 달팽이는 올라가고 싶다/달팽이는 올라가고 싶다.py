import math
A, B, V = map(int, input().split())

day_up = A-B
last_height = V-A


if A >= V:
    cnt = 1
else:
    up_to_last_height = (last_height / day_up)
    cnt = math.ceil(up_to_last_height)
    cnt += 1

print(cnt)
