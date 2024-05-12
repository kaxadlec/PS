from sys import stdin
from itertools import combinations


L, C = map(int, stdin.readline().split())
letters = list(stdin.readline().split())
letters.sort()
vowels = ['a', 'e', 'i', 'o', 'u']

for combo in combinations(letters, L):
    vowel_cnt = 0
    consonant_cnt = 0
    for c in combo:
        if c in vowels:
            vowel_cnt += 1
        else:
            consonant_cnt += 1
        if vowel_cnt >= 1 and consonant_cnt >= 2:
            result = ''.join(combo)
            print(result)
            break
