from sys import stdin


def backtrack(level):
    if level == M:
        print(*path)
        return

    for i in range(N):
        if i == 0:
            pre_num = -1
        if used[i] == 1:
            continue
        num = arr[i]
        if num == pre_num:
            continue
        path.append(num)
        used[i] = 1
        backtrack(level+1)
        used[i] = 0
        pre_num = path.pop()


N, M = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
arr.sort()
used = [0]*N
path = []
backtrack(0)