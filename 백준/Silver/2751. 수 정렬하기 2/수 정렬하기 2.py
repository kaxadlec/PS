from sys import stdin

N = int(stdin.readline())
arr = []
for i in range(N):
    num = int(stdin.readline())
    arr.append(num)
arr.sort()
for i in range(N):
    print(arr[i])
