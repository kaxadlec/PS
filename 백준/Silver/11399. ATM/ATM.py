from sys import stdin
from itertools import accumulate, permutations

N = int(stdin.readline())
times = list(map(int, stdin.readline().split()))
times.sort()
print(sum(accumulate(times)))