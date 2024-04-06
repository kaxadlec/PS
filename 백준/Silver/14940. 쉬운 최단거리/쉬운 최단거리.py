from sys import stdin
from collections import deque
'''
0: 갈 수 없는 땅
1: 갈 수 있는 땅
2: 목표 지점
'''
n, m = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
queue = deque()
visited = [[0]*m for _ in range(n)]
check_board = [[-1]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            queue.append((i, j, 0))
            visited[i][j] = 1
        elif board[i][j] == 0:
            check_board[i][j] = 0

while queue:
    i, j, cnt = queue.popleft()
    check_board[i][j] = cnt
    for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ni = di + i
        nj = dj + j
        if 0 <= ni < n and 0 <= nj < m:
            if visited[ni][nj] == 1:
                continue
            if board[ni][nj] == 0:  # 갈 수 없는 땅
                continue
            elif board[ni][nj] == 1:  # 갈 수 있는 땅
                visited[ni][nj] = 1
                queue.append((ni, nj, cnt+1))

for row in check_board:
    print(*row)
