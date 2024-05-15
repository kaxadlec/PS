from sys import stdin
from itertools import combinations

T = int(stdin.readline())
for tc in range(T):
    N = int(stdin.readline())
    types = stdin.readline().split()
    if len(types) > 32:
        print(0)
        continue
    min_res = float('inf')
    combos = combinations(types, 3)
    for combo in combos:
        combo1 = combo[0]+combo[1]
        combo2 = combo[0]+combo[2]
        combo3 = combo[1]+combo[2]
        set_combo1 = set(combo1)
        set_combo2 = set(combo2)
        set_combo3 = set(combo3)
        res = len(set_combo1) + len(set_combo2) + len(set_combo3) - 12
        min_res = min(min_res, res)

    print(min_res)
