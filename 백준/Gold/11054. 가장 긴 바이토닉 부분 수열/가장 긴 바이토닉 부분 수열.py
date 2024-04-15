from sys import stdin

N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
dp1 = [0]*N
dp2 = [0]*N

for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp1[i] = max(dp1[i], dp1[j]+1)

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if arr[i] > arr[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)

dp_sum = [0]*N
for i in range(N):
    dp_sum[i] = dp1[i]+dp2[i]

print(max(dp_sum)+1)