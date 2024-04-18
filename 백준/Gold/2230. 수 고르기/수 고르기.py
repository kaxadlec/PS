from sys import stdin

N, M = map(int, stdin.readline().split())
arr = [int(stdin.readline()) for _ in range(N)]
arr.sort() 

min_diff = float('INF')

end_idx = 0
for st_idx in range(N):  
    while end_idx < N and arr[end_idx] - arr[st_idx] < M:
        end_idx += 1
    if end_idx == N:
        break
    min_diff = min(min_diff, arr[end_idx]-arr[st_idx])

print(min_diff)