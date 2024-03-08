from collections import deque
T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    board = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        X, Y = map(int, input().split())
        board[Y][X] = 1
    for r in range(N):
        for c in range(M):
            if visited[r][c] == 0 and board[r][c] == 1:
                queue = deque()
                queue.append((r, c))
                while queue:
                    i, j = queue.popleft()
                    for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                        ni = i + di
                        nj = j + dj
                        if 0<=ni<N and 0<=nj<M and board[ni][nj] == 1 and visited[ni][nj] == 0:
                            visited[ni][nj] = 1
                            queue.append((ni, nj))
                cnt += 1

    print(cnt)