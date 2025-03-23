from sys import stdin
import heapq

N = int(stdin.readline())
classes = [tuple(map(int, stdin.readline().split())) for _ in range(N)]
pq = []

classes.sort(key=lambda x:x[1])
for claxx in classes:
    _, st, en = claxx
    if pq and pq[0][0] <= st:
        heapq.heappop(pq)
    heapq.heappush(pq, (en, (st, en)))
    
print(len(pq))
