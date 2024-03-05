def func(level, start):
    if level == M:
        print(*path)
        return
    for i in range(start, N):
        if used[i] == 0:
            path.append(arr[i])
            used[i] = 1
            func(level+1, i+1)
            path.pop()
            used[i] = 0


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
path = []
used = [0]*(N+1)

func(0, 0)