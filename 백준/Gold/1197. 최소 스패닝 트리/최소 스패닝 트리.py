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

    if ranks[root_x] > ranks[root_y]:
        parents[root_y] = root_x
    elif ranks[root_x] < ranks[root_y]:
        parents[root_x] = root_y
    else:
        parents[root_x] = root_y
        ranks[root_y] += 1


V, E = map(int, sys.stdin.readline().split())
edges = []
for _ in range(E):
    a, b, w = map(int, sys.stdin.readline().split())
    edges.append((a, b, w))
edges.sort(key=lambda x: x[2])
parents = [i for i in range(V+1)]
ranks = [0]*(V+1)
mst_list = []

for edge in edges:
    a, b, w = edge
    if find_set(a) == find_set(b):
        continue
    else:
        union(a, b)
        mst_list.append(w)

    if len(mst_list) == V-1:
        break

print(sum(mst_list))
