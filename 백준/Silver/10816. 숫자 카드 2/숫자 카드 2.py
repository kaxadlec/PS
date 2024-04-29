from sys import stdin

N = int(stdin.readline())
cards_arr = list(map(int, stdin.readline().split()))
cards_dict = {}
for card in cards_arr:
    if cards_dict.get(card) is None:
        cards_dict[card] = 1
    else:
        cards_dict[card] += 1

M = int(stdin.readline())
his_cards = list(map(int, stdin.readline().split()))
for card in his_cards:
    if cards_dict.get(card) is None:
        print(0, end=' ')
    else:
        print(cards_dict.get(card), end=' ')