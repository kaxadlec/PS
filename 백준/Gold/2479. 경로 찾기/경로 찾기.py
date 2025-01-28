from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split())
binary_codes = [stdin.readline().rstrip() for _ in range(N)]
st, en = map(int, stdin.readline().split())
st, en = st - 1, en - 1


def bfs(start_node):
    result_min_len = 21e8
    result = []
    queue = deque()
    queue.append((start_node, [start_node]))
    visited = [0 for _ in range(N)]
    visited[start_node] = 1
    while queue:
        # print(queue)
        cur_node, path = queue.popleft()

        if path[-1] == en and len(path) < result_min_len:
            result_min_len = len(path)
            result = path[:]

        for next_node in range(N):
            next_path = path[:]
            if visited[next_node] == 1:
                continue
            if sum(1 for a, b in zip(binary_codes[cur_node], binary_codes[next_node]) if a != b) == 1:
                next_path.append(next_node)
                queue.append((next_node, next_path))
                visited[next_node] = 1
    return result

path_res = bfs(st)
path_res = [i+1 for i in path_res]
if len(path_res) > 0:
    print(*path_res)
else:
    print(-1)