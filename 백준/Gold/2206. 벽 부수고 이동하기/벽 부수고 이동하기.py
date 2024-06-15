from sys import stdin
from collections import deque


N, M = map(int, stdin.readline().split())
unbroken_board = [list(map(int, stdin.readline().rstrip())) for _ in range(N)]
INF = float('inf')
min_dis = INF


def move(board):
    global min_dis

    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
    queue = deque()
    queue.append((0, 0, 1, 0))
    visited[0][0][0] = 1
    visited[0][0][1] = 1
    while queue:
        r, c, dis, is_breaking = queue.popleft()
 
        if r == N-1 and c == M-1:
            min_dis = min(min_dis, dis)

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = dr + r, dc + c
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if is_breaking and board[nr][nc] == 0:
                if visited[nr][nc][1]:
                    continue
                queue.append((nr, nc, dis+1, 1))
                visited[nr][nc][1] = 1
            if not is_breaking:
                if board[nr][nc] == 1:
                    queue.append((nr, nc, dis+1, 1))
                    visited[nr][nc][1] = 1
                else:
                    if visited[nr][nc][0]:
                        continue
                    queue.append((nr, nc, dis+1, 0))
                    visited[nr][nc][0] = 1


move(unbroken_board)
if min_dis == INF:
    print(-1)
else:
    print(min_dis)
