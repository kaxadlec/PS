from sys import stdin
from collections import deque

M, N, H = map(int, stdin.readline().split())
board = [[list(map(int, stdin.readline().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0]*M for _ in range(N)] for _ in range(H)]
already_riped_flag = 1
cant_riped_flag = 0
day = 0
queue = deque()
for h in range(H):
    for i in range(N):
        for j in range(M):
            if board[h][i][j] == 1:
                queue.append((h, i, j, day))

while queue:
    h, i, j, day = queue.popleft()
    # print(board)
    # print(h, i, j, day)
    for dh, di, dj in ((0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0)):
        nh, ni, nj = dh + h, di + i, dj + j
        if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M:
            if board[nh][ni][nj] == 0:
                board[nh][ni][nj] = day + 2
                queue.append((nh, ni, nj, day+1))
for h in range(H):
    for i in range(N):
        for j in range(M):
            if board[h][i][j] == 0:
                cant_riped_flag = 1
                break
        if cant_riped_flag == 1:
            break
    if cant_riped_flag == 1:
        break

if cant_riped_flag == 1:
    print(-1)
else:
    print(day)
