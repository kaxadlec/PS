from collections import deque
from sys import stdin

N, K = map(int, stdin.readline().split())
arr = [(i+1) for i in range(N)]
queue = deque(arr)
yose = deque()
while queue:
    for _ in range(K-1):
        n1 = queue.popleft()
        queue.append(n1)
    n2 = queue.popleft()
    yose.append(n2)


result = ', '.join(str(i) for i in yose)

print(f'<{result}>')
