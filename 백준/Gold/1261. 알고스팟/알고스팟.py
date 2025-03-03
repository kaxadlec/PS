from sys import stdin
from collections import deque

M, N = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().rstrip())) for _ in range(N)]
INF = float('inf')
distance = [[INF]*M for _ in range(N)]
distance[0][0] = 0
dq = deque()
dq.append((0, 0, 0))
min_cnt = INF
while dq:
    i, j, cnt = dq.popleft()
    if i == N-1 and j == M-1:
        min_cnt = min(min_cnt, cnt)
    
    for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ni, nj = i + di, j + dj
        if not (0 <= ni < N and 0 <= nj < M):
            continue
        if distance[i][j] + board[ni][nj] < distance[ni][nj]:
            distance[ni][nj] = distance[i][j] + board[ni][nj]
            
            if board[ni][nj] == 0:
                dq.appendleft((ni, nj, cnt))
            else:
                dq.append((ni, nj, cnt+1))

print(min_cnt)