from sys import stdin
from collections import deque

n = int(stdin.readline())
arr = deque()
stack = deque()
result = []
for _ in range(n):
    arr.append(int(stdin.readline()))

for num in range(1, n+1):
    stack.append(num)
    result.append('+')

    while stack:
        if stack[-1] == arr[0]:
            stack.pop()
            result.append('-')
            arr.popleft()
        else:
            break

if stack:
    print('NO')
else:
    for res in result:
        print(res)

