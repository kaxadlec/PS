from sys import stdin

N, S = map(int, stdin.readline().split())
arr = [0] + list(map(int, stdin.readline().split()))

arr_sum = 0
min_dis = float('INF')
j = 0
for i in range(N+1):
    arr_sum += arr[i]

    while i-j >= 0 and arr_sum-arr[j] >= S:
        arr_sum -= arr[j]
        min_dis = min(min_dis, i - j)
        j += 1

if min_dis == float('inf'):
    print(0)
else:
    print(min_dis)