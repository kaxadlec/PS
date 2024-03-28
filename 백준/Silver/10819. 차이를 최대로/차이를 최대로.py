import itertools

N = int(input())
arr = map(int, input().split())
max_result = 0
for perm in itertools.permutations(arr):
    result = 0
    for idx in range(N-1):
        result += abs(perm[idx] - perm[idx+1])
    if max_result < result:
        max_result = result

print(max_result)

