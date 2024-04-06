from sys import stdin
from collections import deque

N = int(stdin.readline().strip())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
blue_cnt = 0
white_cnt = 0


def backtrack(N, st_pos, end_pos):
    global blue_cnt, white_cnt

    si, sj = st_pos
    ei, ej = end_pos
    st_value = board[si][sj]
    queue = deque()
    visitied = [[0]*N for _ in range(N)]
    false_check = 0
    queue.append((si, sj))
    while queue:
        i, j = queue.popleft()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if si <= ni <= ei and sj <= nj <= ej:
                if visitied[ni-si][nj-sj] == 1:
                    continue
                if board[ni][nj] != st_value:
                    false_check = 1
                    break
                visitied[ni-si][nj-sj] = 1
                queue.append((ni, nj))

        if false_check == 1:
            break
    if false_check == 0:
        if st_value == 1:
            blue_cnt += 1
        else:
            white_cnt += 1

        return

    backtrack(N//2, (si, sj), (si+N//2-1, sj+N//2-1))
    backtrack(N//2, (si, sj+N//2), (si+N//2-1, sj+N-1))
    backtrack(N//2, (si+N//2, sj), (si+N-1, sj+N//2-1))
    backtrack(N//2, (si+N//2, sj+N//2), (si+N-1, sj+N-1))


start_pos = (0, 0)
end_pos = (N-1, N-1)
backtrack(N, start_pos, end_pos)

print(white_cnt)
print(blue_cnt)
