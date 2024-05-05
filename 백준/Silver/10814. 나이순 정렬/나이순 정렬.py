from sys import stdin

N = int(stdin.readline())
arr = [tuple(stdin.readline().split()) for _ in range(N)]
arr.sort(key=lambda x: int(x[0]))
for i in range(N):
    age, name = arr[i]
    print(age, name)