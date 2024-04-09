from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
dp = [-1001]*n
dp[0] = arr[0]
for i in range(1, n):
    dp[i] = max(arr[i], dp[i-1] + arr[i])

print(max(dp))
