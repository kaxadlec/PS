from sys import stdin
import heapq

vertex = int(stdin.readline())
edge = int(stdin.readline())
adj = [[] for _ in range(vertex+1)]
INF = float("inf")
d = [INF] * (vertex + 1)
for _ in range(edge):
    s, e, w = map(int, stdin.readline().split())
    adj[s].append((w, e))
s_vertex, e_vertex = map(int, stdin.readline().split())


def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    d[start] = 0

    while pq:
        dist, cur_node = heapq.heappop(pq)
        if d[cur_node] < dist:
            continue
        for neighbor in adj[cur_node]:
            neighbor_dist, neighbor_node = neighbor
            cost = dist + neighbor_dist
            if cost < d[neighbor_node]:
                d[neighbor_node] = cost
                heapq.heappush(pq, (cost, neighbor_node))


dijkstra(s_vertex)
print(d[e_vertex])
