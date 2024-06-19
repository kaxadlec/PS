from sys import stdin

T = int(stdin.readline())
for tc in range(T):
    print(f'Case #{tc+1}:')
    N, Q = map(int, stdin.readline().split())
    arr = list(map(int, stdin.readline().split()))
    res = []
    for i in range(N):
        part_sum = 0
        for j in range(i, N):
            part_sum += arr[j]
            res.append(part_sum)
    res.sort()

    for _ in range(Q):
        L, R = map(int, stdin.readline().split())
        res_sum = sum(res[L-1:R])
        print(res_sum)
