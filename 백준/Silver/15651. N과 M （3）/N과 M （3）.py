def func(level):
    if level == M:
        print(*path)
        return

    for i in range(1, N+1):
        path.append(i)
        func(level+1)
        path.pop()


N, M = map(int, input().split())
path = []
func(0)