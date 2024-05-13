from sys import stdin

N, M = map(int, stdin.readline().split())
board = [list(stdin.readline().rstrip()) for _ in range(N)]
min_cnt = 21e8

if board[0][0] == 'W':
    for i in range(N - 7):
        for j in range(M - 7):
            cnt1 = 0
            cnt2 = 0
            for r in range(i, i + 8):
                for c in range(j, j + 8):
                    if (r + c) % 2 == 0:
                        if board[r][c] == 'B':
                            cnt1 += 1
                        elif board[r][c] == 'W':
                            cnt2 += 1
                    else:
                        if board[r][c] == 'B':
                            cnt2 += 1
                        elif board[r][c] == 'W':
                            cnt1 += 1
            cnt = min(cnt1, cnt2)
            if cnt < min_cnt:
                min_cnt = cnt


elif board[0][0] == 'B':
    for i in range(N-7):
        for j in range(M-7):
            cnt1 = 0
            cnt2 = 0
            for r in range(i, i+8):
                for c in range(j, j+8):
                    if (r+c) % 2 == 0:
                        if board[r][c] == 'B':
                            cnt2 += 1
                        elif board[r][c] == 'W':
                            cnt1 += 1
                    else:
                        if board[r][c] == 'B':
                            cnt1 += 1
                        elif board[r][c] == 'W':
                            cnt2 += 1
            cnt = min(cnt1, cnt2)
            if cnt < min_cnt:
                min_cnt = cnt

print(min_cnt)
