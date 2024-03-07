from collections import deque
import sys

input = sys.stdin.readline
K = int(input())
stack = deque()
for i in range(K):
    n = int(input())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)
result = sum(stack)
print(result)
