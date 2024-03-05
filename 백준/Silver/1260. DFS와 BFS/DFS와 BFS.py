from collections import deque


def dfs(node):
    print(node, end=' ')
    visited1[node] = 1
    for neighbor in graph[node]:
        if visited1[neighbor] == 0:
            dfs(neighbor)


def bfs(sn):
    queue.append(sn)
    visited2[sn] = 1
    print(sn, end=' ')
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if visited2[neighbor] == 0:
                queue.append(neighbor)
                print(neighbor, end=' ')
                visited2[neighbor] = 1


# 정점의 개수, 간선의 개수, 정점의 번호
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    # 간선은 양방향
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# 정점번호 오름차순으로 정렬
for g in graph:
    g.sort()
visited1 = [0]*(N+1)
visited1[V] = 1
dfs(V)
print()

visited2 = [0]*(N+1)
queue = deque()
bfs(V)


