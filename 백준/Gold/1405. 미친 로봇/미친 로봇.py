# 코드를 작성해주세요
from sys import stdin
from collections import deque 


N, east, west, south, north = map(int, stdin.readline().split())
pre_prob_list = [east, west, south, north]
prob_list = [i*0.01 for i in pre_prob_list]
visited = [[0]*(2*N+1) for _ in range(2*N+1)]
path = [0] * N
result = 0

def backtrack(turn, i, j, prob, visited):
    global result 
    # print("턴", turn)
    # print(i, j)
    # print("확률", prob)
    # print(visited)
    
    if visited[i][j] == 1:
        return
        
    if turn == N:
        result += prob
        return
        
    
        
    for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ni, nj = di + i, dj + j
        if not (0 <= ni < 2*N+1 and 0 <= nj < 2*N+1):
            continue
        if di == 0 and dj == 1:
            idx = 0
        elif di == 0 and dj == -1:
            idx = 1
        elif di == 1 and dj == 0:
            idx = 2
        elif di == -1 and dj == 0:
            idx = 3
            
        visited[i][j] = 1
        backtrack(turn + 1, ni, nj, prob * prob_list[idx], visited)
        visited[i][j] = 0

backtrack(0, N, N, 1, visited)

print(result)