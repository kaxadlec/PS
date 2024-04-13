from sys import stdin

N = int(stdin.readline())
ts = [0]*(N+1)
arr = [0]*(N+1)
for i in range(N):
    t, p = map(int, stdin.readline().split())
    ts[i + 1], arr[i + 1] = t, p

dp = [0]*(N+2)
for day in range(N, 0, -1):
    if day + ts[day]-1 > N:
        dp[day] = dp[day+1]
        continue
    dp[day] = max(dp[day+ts[day]] + arr[day], dp[day+1])

print(dp[1])