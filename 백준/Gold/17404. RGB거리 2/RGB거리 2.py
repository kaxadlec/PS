from sys import stdin

n = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
combinations = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]

dp = [[1001*n]*3 for _ in range(n)]
dp[0][0], dp[0][1], dp[0][2] = board[0][0], board[0][1], board[0][2]

for comb in combinations:
    if comb[0] == 0:
        dp[1][0] = 2002
        dp[1][1] = board[1][1] + dp[0][0]
        dp[1][2] = board[1][2] + dp[0][0]
    elif comb[0] == 1:
        dp[1][1] = 2002
        dp[1][0] = board[1][0] + dp[0][1]
        dp[1][2] = board[1][2] + dp[0][1]
    elif comb[0] == 2:
        dp[1][2] = 2002
        dp[1][0] = board[1][0] + dp[0][2]
        dp[1][1] = board[1][1] + dp[0][2]

    for i in range(2, n-1):
        dp[i][0] = board[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = board[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = board[i][2] + min(dp[i-1][0], dp[i-1][1])

    if comb[1] == 1:
        dp[n-1][1] = min(dp[n-1][1], board[n-1][1] + min(dp[n-2][0], dp[n-2][2]))
    elif comb[1] == 2:
        dp[n-1][2] = min(dp[n-1][2], board[n-1][2] + min(dp[n-2][0], dp[n-2][1]))
    elif comb[1] == 0:
        dp[n - 1][0] = min(dp[n - 1][0], board[n - 1][0] + min(dp[n - 2][1], dp[n - 2][2]))

print(min(dp[n-1]))
