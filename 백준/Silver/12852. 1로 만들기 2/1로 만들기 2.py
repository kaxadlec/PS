from sys import stdin

N = int(stdin.readline())
dp = [0]*(N+1)
dp[1] = 0
for k in range(2, N+1):
    dp[k] = dp[k - 1] + 1
    if k % 3 == 0:
        dp[k] = min(dp[k], dp[k//3]+1)
    if k % 2 == 0:
        dp[k] = min(dp[k], dp[k//2]+1)

cnt = dp[N]
print(cnt)
for _ in range(cnt+1):
    print(N, end=' ')
    res1 = dp[N-1]+1
    if N % 6 == 0:
        res2, res3 = dp[N//3]+1, dp[N//2]+1
        min_res = min(res1, res2, res3)
        if min_res == res1:
            N = N-1
        elif min_res == res2:
            N = N // 3
        elif min_res == res3:
            N = N // 2
    elif N % 2 == 0:
        res2 = dp[N//2]+1
        min_res = min(res1, res2)
        if min_res == res1:
            N = N-1
        elif min_res == res2:
            N = N // 2
    elif N % 3 == 0:
        res2 = dp[N // 3] + 1
        min_res = min(res1, res2)
        if min_res == res1:
            N = N - 1
        elif min_res == res2:
            N = N // 3
    else:
        min_res = res1
        N = N - 1
