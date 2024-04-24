from sys import stdin

T = int(stdin.readline())
for tc in range(T):
    k = int(stdin.readline())
    n = int(stdin.readline())
    dp = [[0]*(n+1) for _ in range(k+1)]
    for ho in range(1, n+1):
        dp[0][ho] = ho

    for floor in range(1, k+1):
        for ho in range(1, n+1):
            if ho == 1:
                dp[floor][ho] = 1
            else:
                dp[floor][ho] = dp[floor][ho-1] + dp[floor-1][ho]

    print(dp[k][n])