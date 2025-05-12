from sys import stdin
from itertools import combinations
    
    
N = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
min_res = float('inf')
nums = [i for i in range(1, N+1)]
all_team = set(nums)

for team_size in range(1, N // 2 + 1):
    for combo in combinations(nums, team_size): 
        start_team = set(combo)
        link_team = all_team - start_team
        
        # print("start_team", start_team)
        # print("link_team", link_team)
        start_sum = 0
        link_sum = 0
    
        for combo in combinations(start_team, 2):
            a, b = combo
            start_sum += board[a-1][b-1]
            start_sum += board[b-1][a-1]
        
    
        for combo in combinations(link_team, 2):
            a, b = combo
            link_sum += board[a-1][b-1]
            link_sum += board[b-1][a-1]
        
        min_res = min(min_res, abs(start_sum - link_sum))
        if min_res == 0:
            break
    if min_res == 0:
            break

print(min_res)           
