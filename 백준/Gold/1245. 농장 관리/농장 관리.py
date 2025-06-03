from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
checked = [[False] * M for _ in range(N)]
ans = 0

def bfs(si, sj):
    queue = deque()
    queue.append((si, sj))
    visited = [[False] * M for _ in range(N)]
    visited[si][sj] = True
    while queue:
        i, j = queue.popleft()
        checked[i][j] = True
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)):
            ni, nj = i + di, j + dj
            if not ((0 <= ni < N) and (0 <= nj < M)):
                continue
            if visited[ni][nj]:
                continue
            if board[ni][nj] > board[i][j]:
                return False
            elif board[ni][nj] == board[i][j]:
                queue.append((ni, nj))
                visited[ni][nj]= True

    return True


for x in range(N):
    for y in range(M):
        if checked[x][y]:
            continue
        result = bfs(x, y)
        if result:
            ans += 1
    
print(ans)