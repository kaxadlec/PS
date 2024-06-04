from sys import stdin

N, M, i, j, K = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
commands = list(map(int, stdin.readline().split()))
dice = [[0]*3 for _ in range(4)]

for turn in range(K):
    if commands[turn] == 1:     # 동
        ni, nj = i, j + 1
        if not (0<=ni<N and 0<=nj<M):
            continue
        left, top, right, bottom = dice[1][0], dice[1][1], dice[1][2], dice[3][1]
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = top, right, bottom, left
    elif commands[turn] == 2:   # 서
        ni, nj = i, j - 1
        if not (0<=ni<N and 0<=nj<M):
            continue
        left, top, right, bottom = dice[1][0], dice[1][1], dice[1][2], dice[3][1]
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = bottom, left, top, right
    elif commands[turn] == 3:   # 북
        ni, nj = i - 1, j
        if not (0<=ni<N and 0<=nj<M):
            continue
        back, top, front, bottom = dice[0][1], dice[1][1], dice[2][1], dice[3][1]
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = top, front, bottom, back
    else:   # 남
        ni, nj = i + 1, j
        if not (0<=ni<N and 0<=nj<M):
            continue
        back, top, front, bottom = dice[0][1], dice[1][1], dice[2][1], dice[3][1]
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = bottom, back, top, front

    i, j = ni, nj

    if board[i][j] == 0:  # 주사위가 위치한 칸의 숫자가 0
        # 주사위의 바닥면에 쓰여 있는 숫자가 칸에 복사됨
        board[i][j] = dice[3][1]
    else:  # 주사위가 위치한 칸의 숫자가 0이 아니면
        # 주사위 바닥면으로 칸에 쓰여있는 숫자가 복사
        dice[3][1] = board[i][j]
        # 그리고 칸에 쓰여 있는 숫자는 0이 됨
        board[i][j] = 0

    print(dice[1][1])
