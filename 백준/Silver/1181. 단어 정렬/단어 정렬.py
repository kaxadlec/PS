from sys import stdin
import heapq

N = int(stdin.readline())
pq = []
for _ in range(N):
    word = stdin.readline().rstrip()
    heapq.heappush(pq, (len(word), word))

pre_word = ''
while pq:
    length, word = heapq.heappop(pq)
    if pre_word != word:
        print(word)
        pre_word = word
