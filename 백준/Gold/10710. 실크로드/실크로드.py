from sys import stdin

N, M = map(int, stdin.readline().split())
dist = list(int(stdin.readline()) for _ in range(N))
weather = list(int(stdin.readline()) for _ in range(M))
dp = list([0]*(M-N+1) for _ in range(N))

for i in range(N):
    for j in range(M-N+1):
        if i == 0:
            if j == 0:
                dp[i][j] = dist[i] * weather[i + j]
            else:
                dp[i][j] = min(dp[i][j - 1], dist[i] * weather[i + j])
        else:
            if j == 0:
                dp[i][j] = dist[i] * weather[i + j] + dp[i-1][j]
            else:
                dp[i][j] = min(dp[i][j - 1], dist[i] * weather[i + j] + dp[i-1][j])

print(dp[N-1][M-N])