from sys import stdin

N = int(stdin.readline())
dp = [float('INF')]*(N+1)
dp[0] = 0
for i in range(1, N+1):
    divided_num = i**(1/2)
    if divided_num.is_integer():
        dp[i] = 1
    else:
        int_divided_num = int(divided_num)
        half_num = int(i/2)
        for j in range(int(half_num**(1/2)), int_divided_num+1):
            dp[i] = min(dp[i], dp[j**2] + dp[i-j**2])

print(dp[N])