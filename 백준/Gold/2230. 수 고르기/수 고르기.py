from sys import stdin

N, M = map(int, stdin.readline().split())
arr = [int(stdin.readline()) for _ in range(N)]
arr.sort()

min_diff = float('INF')

end_flag = 0
pre_end_idx = 0
for st_idx in range(N):
    for end_idx in range(pre_end_idx, N+1):
        if end_idx == N:
            end_flag = 1
            break
        if arr[end_idx]-arr[st_idx] >= M:
            pre_end_idx = end_idx
            min_diff = min(min_diff, arr[end_idx]-arr[st_idx])
            break
    if end_flag == 1:
        break

print(min_diff)
