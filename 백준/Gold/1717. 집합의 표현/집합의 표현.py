import sys

def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x == root_y:
        return

    if ranks[root_x] < ranks[root_y]:
        parents[root_x] = root_y
    elif ranks[root_x] > ranks[root_y]:
        parents[root_y] = root_x
    else:
        parents[root_y] = root_x
        ranks[root_x] += 1


n, m = map(int, sys.stdin.readline().split())
parents = [p for p in range(n+1)]
ranks = [0]*(n+1)
for _ in range(m):
    k, a, b = map(int, sys.stdin.readline().split())
    if k == 0:
        union(a, b)
    elif k == 1:
        if find_set(a) == find_set(b):
            print("YES")
        else:
            print("NO")
