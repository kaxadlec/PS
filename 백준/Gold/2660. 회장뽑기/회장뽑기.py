from collections import deque


def bfs(node):
    global cnt, level
    queue = deque()
    visited = [0]*(member_num+1)
    queue.append((node, 0))
    # print()
    # print('node', node)
    visited[node] = 1
    cnt += 1

    while queue:
        # print('cnt', cnt)
        if cnt == member_num:
            level = level + 1
            break
        current_node, level = queue.popleft()  # 현재 노드의 회원번호, 회원점수
        # print('current', current_node, 'level', level)
        for neighbor_node in graph[current_node]:   # 인접한 노드로 접근
            if visited[neighbor_node] == 0:     # 방문한 적 없는 노드라면
                # print('neighbor', neighbor_node)
                visited[neighbor_node] = 1      # 방문표시
                cnt += 1                # 방문표시횟수
                queue.append((neighbor_node, level+1))  # 인접노드 회원번호, 회원점수


member_num = int(input())
graph = [[] for _ in range(member_num+1)]
while 1:
    n1, n2 = map(int, input().split())
    if n1 == - 1 and n2 == -1:
        break
    graph[n1].append(n2)
    graph[n2].append(n1)

min_score = 21e8
candidate_list = deque()
for i in range(1, member_num+1):
    cnt = 0
    level = 0
    bfs(i)
    score = level
    if score == 0:
        continue
    if min_score > score:
        min_score = score
        candidate_score = score
        candidate_num = 1
        candidate_list.clear()
        candidate_list.append(i)
    elif min_score == score:
        candidate_num += 1
        candidate_list.append(i)

print(candidate_score, candidate_num)
print(*candidate_list)
