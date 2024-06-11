from sys import stdin
from collections import deque


def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    coordinate = [(r, c)]
    cnt = 1
    visited[r][c] = 1
    while queue:
        x, y = queue.popleft()
        color = board[x][y]
        # print(x, y, color)
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if not (0<=nx<12 and 0<=ny<6):
                continue
            if visited[nx][ny] == 1:
                continue
            if board[nx][ny] == color:
                cnt += 1
                visited[nx][ny] = 1
                queue.append((nx, ny))
                coordinate.append((nx, ny))
    # print('cnt', cnt)
    if cnt >= 4:
        for x, y in coordinate:
            board[x][y] = '.'
        return True
    else:
        return False


board = [list(stdin.readline().rstrip()) for _ in range(12)]

chain = 0
while 1:
    if chain > 0:
        # 중력의 영향을 받아 뿌요들이 아래로 떨어지게 하는 알고리즘
        for j in range(6):
            blank_queue = deque()
            for i in range(11, -1, -1):
                if board[i][j] == '.':
                    blank_queue.append((i, j))
                else:
                    if len(blank_queue) != 0:
                        r, c = blank_queue.popleft()
                        board[i][j], board[r][c] = board[r][c], board[i][j]
                        blank_queue.append((i, j))

    visited = [[0] * 6 for _ in range(12)]
    chain_flag = 0
    # print(chain)
    for i in range(12):
        for j in range(6):
            if board[i][j] == '.':
                continue
            if visited[i][j] == 1:
                continue
            result = bfs(i, j)
            if result:
                chain_flag = 1
            # for b in board:
            #     print(*b)
            # print()
    if chain_flag:
        chain += 1
    else:
        break

print(chain)
