from sys import stdin
from itertools import combinations

N, M = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]

home_coordinate = []
chicken_restaurant_coordinate = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            home_coordinate.append((i, j))
        elif board[i][j] == 2:
            chicken_restaurant_coordinate.append((i, j))

distance = []
for n in range(len(chicken_restaurant_coordinate)):
    r, c = chicken_restaurant_coordinate[n]
    distance.append([])
    for home in home_coordinate:
        x, y = home
        dis = abs(r-x) + abs(c-y)
        distance[n].append(dis)

min_dis_sum = float('inf')
INF = float('inf')
for combo in combinations(distance, M):
    dis_sum = 0
    com_dis_list = [INF]*len(home_coordinate)
    for com in combo:
        for i in range(len(com)):
            com_dis_list[i] = min(com_dis_list[i], com[i])
    min_dis_sum = min(min_dis_sum, sum(com_dis_list))

print(min_dis_sum)

