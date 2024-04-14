from sys import stdin

N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
dp = [(0, 0)]*N

for i in range(N):
    for j in range(i):
        if dp[j][1] < arr[j] < arr[i]:
            dp[i] = max(dp[i], (dp[j][0]+1, arr[j]))

print(max(dp)[0] + 1)