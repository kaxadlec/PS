# 트리의 부모 찾기
from sys import stdin

def DFS(graph, idx, visited):
    parent_list = [0 for _ in range(n+1)]
    stack = [idx]
    visited[idx] = True

    while stack:
        current = stack.pop()

        if not visited[current]:
            visited[current] = True

        for child in graph[current]:
            if not visited[child]:
                stack.append(child)
                parent_list[child] = current

    return parent_list

if __name__ == '__main__':
    n = int(stdin.readline().strip())
    graph = [[] for _ in range(n+1)]

    for _ in range(n-1):
        a, b = map(int, stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False for _ in range(n+1)]
    parent_list = DFS(graph, 1, visited)

    for parent in parent_list[2:]:
        print(parent)