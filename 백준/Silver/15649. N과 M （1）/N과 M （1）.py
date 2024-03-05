"""
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
"""


def func(level):
    if level == M:
        print(*path)
        return

    for i in range(1, N+1):
        if used[i] == 0:
            path.append(i)
            used[i] = 1
            func(level+1)
            path.pop()
            used[i] = 0


N, M = map(int, input().split())
path = []
used = [0]*(N+1)
func(0)
