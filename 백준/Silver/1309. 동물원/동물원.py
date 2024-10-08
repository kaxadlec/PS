from sys import stdin

N = int(stdin.readline())
dp = [[0] * 3 for _ in range(100001)]
dp[1][0], dp[1][1], dp[1][2] = 1, 1, 1
for i in range(2, N+1):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][1]) % 9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][2]) % 9901

print(sum(dp[N]) % 9901)