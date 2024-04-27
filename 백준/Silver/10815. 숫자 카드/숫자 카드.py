from sys import stdin

N = int(stdin.readline())
cards = set(map(int, stdin.readline().split()))
M = int(stdin.readline())
is_cards = list(map(int, stdin.readline().split()))

for i in range(M):
    print(int(is_cards[i] in cards), end=' ')