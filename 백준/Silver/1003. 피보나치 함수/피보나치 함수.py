import sys

T = int(input())
for tc in range(T):
    n = int(sys.stdin.readline())
    dp = [0]*42
    dp[0] = 1
    dp[1] = 0
    dp[2] = 1
    for i in range(3, 42):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[n], dp[n+1])

