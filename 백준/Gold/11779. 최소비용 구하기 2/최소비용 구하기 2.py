from sys import stdin
import heapq

n = int(stdin.readline())
m = int(stdin.readline())
bus_info = [list(map(int, stdin.readline().split())) for _ in range(m)]
start, end = map(int, stdin.readline().split())
adj = [[] for _ in range(n+1)]
INF = float('inf')
distance = [INF] * (n+1)
path = [0] * (n+1)
   
for i in range(m):
    st, en, w = bus_info[i]
    adj[st].append((w, en))

pq = []
distance[start] = 0
heapq.heappush(pq, (0, start))
# print(adj)
while pq:
    dist, node = heapq.heappop(pq)
    
    if node == end:
        
        result_path = [node]
        while 1:
            pre_node = path[node]
            result_path.append(pre_node)
            node = pre_node
            if pre_node == start:
                break
        result_path.reverse()
        print(dist)
        print(len(result_path))
        print(*result_path)
        break

    if distance[node] < dist:
        continue
        
    for neighbor_dist, neighbor_node in adj[node]:
        cost = neighbor_dist + dist
        
        if cost < distance[neighbor_node]:
            distance[neighbor_node] = cost
            path[neighbor_node] = node
            heapq.heappush(pq, (cost, neighbor_node))

