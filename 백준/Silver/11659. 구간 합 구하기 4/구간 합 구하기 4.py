from sys import stdin

N, M = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))
memo = [0]*(N+1)
for k in range(1, N+1):
    memo[k] = memo[k-1] + nums[k-1]

for _ in range(M):
    i, j = map(int, stdin.readline().split())
    print(memo[j]-memo[i-1])
