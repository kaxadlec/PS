from sys import stdin
from collections import deque


def bfs(n):
    global res

    queue = deque()
    queue.append((n, 0))
    while queue:
        num, level = queue.popleft()
        if num == B:
            res = level+1
            break
        if num < B:
            queue.append((2*num, level+1))
            queue.append((10*num+1, level+1))


A, B = map(int, stdin.readline().split())
res = -1
bfs(A)
print(res)