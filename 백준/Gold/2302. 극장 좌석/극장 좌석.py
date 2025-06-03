from sys import stdin

N = int(stdin.readline())
M = int(stdin.readline())
fixed_seat = set(int(stdin.readline()) for _ in range(M))
dp = [0] * (N+1)
dp[0] = 1
dp[1] = 1
if N>=2:
    dp[2] = 2
if N>=3:
    for i in range(3, N+1):
        dp[i] = dp[i-2] + dp[i-1]

ans = 1
streak = 0
for i in range(1, N+2):
    if i in fixed_seat or i == N+1:
        ans *= dp[streak]
        streak = 0
    else:
        streak += 1

print(ans)