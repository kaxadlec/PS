from collections import deque
N = int(input())
cards = [(i+1) for i in range(N)]
queue = deque(cards)

while queue:
    card1 = queue.popleft()
    if queue:
        card2 = queue.popleft()
        queue.append(card2)
    else:
        result = card1

print(result)
