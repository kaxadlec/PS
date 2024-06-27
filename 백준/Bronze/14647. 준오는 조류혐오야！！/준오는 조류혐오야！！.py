from sys import stdin

N, M = map(int, stdin.readline().split())
board = [list(stdin.readline().split()) for _ in range(N)]
transposed_board = list(map(list, zip(*board)))

all_cnt = 0
max_cnt = 0
for i in range(N):
    row_cnt = 0
    for num in board[i]:
        row_cnt += num.count('9')

    all_cnt += row_cnt
    max_cnt = max(max_cnt, row_cnt)

for j in range(M):
    col_cnt = 0
    for num in transposed_board[j]:
        col_cnt += num.count('9')

    all_cnt += col_cnt
    max_cnt = max(max_cnt, col_cnt)

print((all_cnt - 2*max_cnt) // 2)

