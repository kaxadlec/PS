from sys import stdin

N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
cnt = 0
en = 0
check = {}

for st in range(N):
    while en < N and arr[en] not in check:
        check[arr[en]] = True
        en += 1
    cnt += (en-st)
    del check[arr[st]]

print(cnt)