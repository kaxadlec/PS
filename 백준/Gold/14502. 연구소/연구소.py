from sys import stdin
from itertools import combinations
from collections import deque

N, M = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
blank_arr = []
virus_arr = []

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            blank_arr.append((i, j))
        elif board[i][j] == 2:
            virus_arr.append((i, j))


def spreading_virus(spread_board):
    visited = [[0]*M for _ in range(N)]
    virus_queue = deque(virus_arr)
    while virus_queue:
        r, c = virus_queue.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = dr + r, dc + c
            if not (0<=nr<N and 0<=nc<M):
                continue
            if visited[nr][nc]:
                continue
            if spread_board[nr][nc] == 0:
                spread_board[nr][nc] = 2
                visited[nr][nc] = 1
                virus_queue.append((nr, nc))


max_cnt = 0
for combo in combinations(blank_arr, 3):
    new_board = [row[:] for row in board]
    for com in combo:
        x, y = com
        new_board[x][y] = 1
    spreading_virus(new_board)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if new_board[i][j] == 0:
                cnt += 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)
