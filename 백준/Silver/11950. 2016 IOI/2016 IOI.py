N, M = map(int, input().split())    # N*M 격자판
board = [list(input()) for _ in range(N)]   # N줄

w_cnt = 0
min_change_cnt = 21e8
for i in range(N-2):
    w_cnt += board[i].count('W')
    b_cnt = 0
    for j in range(i+1, N-1):
        b_cnt += board[j].count('B')
        r_cnt = 0
        for k in range(j+1, N):
            r_cnt += board[k].count('R')

        change_cnt = N*M-(w_cnt+b_cnt+r_cnt)
        if min_change_cnt > change_cnt:
            min_change_cnt = change_cnt

print(min_change_cnt)
