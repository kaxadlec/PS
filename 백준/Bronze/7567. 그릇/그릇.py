from sys import stdin
from collections import deque

bowl = stdin.readline().rstrip()
stack = deque()
res = 0
for i in range(len(bowl)):
    if i == 0:
        stack.append(bowl[i])
        res += 10
    else:
        top = stack.pop()
        if top == bowl[i]:
            res += 5
        else:
            res += 10
        stack.append(bowl[i])

print(res)