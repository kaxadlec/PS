def dfs(node):
    global cnt
    for neighbor in adj[node]:
        if visited[neighbor] == 1:
            continue
        visited[neighbor] = 1
        cnt += 1
        dfs(neighbor)


N = int(input())
E = int(input())
adj = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for i in range(E):
    n1, n2 = map(int, input().split())
    adj[n1].append(n2)
    adj[n2].append(n1)
cnt = 0
visited[1] = 1
dfs(1)
print(cnt)
