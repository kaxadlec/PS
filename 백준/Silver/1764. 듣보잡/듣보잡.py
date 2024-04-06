from sys import stdin

N, M = map(int, stdin.readline().split())
unheard = set(stdin.readline().strip() for _ in range(N))
unseen = set(stdin.readline().strip() for _ in range(M))
overlap = unheard & unseen
print(len(overlap))
overlap_list = list(overlap)
overlap_list.sort()
for i in range(len(overlap)):
    print(overlap_list[i])

