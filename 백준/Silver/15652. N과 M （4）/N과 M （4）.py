def func(level, start):
    if level == M:
        print(*path)
        return
    for i in range(start, N+1):
        path.append(i)
        func(level+1, i)
        path.pop()


N, M = map(int, input().split())
path = []
func(0, 1)