from sys import stdin

n, m = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            dp[i][j] = board[i][j]
        elif j == 0:
            dp[i][j] = board[i][j] + dp[i-1][j]
        elif i == 0:
            dp[i][j] = board[i][j] + dp[i][j-1]
        else:
            dp[i][j] = board[i][j] + max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

print(dp[n-1][m-1])


