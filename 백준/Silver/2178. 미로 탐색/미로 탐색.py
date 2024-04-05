from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().strip())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
result = 0

si, sj = 0, 0
goal = (N-1, M-1)
queue = deque()
queue.append((si, sj, 0))
while queue:
    i, j, cnt = queue.popleft()
    if (i, j) == goal:
        result = cnt+1
        break
    for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ni = di + i
        nj = dj + j
        if 0<=ni<N and 0<=nj<M and board[ni][nj] == 1:
            if visited[ni][nj] == 1:
                continue
            visited[ni][nj] = 1
            queue.append((ni, nj, cnt+1))

print(result)

