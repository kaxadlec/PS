from sys import stdin


def dfs(node, visited):
    global cnt

    visited[node] = 1
    for neighbor in graph[node]:
        if visited[neighbor] == 1:
            continue
        cnt += 1
        dfs(neighbor, visited)


T = int(stdin.readline())
for tc in range(T):
    N, M = map(int, stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [0]*(N+1)
    cnt = 0
    dfs(1, visited)
    print(cnt)
