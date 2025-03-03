# 코드를 작성해주세요
from sys import stdin

r, c, T = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(r)]
for t in range(T):
    new_board = [row[:] for row in board]
    up_cleaner_i, up_cleaner_j = None, None
    cleaner_flag = 0
    # 미세먼지 확산
    for i in range(r):
        for j in range(c):
            if cleaner_flag == 0 and j == 0 and board[i][j] == -1:
                up_cleaner_i, up_cleaner_j = i, j
                cleaner_flag = 1
            if board[i][j] != -1 and board[i][j] != 0:
                spread_cnt = 0
                spread_amount = board[i][j] // 5
                for di, dj in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                    ni = di + i
                    nj = dj + j
                    if not (0 <= ni < r and 0 <= nj < c):
                        continue
                    if board[ni][nj] == -1:
                        continue
                    new_board[ni][nj] += spread_amount
                    spread_cnt += 1
                new_board[i][j] = new_board[i][j] - (spread_amount * spread_cnt)

    # 공기청정기 작동
    new_new_board = [row[:] for row in new_board]
    # 위쪽 공기청정기 순환
    #1
    new_new_board[up_cleaner_i][1] = 0
    new_new_board[up_cleaner_i][2:c] = new_board[up_cleaner_i][1:c-1]
    #2
    for i in range(up_cleaner_i):
        new_new_board[i][c-1] = new_board[i+1][c-1]
    #3
    for j in range(c-1):
        new_new_board[0][j] = new_board[0][j+1]
    #4
    for i in range(1, up_cleaner_i):
        new_new_board[i][0] = new_board[i-1][0]
    
    # 아래쪽 공기청정기 순환
    down_cleaner_i, down_cleaner_j = up_cleaner_i+1, up_cleaner_j
    new_new_board[down_cleaner_i][1] = 0
    for j in range(2, c):
        new_new_board[down_cleaner_i][j] = new_board[down_cleaner_i][j-1]
    for i in range(down_cleaner_i+1, r):
        new_new_board[i][c-1] = new_board[i-1][c-1]
    for j in range(c-1):
        new_new_board[r-1][j] = new_board[r-1][j+1]
    for i in range(down_cleaner_i+1, r-1):
        new_new_board[i][0] = new_board[i+1][0]
        
    board = [row[:] for row in new_new_board]
        
# for row in new_board:
    # print(*row)
# print("-----------------")
# for row in new_new_board:
    # print(*row)                
result = sum(sum(row) for row in board)     
print(result+2)