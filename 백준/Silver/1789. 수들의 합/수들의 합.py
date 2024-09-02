from sys import stdin

S = int(stdin.readline())
res = 0
i = 1
while 1:
    res += i
    if res > S:
        print(i-1)
        break
    i = i + 1

