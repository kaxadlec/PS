from sys import stdin
from collections import deque

N = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
max_block = 0


def move_up(updated_board):
    for j in range(N):
        stack = deque()
        queue = deque()
        for i in range(N-1, -1, -1):
            if updated_board[i][j] != 0:
                stack.append((updated_board[i][j]))

        while stack:
            if len(stack) == 1:
                queue.append(stack.pop())
                break
            num1, num2 = stack.pop(), stack.pop()
            if num1 == num2:
                queue.append((num1+num2))
            else:
                queue.append(num1)
                stack.append(num2)

        r, c = 0, j
        while queue:
            updated_board[r][c] = queue.popleft()
            r += 1
        if 0<=r<N:
            for x in range(r, N):
                updated_board[x][c] = 0
    return updated_board


def move_down(updated_board):
    for j in range(N):
        stack = deque()
        queue = deque()
        for i in range(N):
            if updated_board[i][j] != 0:
                stack.append((updated_board[i][j]))

        while stack:
            if len(stack) == 1:
                queue.append(stack.pop())
                break
            num1, num2 = stack.pop(), stack.pop()
            if num1 == num2:
                queue.append((num1 + num2))
            else:
                queue.append(num1)
                stack.append(num2)

        r, c = N-1, j
        while queue:
            updated_board[r][c] = queue.popleft()
            r -= 1
        if 0 <= r < N:
            for x in range(r+1):
                updated_board[x][c] = 0
    return updated_board


def move_right(updated_board):
    for i in range(N):
        stack = deque()
        queue = deque()
        for j in range(N):
            if updated_board[i][j] != 0:
                stack.append((updated_board[i][j]))

        while stack:
            if len(stack) == 1:
                queue.append(stack.pop())
                break
            num1, num2 = stack.pop(), stack.pop()
            if num1 == num2:
                queue.append((num1 + num2))
            else:
                queue.append(num1)
                stack.append(num2)

        r, c = i, j
        while queue:
            updated_board[r][c] = queue.popleft()
            c -= 1
        if 0 <= c < N:
            for y in range(c + 1):
                updated_board[r][y] = 0
    return updated_board


def move_left(updated_board):
    for i in range(N):
        stack = deque()
        queue = deque()
        for j in range(N-1, -1, -1):
            if updated_board[i][j] != 0:
                stack.append((updated_board[i][j]))

        while stack:
            if len(stack) == 1:
                queue.append(stack.pop())
                break
            num1, num2 = stack.pop(), stack.pop()
            if num1 == num2:
                queue.append((num1 + num2))
            else:
                queue.append(num1)
                stack.append(num2)

        r, c = i, 0
        while queue:
            updated_board[r][c] = queue.popleft()
            c += 1
        if 0 <= c < N:
            for y in range(c, N):
                updated_board[r][y] = 0
    return updated_board


def check_max_block(board):
    level_max_block = 0
    for row in board:
        level_max_block = max(level_max_block, max(row))
    return level_max_block


def backtrack(level, board):
    global max_block

    if level == 5:
        max_block = max(max_block, check_max_block(board))
        return

    board_up = [row[:] for row in board]
    board_down = [row[:] for row in board]
    board_right = [row[:] for row in board]
    board_left = [row[:] for row in board]
    backtrack(level+1, move_up(board_up))
    backtrack(level+1, move_down(board_down))
    backtrack(level+1, move_right(board_right))
    backtrack(level+1, move_left(board_left))


backtrack(0, board)
print(max_block)