import heapq

N = int(input())
pq_cards = [int(input()) for _ in range(N)]

heapq.heapify(pq_cards)
cnt = 0
while len(pq_cards) > 1:
    card1 = heapq.heappop(pq_cards)
    card2 = heapq.heappop(pq_cards)
    heapq.heappush(pq_cards, card1+card2)
    cnt += (card1+card2)

print(cnt)



