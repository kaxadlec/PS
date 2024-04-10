from sys import stdin

N = int(stdin.readline())
# dp[i][j] 계단의 길이가 i일때, 끝 자리가 j 인 수의 개수
dp = [[0]*10 for _ in range(102)]

# N이 1일때
dp[1][0] = 0
for j in range(1, 10):
    dp[1][j] = 1

# N이 2 이상 일때,
for i in range(2, 101):
    for j in range(0, 10):
        if j == 0:
            dp[i][j] = dp[i-1][1] % (10**9)
        elif j == 9:
            dp[i][j] = dp[i-1][8] % (10**9)
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % (10**9)

print(sum(dp[N]) % (10**9))
