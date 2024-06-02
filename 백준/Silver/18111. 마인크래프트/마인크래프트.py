from sys import stdin

N, M, B = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
# board_max = max(max(i) for i in board)
board_ref = 256
res_time, res_height = float('inf'), -1

while board_ref >= 0:
    # print(board_ref)
    inventory_block = B
    time, height = 0, board_ref

    for i in range(N):
        for j in range(M):
            if board[i][j] > board_ref:
                diff = board[i][j] - board_ref
                inventory_block += diff
                time += diff*2
            elif board[i][j] < board_ref:
                diff = board_ref - board[i][j]
                inventory_block -= diff
                time += diff

    board_ref = board_ref - 1
    if inventory_block < 0:
        # print('블록소진')
        continue
    # print(time, height)
    if time < res_time:
        res_time = time
        res_height = height

    elif time == res_time:
        if res_height < height:
            res_height = height


print(res_time, res_height)
