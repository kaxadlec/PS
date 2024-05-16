from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
board = [list(stdin.readline().rstrip()) for _ in range(N)]


def bfs(si, sj):
    global cnt
    visited = [[0]*M for _ in range(N)]
    queue = deque()
    queue.append((si, sj))
    visited[si][sj] = 1
    while queue:
        i, j = queue.popleft()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = di + i
            nj = dj + j
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0:
                if board[ni][nj] == 'O':
                    queue.append((ni, nj))
                    visited[ni][nj] = 1
                elif board[ni][nj] == 'P':
                    queue.append((ni, nj))
                    visited[ni][nj] = 1
                    cnt += 1


cnt = 0
for r in range(N):
    for c in range(M):
        if board[r][c] == 'I':
            bfs(r, c)
            break

if cnt == 0:
    print('TT')
else:
    print(cnt)
