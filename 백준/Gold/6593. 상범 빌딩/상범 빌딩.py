from sys import stdin
from collections import deque


def bfs(i, j, k, visited):
    queue = deque()
    queue.append((i, j, k, 0))

    while queue:
        x, y, z, minute = queue.popleft()
        for dx, dy, dz in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
            nx, ny, nz = x + dx, y + dy, z + dz
            if not (0<=nx<R and 0<=ny<C and 0<=nz<L):
                continue
            if visited[nz][nx][ny] == 1:
                continue
            if building[nz][nx][ny] == 'E':
                return minute+1
            elif building[nz][nx][ny] == '#':
                continue
            elif building[nz][nx][ny] == '.':
                visited[nz][nx][ny] = 1
                queue.append((nx, ny, nz, minute+1))


while 1:
    L, R, C = map(int, stdin.readline().split())

    if L == 0 and R == 0 and C == 0:
        break

    building = []
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]
    for _ in range(L):
        floor = [list(stdin.readline().rstrip()) for _ in range(R)]
        blank = stdin.readline().rstrip()
        building.append(floor)

    for k in range(L):
        for i in range(R):
            for j in range(C):
                if building[k][i][j] == 'S':
                    result = bfs(i, j, k, visited)

    if result is None:
        print('Trapped!')
    else:
        print(f'Escaped in {result} minute(s).')

