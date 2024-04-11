from sys import stdin

dp = [0]*101
dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
for i in range(5, 101):
    dp[i] = dp[i-5] + dp[i-1]

T = int(stdin.readline())
for tc in range(T):
    N = int(stdin.readline())
    print(dp[N])