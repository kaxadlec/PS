from collections import deque
import sys

def normal():
    global normal_cnt
    visited = [[0] * N for _ in range(N)]
    queue_visited = [[0] * N for _ in range(N)]
    stack = deque()
    queue = deque()
    queue.append((0, 0))
    while queue:
        qi, qj = queue.popleft()
        if visited[qi][qj] == 1:
            continue

        stack.append((qi, qj))
        visited[qi][qj] = 1
        current_color = board[qi][qj]
        normal_cnt += 1
        while stack:
            si, sj = stack.pop()
            for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                ni = si + di
                nj = sj + dj
                if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                    if current_color == board[ni][nj]:
                        visited[ni][nj] = 1
                        stack.append((ni, nj))
                    else:
                        if queue_visited[ni][nj] == 0:
                            queue.append((ni, nj))
                            queue_visited[ni][nj] = 1


def red_green():
    global red_green_cnt
    visited = [[0] * N for _ in range(N)]
    queue_visited = [[0] * N for _ in range(N)]
    stack = deque()
    queue = deque()
    queue.append((0, 0))
    while queue:
        qi, qj = queue.popleft()
        if visited[qi][qj] == 1:
            continue
        stack.append((qi, qj))
        visited[qi][qj] = 1
        current_color = board[qi][qj]
        red_green_cnt += 1
        while stack:
            si, sj = stack.pop()
            for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                ni = si + di
                nj = sj + dj
                if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                    if current_color == 'R' or current_color == 'G':
                        if board[ni][nj] == 'R' or board[ni][nj] == 'G':
                            visited[ni][nj] = 1
                            stack.append((ni, nj))
                        else:
                            if queue_visited[ni][nj] == 0:
                                queue.append((ni, nj))
                                queue_visited[ni][nj] = 1

                    elif current_color == 'B':
                        if board[ni][nj] == 'B':
                            visited[ni][nj] = 1
                            stack.append((ni, nj))
                        else:
                            if queue_visited[ni][nj] == 0:
                                queue.append((ni, nj))
                                queue_visited[ni][nj] = 1


input = sys.stdin.readline
N = int(input())
board = [list(input()) for _ in range(N)]
normal_cnt = 0
normal()
red_green_cnt = 0
red_green()
print(normal_cnt, red_green_cnt)

