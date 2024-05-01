from sys import stdin
from collections import deque


def bfs(node):
    global cnt

    dist = [-1] * (N + 1)
    queue = deque()
    queue.append(node)
    dist[node] = 0
    while queue:
        cur = queue.popleft()
        if 0 < dist[cur] < 3:
            cnt += 1
        elif dist[cur] == 3:
            return
        for neighbor in graph[cur]:
            if neighbor is None:
                break
            if dist[neighbor] != -1:
                continue
            dist[neighbor] = dist[cur] + 1
            queue.append(neighbor)


N = int(stdin.readline())
M = int(stdin.readline())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

cnt = 0
bfs(1)
print(cnt)
