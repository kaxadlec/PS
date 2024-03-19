def dfs(i, j):
    global house
    for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        ni = i + di
        nj = j + dj
        if 0<=ni<N and 0<=nj<N:
            if board[ni][nj] == 1 and visited[ni][nj] ==0:
                visited[ni][nj] = 1
                house += 1
                dfs(ni, nj)


N = int(input())
board = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
cnt = 0
houses = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and visited[i][j] == 0:
            house = 1
            visited[i][j] = 1
            dfs(i, j)
            houses.append(house)
            cnt += 1

print(cnt)
houses.sort()
for k in range(cnt):
    print(houses[k])