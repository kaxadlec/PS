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

input = sys.stdin.readline
N, E = map(int, input().split())
parents = [i for i in range(N+1)]
ranks = [0 for _ in range(N+1)]

for i in range(E):
    n1, n2 = map(int, input().split())
    union(n1, n2)

print(len(set([find_set(i) for i in range(1, N + 1)])))
