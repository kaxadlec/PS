import itertools
import sys

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr = [i for i in range(N)]
min_diff = 21e8
for combo in itertools.combinations(arr, N // 2):
    result, diff_result = 0, 0
    diff_combo = [k for k in arr if k not in combo]
    for perm in itertools.permutations(combo, 2):
        i, j = perm
        result += board[i][j]
    for perm in itertools.permutations(diff_combo, 2):
        i, j = perm
        diff_result += board[i][j]

    diff = abs(result - diff_result)
    if diff < min_diff:
        min_diff = diff

print(min_diff)
