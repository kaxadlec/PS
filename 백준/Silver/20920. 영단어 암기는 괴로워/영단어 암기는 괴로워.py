from sys import stdin

N, M = map(int, stdin.readline().split())
word_dict = dict()
for _ in range(N):
    word = stdin.readline().rstrip()
    if len(word) < M:
        continue
    if word_dict.get(word) is None:
        word_dict[word] = 1
    else:
        word_dict[word] += 1

items = word_dict.items()
sorted_items = sorted(items, key=lambda x: (-x[1], -len(x[0]), x[0]))
for item_name in sorted_items:
    print(item_name[0])