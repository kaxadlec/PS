from sys import stdin
from collections import deque

N = int(stdin.readline())
apple_board = [[0]*N for _ in range(N)]
K = int(stdin.readline())
for _ in range(K):
    a, b = map(int, stdin.readline().split())
    apple_board[a-1][b-1] = 1

L = int(stdin.readline())
turn_info = deque()
for _ in range(L):
    x, c = stdin.readline().split()
    turn_info.append((int(x), c))
di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

snake_board = [[0]*N for _ in range(N)]
sec = 0
i, j = 0, 0
d_idx = 0
snake_board[0][0] = 1
queue = deque()
queue.append((i, j, sec, d_idx))
snake_queue = deque()
snake_queue.append((i, j))
while queue:
    i, j, sec, d_idx = queue.popleft()

    if turn_info:
        if sec == turn_info[0][0]:
            if turn_info[0][1] == 'L':
                d_idx = (d_idx+3) % 4
            elif turn_info[0][1] == 'D':
                d_idx = (d_idx+1) % 4
            turn_info.popleft()

    ni, nj = i + di[d_idx], j + dj[d_idx]

    # 게임 종료 조건 2가지
    if not (0<=ni<N and 0<=nj<N):
        break
    if snake_board[ni][nj] == 1:
        break
        
    if apple_board[ni][nj] != 1:
        tail_i, tail_j = snake_queue.popleft()
        snake_board[tail_i][tail_j] = 0
    elif apple_board[ni][nj] == 1:
        apple_board[ni][nj] = 0
    snake_board[ni][nj] = 1
    snake_queue.append((ni, nj))

    queue.append((ni, nj, sec+1, d_idx))


print(sec+1)
