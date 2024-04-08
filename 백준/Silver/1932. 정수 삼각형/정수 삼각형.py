from sys import stdin

n = int(stdin.readline())
dp = list([0]*i for i in range(1, n+1))
tri = []
for _ in range(n):
    el = list(map(int, stdin.readline().split()))
    tri.append(el)

dp[0][0] = tri[0][0]
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + tri[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + tri[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + tri[i][j]
max_res = 0
for j in range(n):
    res = dp[n-1][j]
    if res > max_res:
        max_res = res

print(max_res)
