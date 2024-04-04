from collections import deque

N, K = map(int, input().split())
visited = [0]*100002

if N == K:
    min_cnt = 0

elif N > K:
    min_cnt = N-K

elif N < K:
    queue = deque()
    queue.append((N, N, N, 0))
    while queue:
        backward, forward, teleport, cnt = queue.popleft()
        if backward == K or forward == K or teleport == K:
            min_cnt = cnt
            break
        else:
            if 0 <= backward <= 100000 and visited[backward] == 0:
                visited[backward] = 1
                queue.append((backward-1, backward+1, backward*2, cnt+1))
            if 0 <= forward <= 100000 and visited[forward] == 0:
                visited[forward] = 1
                queue.append((forward - 1, forward + 1, forward * 2, cnt + 1))
            if 0 <= teleport <= 100000 and visited[teleport] == 0:
                visited[teleport] = 1
                queue.append((teleport - 1, teleport + 1, teleport * 2, cnt + 1))

print(min_cnt)