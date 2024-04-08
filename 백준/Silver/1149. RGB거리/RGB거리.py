from sys import stdin

N = int(stdin.readline())
R = [0]*(N+1)
G = [0]*(N+1)
B = [0]*(N+1)
dp = [[0, 0, 0] for _ in range(N+1)]
for i in range(1, N+1):
    R[i], G[i], B[i] = map(int, stdin.readline().split())

dp[1][0] = R[1]
dp[1][1] = G[1]
dp[1][2] = B[1]
for k in range(2, N+1):
    dp[k][0] = min(dp[k-1][1], dp[k-1][2]) + R[k]
    dp[k][1] = min(dp[k-1][0], dp[k-1][2]) + G[k]
    dp[k][2] = min(dp[k-1][0], dp[k-1][1]) + B[k]

print(min(dp[N][0], dp[N][1], dp[N][2]))