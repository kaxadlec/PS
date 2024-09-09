from sys import stdin

T = int(stdin.readline())
dp = [[1] * 31 for _ in range(31)]

for i in range(1, 31):
    for j in range(2, 31):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

for _ in range(T):
    a, b = map(int, stdin.readline().split())
    i = a
    j = b - a + 1
    print(dp[i][j])
