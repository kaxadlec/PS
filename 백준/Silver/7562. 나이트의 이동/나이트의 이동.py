from sys import stdin
from collections import deque

T = int(stdin.readline())
for tc in range(T):
    N = int(stdin.readline())
    cur_i, cur_j = map(int, stdin.readline().split())
    goal_i, goal_j = map(int, stdin.readline().split())
    queue = deque()
    queue.append((cur_i, cur_j, 0))
    visited = [[0]*N for _ in range(N)]
    while queue:
        i, j, cnt = queue.popleft()
        if i == goal_i and j == goal_j:
            print(cnt)
            break
        for di, dj in ((1, 2), (-1, 2), (2, 1), (2, -1), (-1, -2), (1, -2), (-2, -1), (-2, 1)):
            ni = i + di
            nj = j + dj
            if 0<=ni<N and 0<=nj<N:
                if visited[ni][nj] == 1:
                    continue
                visited[ni][nj] = 1
                queue.append((ni, nj, cnt+1))
