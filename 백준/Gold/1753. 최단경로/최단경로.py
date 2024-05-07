from sys import stdin
import heapq

V, E = map(int, stdin.readline().split())
st_v = int(stdin.readline())
graph = [[] for _ in range(V+1)]
INF = float('inf')
d = [INF] * (V+1)
for i in range(E):
    a, b, w = map(int, stdin.readline().split())
    graph[a].append((w, b))

pq = []
heapq.heappush(pq, (0, st_v))
d[st_v] = 0
while pq:
    dist, cur_v = heapq.heappop(pq)
    for next in graph[cur_v]:
        cost, vertex = next
        next_dist = dist + cost
        if next_dist < d[vertex]:
            d[vertex] = next_dist
            heapq.heappush(pq, (next_dist, vertex))

for i in range(1, V+1):
    if d[i] == INF:
        print('INF')
    else:
        print(d[i])