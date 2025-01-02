from sys import stdin

N = int(stdin.readline())
big_list = list(tuple(map(int, stdin.readline().split())) for _ in range(N))
big_rank = [1]*N
for i in range(N):
    for j in range(N):
        if i != j and big_list[i][0] < big_list[j][0] and big_list[i][1] < big_list[j][1]:
            big_rank[i] += 1

print(*big_rank)