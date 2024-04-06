from sys import stdin
from collections import deque
'''
1: 익은 토마토
0: 익지 않은 토마토
-1: 토마토가 들어있지 않음
@ 하루 지나면, 상하좌우로 익은 토마토 영향받음
@ 최소 일수 구하기
'''


def bfs(ripe_tomatoes):
    queue = deque()
    for ripe_tomato in ripe_tomatoes:
        queue.append(ripe_tomato)
    while queue:
        i, j, cnt = queue.popleft()
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni = di + i
            nj = dj + j
            if 0 <= ni < N and 0 <= nj < M:
                if visited[ni][nj] == 1:
                    continue
                visited[ni][nj] = 1
                queue.append((ni, nj, cnt+1))
    return cnt


M, N = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
ripe_tomatoes = []
visited = [[0] * M for _ in range(N)]
ripe_cnt = 0
unripe_cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            ripe_cnt += 1
            ripe_tomatoes.append((i, j, 0))
            visited[i][j] = 1
        elif board[i][j] == -1:
            visited[i][j] = 1   # 어차피 못 가는 곳이지만, bfs를 다 돌았을 때, 접근하지 못한 곳 있는지 확인차
        elif board[i][j] == 0:
            unripe_cnt += 1
if ripe_cnt == M*N:
    print(0)
elif unripe_cnt == M*N or len(ripe_tomatoes) == 0:
    print(-1)
else:
    days = bfs(ripe_tomatoes)
    false_check = 0
    for row_visited in visited:
        if set(row_visited) != {1}:
            false_check = 1
            print(-1)
            break
    if false_check == 0:
        print(days)
