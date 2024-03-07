def func(level, start):
    if level == 6:
        print(*path)
        return

    for i in range(start, len(s_set)):
        path.append(s_set[i])
        func(level+1, i+1)
        path.pop()


while 1:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    k = arr[0]
    s_set = arr[1:]
    path = []
    func(0, 0)
    print()