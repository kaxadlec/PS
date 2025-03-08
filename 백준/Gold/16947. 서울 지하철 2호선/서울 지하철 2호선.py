from sys import stdin
from collections import deque

N = int(stdin.readline())
adj_list = [[] for _ in range(N+1)]
for _ in range(N):
    n1, n2 = map(int, stdin.readline().split())
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

def find_cycle():
    visited = [0]*(N+1)
    parents = [-1]*(N+1)
    cycle = set()
    
    stack = deque()
    cycle_flag = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            stack.append((i, - 1))
            while stack:
                cur_node, parent_node = stack.pop()
                # print("cur", "parent", cur_node, parent_node)
                visited[cur_node] = 1
                parents[cur_node] = parent_node
                for neighbor_node in adj_list[cur_node]:
                    # print("neighbor", neighbor_node)
                    if neighbor_node == parent_node:
                        continue
                    if visited[neighbor_node] == 0:
                        stack.append((neighbor_node, cur_node))
                    else: # 사이클 발견
                        in_cycle_node = cur_node
                        while neighbor_node != in_cycle_node:
                            cycle.add(in_cycle_node)
                            in_cycle_node = parents[in_cycle_node]
                        cycle.add(neighbor_node)
                        cycle_flag = 1
                        break
                if cycle_flag == 1:
                    break
        if cycle_flag == 1:
            break   
    return cycle 
    
    
def find_dist(cycle):
    queue = deque()
    dist = [-1] * (N+1)
    for i in range(1, N+1):
        if i in cycle:
            queue.append(i)
            dist[i] = 0
            
    while queue:
        cur = queue.popleft()
        for neighbor in adj_list[cur]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[cur] + 1
                queue.append(neighbor)
    print(*dist[1:])
    
cycle = find_cycle()
find_dist(cycle)

