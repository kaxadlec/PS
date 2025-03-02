# 코드를 작성해주세요
from sys import stdin
import heapq

n = int(stdin.readline())
arr = [int(stdin.readline()) for _ in range(n)]
pq = []
for i in range(n):
    num = arr[i]
    if num == 0:
        if len(pq) == 0:
            print(0)
        else:
            print(-1 * heapq.heappop(pq))
    else:
        heapq.heappush(pq, -1*num)
    
    # print(pq)
    
