from sys import stdin

def idx_transform(x, N):
    if x < 0:
        temp = -1 * x
        temp = temp % N
        temp = -1 * temp
        if temp == 0:
            x = 0
        else:
            x = N + temp
    else:
        x = x % N
    return x
    
    
N, M = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
dir = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
initial_clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
clouds = set(initial_clouds)
for _ in range(M):
    d, s = map(int, stdin.readline().split())
    di, dj = dir[d - 1]
    moved_clouds = set()
    #1 구름 d 방향으로 s칸 이동
    for cloud in clouds:
        i, j = cloud
        ni, nj = i + di * s, j + dj * s
        if not (0 <= ni < N):
            ni = idx_transform(ni, N)
        if not (0 <= nj < N):
            nj = idx_transform(nj, N)
        
        moved_clouds.add((ni, nj))  
        #2 물의 양 1 증가 
        board[ni][nj] += 1
        
       
    #4 물복사버그 마법
    for cloud in moved_clouds:
        r, c = cloud
        for dr, dc in ((-1, -1), (-1, 1), (1, 1), (1, -1)):
            nr, nc = dr + r, dc + c
            if not (0<=nr<N and 0<=nc<N):
                continue
            if board[nr][nc] == 0:
                continue
            board[r][c] += 1
    #5 기존 구름 위치 제외한 새로운 구름 생성
    clouds = set()
    for i in range(N):
        for j in range(N):
            if board[i][j] < 2:
                continue
            if (i, j) in moved_clouds:
                continue
            board[i][j] -= 2
            clouds.add((i, j))
            
result = 0
for i in range(N):
    for j in range(N):
        result += board[i][j]
print(result)     