from sys import stdin

N, M = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]


def up_monitor(i, j):
    idx_path = []
    for n in range(1, N + 1):  # 위쪽
        ni = -1 * n + i
        nj = j
        if not (0 <= ni < N):
            break
        if board[ni][nj] == 6:
            break
        if board[ni][nj] == 0:
            idx_path.append((ni, nj))
            board[ni][nj] = '#'
    return idx_path


def down_monitor(i, j):
    idx_path = []
    for n in range(1, N + 1):  # 아래쪽
        ni = 1 * n + i
        nj = j
        if not (0 <= ni < N):
            break
        if board[ni][nj] == 6:
            break
        if board[ni][nj] == 0:
            idx_path.append((ni, nj))
            board[ni][nj] = '#'
    return idx_path


def right_monitor(i, j):
    idx_path = []
    for m in range(1, M + 1):  # 오른쪽
        ni = i
        nj = 1 * m + j
        if not (0 <= nj < M):
            break
        if board[ni][nj] == 6:
            break
        if board[ni][nj] == 0:
            idx_path.append((ni, nj))
            board[ni][nj] = '#'
    return idx_path


def left_monitor(i, j):
    idx_path = []
    for m in range(1, M + 1):  # 왼쪽
        ni = i
        nj = -1 * m + j
        if not (0 <= nj < M):
            break
        if board[ni][nj] == 6:
            break
        if board[ni][nj] == 0:
            idx_path.append((ni, nj))
            board[ni][nj] = '#'
    return idx_path


cctv_cnt = 0
cctv_list = []
for i in range(N):
    for j in range(M):
        if 1 <= board[i][j] <= 5:
            cctv_cnt += 1
            cctv_list.append((i, j, board[i][j]))

min_result = 21e8


def backtrack(idx):
    global min_result

    if idx == cctv_cnt:     # 기저 조건
        result = 0
        for row in board:
            result += row.count(0)
        min_result = min(min_result, result)
        return

    # cctv 좌표
    x, y = cctv_list[idx][0], cctv_list[idx][1]
    if cctv_list[idx][2] == 1:  # 1번 cctv
        up_path = up_monitor(x, y)
        backtrack(idx+1)
        for up in up_path:
            r, c = up
            board[r][c] = 0

        right_path = right_monitor(x, y)
        backtrack(idx+1)
        for right in right_path:
            r, c = right
            board[r][c] = 0

        down_path = down_monitor(x, y)
        backtrack(idx+1)
        for down in down_path:
            r, c = down
            board[r][c] = 0

        left_path = left_monitor(x, y)
        backtrack(idx+1)
        for left in left_path:
            r, c = left
            board[r][c] = 0

    elif cctv_list[idx][2] == 2:  # 2번 cctv
        up_path = up_monitor(x, y)
        down_path = down_monitor(x, y)
        backtrack(idx + 1)
        for up in up_path:
            r, c = up
            board[r][c] = 0
        for down in down_path:
            r, c = down
            board[r][c] = 0

        right_path = right_monitor(x, y)
        left_path = left_monitor(x, y)
        backtrack(idx + 1)
        for right in right_path:
            r, c = right
            board[r][c] = 0
        for left in left_path:
            r, c = left
            board[r][c] = 0

    elif cctv_list[idx][2] == 3:  # 3번 cctv
        up_path = up_monitor(x, y)
        right_path = right_monitor(x, y)
        backtrack(idx+1)
        for up in up_path:
            r, c = up
            board[r][c] = 0
        for right in right_path:
            r, c = right
            board[r][c] = 0

        right_path = right_monitor(x, y)
        down_path = down_monitor(x, y)
        backtrack(idx + 1)
        for right in right_path:
            r, c = right
            board[r][c] = 0
        for down in down_path:
            r, c = down
            board[r][c] = 0

        down_path = down_monitor(x, y)
        left_path = left_monitor(x, y)
        backtrack(idx+1)
        for down in down_path:
            r, c = down
            board[r][c] = 0
        for left in left_path:
            r, c = left
            board[r][c] = 0

        left_path = left_monitor(x, y)
        up_path = up_monitor(x, y)
        backtrack(idx + 1)
        for left in left_path:
            r, c = left
            board[r][c] = 0
        for up in up_path:
            r, c = up
            board[r][c] = 0

    elif cctv_list[idx][2] == 4:  # 4번 cctv
        up_path = up_monitor(x, y)
        right_path = right_monitor(x, y)
        down_path = down_monitor(x, y)
        backtrack(idx + 1)
        for up in up_path:
            r, c = up
            board[r][c] = 0
        for right in right_path:
            r, c = right
            board[r][c] = 0
        for down in down_path:
            r, c = down
            board[r][c] = 0

        right_path = right_monitor(x, y)
        down_path = down_monitor(x, y)
        left_path = left_monitor(x, y)
        backtrack(idx + 1)
        for right in right_path:
            r, c = right
            board[r][c] = 0
        for down in down_path:
            r, c = down
            board[r][c] = 0
        for left in left_path:
            r, c = left
            board[r][c] = 0

        down_path = down_monitor(x, y)
        left_path = left_monitor(x, y)
        up_path = up_monitor(x, y)
        backtrack(idx + 1)
        for down in down_path:
            r, c = down
            board[r][c] = 0
        for left in left_path:
            r, c = left
            board[r][c] = 0
        for up in up_path:
            r, c = up
            board[r][c] = 0

        left_path = left_monitor(x, y)
        up_path = up_monitor(x, y)
        right_path = right_monitor(x, y)
        backtrack(idx + 1)
        for left in left_path:
            r, c = left
            board[r][c] = 0
        for up in up_path:
            r, c = up
            board[r][c] = 0
        for right in right_path:
            r, c = right
            board[r][c] = 0

    else:  # 5번 cctv
        up_path = up_monitor(x, y)
        right_path = right_monitor(x, y)
        down_path = down_monitor(x, y)
        left_path = left_monitor(x, y)
        backtrack(idx+1)


backtrack(0)

print(min_result)



