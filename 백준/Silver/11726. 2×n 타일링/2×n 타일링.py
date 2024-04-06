from sys import stdin

N = int(stdin.readline())
dp = [0]*1001
dp[1] = 1
dp[2] = 2
for i in range(3, 1001):
    dp[i] = dp[i-1] + dp[i-2]
    if i == N:
        break

print(dp[N] % 10007)