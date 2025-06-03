from sys import stdin

N, M, L = map(int, stdin.readline().split())
rest = [0] + list(map(int, stdin.readline().split())) + [L]
rest.sort()
dist = [0]*(N+2)
for i in range(1, N+2):
    dist[i] = rest[i] - rest[i - 1]


def is_possible(target):
    check = 0
    for x in range(1, N+2):
        d = dist[x]
        if d > target:
            divided_cnt = d // target
            if d % target == 0:
                check += divided_cnt - 1
            else:
                check += divided_cnt

    if check <= M:
        return True
    else:
        return False


left = 1
right = max(dist)
ans = right

while left <= right:
    mid = (left + right) // 2
    # print(mid)
    if is_possible(mid):
        # print("possible")
        right = mid - 1
        ans = min(ans, mid)
    else:
        # print("impossible")
        left = mid + 1

print(ans)