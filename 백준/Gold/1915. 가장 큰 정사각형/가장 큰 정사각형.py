from sys import stdin

n, m = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().rstrip())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
result = 0
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = board[i][j]
        elif board[i][j] == 1 and dp[i-1][j-1] >= 1 and dp[i][j-1] >= 1 and dp[i-1][j] >= 1:
            square_num = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
            num = square_num ** (0.5)
            dp[i][j] = (num+1)**2
            
        else:
            dp[i][j] = board[i][j]
        
        result = max(result, dp[i][j])
# print(dp)
print(int(result))