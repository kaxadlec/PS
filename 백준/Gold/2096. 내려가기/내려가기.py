from sys import stdin

N = int(stdin.readline())
max_dp = [0]*3
min_dp = [0]*3

for i in range(N):
    arr = list(map(int, stdin.readline().split()))
    if i == 0:
        for j in range(3):
            max_dp[j] = arr[j]
            min_dp[j] = arr[j]
    else:
        max_j_0_1 = max(max_dp[0], max_dp[1])
        max_j_0_1_2 = max(max_dp[0], max_dp[1], max_dp[2])
        max_j_1_2 = max(max_dp[1], max_dp[2])
        min_j_0_1 = min(min_dp[0], min_dp[1])
        min_j_0_1_2 = min(min_dp[0], min_dp[1], min_dp[2])
        min_j_1_2 = min(min_dp[1], min_dp[2])

        max_dp[0] = arr[0] + max_j_0_1
        max_dp[1] = arr[1] + max_j_0_1_2
        max_dp[2] = arr[2] + max_j_1_2
        min_dp[0] = arr[0] + min_j_0_1
        min_dp[1] = arr[1] + min_j_0_1_2
        min_dp[2] = arr[2] + min_j_1_2

print(max(max_dp), min(min_dp))