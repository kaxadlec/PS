from sys import stdin
import heapq

pq = []
N = int(stdin.readline())
for _ in range(N):
    x = int(stdin.readline())
    if x == 0:
        if len(pq) == 0:
            print(0)
        else:
            abs_elem, elem = heapq.heappop(pq)
            print(elem)
    else:
        heapq.heappush(pq, (abs(x), x))