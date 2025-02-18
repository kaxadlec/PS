from sys import stdin

N = int(stdin.readline())
M = int(stdin.readline())
infos = [list(map(int, stdin.readline().split())) for _ in range(N)]
plans = list(map(int, stdin.readline().split()))

def find(x):
    if parents[x] == x:
        return x
    root_node = find(parents[x])
    parents[x] = root_node
    return root_node


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:
        return
    if ranks[root_x] < ranks[root_y]:
        parents[root_x] = root_y
    else:
        if ranks[root_x] == ranks[root_y]:
            ranks[root_x] += 1
        parents[root_y] = root_x

parents = [i for i in range(N+1)]
ranks = [0]*(N+1)

for i in range(N):
    for j in range(N):
        if i < j and infos[i][j] == 1:
            union(i+1, j+1)

root = find(plans[0])
for i in plans[1:]:
    if find(i) != root:
        print("NO")
        break
else:
    print("YES")


