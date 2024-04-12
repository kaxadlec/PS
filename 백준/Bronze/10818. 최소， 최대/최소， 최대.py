from sys import stdin

N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
print(min(arr), max(arr))