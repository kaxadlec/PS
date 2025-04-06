from sys import stdin
from itertools import combinations

N = int(stdin.readline())
mp, mf, ms, mv = map(int, stdin.readline().split())
gradients = [[i+1] + list(map(int, stdin.readline().split())) for i in range(N)]
min_cost = 21e8
min_cost_gradients = tuple()
result_flag = False

for i in range(1, N+1):
    for combo in combinations(gradients, i):
        # print(combo)
        zip_combo = list(zip(*combo))
        # print(zip_combo)
        sum_zip_combo = list(map(sum, zip_combo))
        # print(sum_zip_combo)
        _, p, f, s, v, c = sum_zip_combo
        # print(p, f, s, v, c)
        if p >= mp and f >= mf and s >= ms and v >= mv:
            if not result_flag:
                result_flag = True
            if min_cost > c:
                min_cost = c
                min_cost_gradients = zip_combo[0]
            elif min_cost == c:
                if min_cost_gradients > zip_combo[0]:
                    min_cost_gradients = zip_combo[0]
            # print(min_cost_gradients)
            
if result_flag:
    print(min_cost)
    print(*min_cost_gradients) 
else:
    print(-1)
   