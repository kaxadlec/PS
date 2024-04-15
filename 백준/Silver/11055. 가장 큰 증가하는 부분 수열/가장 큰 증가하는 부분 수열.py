from sys import stdin

N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
dp = [arr[i] for i in range(N)]

for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + arr[i])

print(max(dp))