def func(level, start):
    if level == M:
        print(*path)
        return

    for i in range(start, N+1):
        path.append(i)
        func(level+1, i+1)
        path.pop()


N, M = map(int, input().split())
path = []
func(0, 1)