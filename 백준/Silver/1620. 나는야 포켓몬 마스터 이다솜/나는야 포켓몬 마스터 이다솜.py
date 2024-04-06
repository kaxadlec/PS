from sys import stdin

N, M = map(int, stdin.readline().split())
pokemon_collection = {}
numeric_pokemon_collection = {}
for i in range(N):
    pokemon = stdin.readline().strip()
    pokemon_collection[pokemon] = i+1
    numeric_pokemon_collection[i+1] = pokemon

for _ in range(M):
    pokemon = stdin.readline().strip()
    if pokemon.isnumeric():
        print(numeric_pokemon_collection[int(pokemon)])
    else:
        print(pokemon_collection[pokemon])
