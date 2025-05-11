from sys import stdin
from collections import deque

n, l, r = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]

locked = [[False] * n for _ in range(n)]
day = 0
# 하루 day가 증가하는 while문
while 1:
    keep_flag = False
    visited = [[False] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if not visited[x][y] and not locked[x][y]:
                # print("x y", x, y)
                queue = deque()
                queue.append((x, y))
                path = set()
                path.add((x, y))
                visited[x][y] = True
                num_sum = board[x][y]
                num_cnt = 1
                while queue:
                    i, j = queue.popleft()
                    locked[i][j] = True
                    for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                        ni, nj = di + i, dj + j
                        if not (0 <= ni < n and 0 <= nj < n):
                            continue
                        if visited[ni][nj]:
                            continue
                        if l <= abs(board[ni][nj] - board[i][j]) <= r:
                            queue.append((ni, nj))
                            path.add((ni, nj))
                            visited[ni][nj] = True
                            num_sum += board[ni][nj]
                            num_cnt += 1
                            # print("ni nj num_sum num_cnt", ni, nj, num_sum, num_cnt)


                # print("num_sum", num_sum, "num_cnt", num_cnt)
                if num_cnt > 1:
                    if not keep_flag:
                        keep_flag = True
                    avg_num = num_sum // num_cnt
                    for pi, pj in path:
                        board[pi][pj] = avg_num
                        locked[pi][pj] = False
                # print(board)
                # print("-----------------------------")
    if not keep_flag:
        break
    day += 1

    # print(locked)
    # print("day", day)
    # print()

print(day)
