from sys import stdin

N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
x = int(stdin.readline())
check = [0]*2000001
cnt = 0
for i in range(N):
    if check[x-arr[i]] == 1:
        cnt += 1
    check[arr[i]] = 1

print(cnt)
