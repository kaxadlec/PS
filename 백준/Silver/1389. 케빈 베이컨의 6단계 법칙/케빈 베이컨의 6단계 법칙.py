from sys import stdin
from collections import deque


def bfs(node):
    global result
    queue = deque()
    queue.append((node, 0))
    visited = [0]*(N+1)
    visited[node] = 1
    while queue:
        cur_node, level = queue.popleft()
        result += level
        for friend in adj_list[cur_node]:
            if visited[friend] == 1:
                continue
            visited[friend] = 1
            queue.append((friend, level+1))


N, M = map(int, stdin.readline().split())
adj_list = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, stdin.readline().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

min_result = 21e8
min_user = 0
for user in range(1, N+1):
    result = 0
    bfs(user)
    if result < min_result:
        min_result = result
        min_user = user

print(min_user)
