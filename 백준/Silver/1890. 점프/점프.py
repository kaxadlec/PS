from sys import stdin

N = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
dp = [[0]*101 for _ in range(101)]

for i in range(N):
    for j in range(N):
        if board[i][j] == 0:
            continue
        if i == 0 and j == 0:
            dp[i + board[i][j]][j] += 1
            dp[i][j + board[i][j]] += 1
        if dp[i][j]:
            dp[i+board[i][j]][j] += dp[i][j]
            dp[i][j+board[i][j]] += dp[i][j]

print(dp[N-1][N-1])