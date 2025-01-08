from sys import stdin

n = int(stdin.readline())
result = 1

for i in range(1, n+1):
    result *= i
   
print(result)