from sys import stdin

N, M = map(int, stdin.readline().split())
reals = list(map(int, stdin.readline().split()))
real_nums = set(reals[1:])
parties = [list(map(int, stdin.readline().split())) for _ in range(M)]
result = 0

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return
    if ranks[root_x] < ranks[root_y]:
        parents[root_x] = root_y
    elif ranks[root_x] > ranks[root_y]:
        parents[root_y] = root_x
    else:
        parents[root_y] = root_x
        ranks[root_x] += 1

parents = [x for x in range(N+1)]
ranks = [0]*(N+1)

for party in parties:
    party_nums = sorted(party[1:])
    base_num = party_nums[0]
    for num in party_nums[1:]:
        union(base_num, num)

real_roots = set()
for num in real_nums:
    real_roots.add(find(num))

for party in parties:
    real_flag = False
    party_nums = sorted(party[1:])
    for num in party_nums:
        num_root = find(num)
        if num_root in real_roots:
            real_flag = True
            break

    if not real_flag:
        result += 1

print(result)




