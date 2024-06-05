from sys import stdin
import math

N = int(stdin.readline())
kits = list(map(int, stdin.readline().split()))
T, P = map(int, stdin.readline().split())

t_bundles = 0

for shirt in kits:
    t_bundles += math.ceil(shirt/T)

print(t_bundles)
kits_cnt = sum(kits)
print(kits_cnt // P, kits_cnt % P)
