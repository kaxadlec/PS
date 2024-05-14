from sys import stdin
import heapq


def go_party(st, d):
    d[st] = 0
    pq = []
    heapq.heapify(pq)
    heapq.heappush(pq, (0, st))
    while pq:
        weight, node = heapq.heappop(pq)
        if d[node] < weight:
            continue
        for next in graph[node]:
            next_cost, next_node = next
            if next_node == st:
                continue
            nnext_cost = next_cost + weight
            if nnext_cost < d[next_node]:
                d[next_node] = nnext_cost
                heapq.heappush(pq, (nnext_cost, next_node))


N, M, X = map(int, stdin.readline().split())
graph = [[] for _ in range(N+1)]
INF = float('inf')
for i in range(M):
    st, en, w = map(int, stdin.readline().split())
    graph[st].append((w, en))

result = [0] * (N+1)
for st_node in range(1, N+1):
    d_table = [INF] * (N + 1)
    go_party(st_node, d_table)
    if st_node == X:
        for i in range(1, N+1):
            result[i] += d_table[i]
    else:
        result[st_node] += d_table[X]

print(max(result))
