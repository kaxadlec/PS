import sys
from collections import deque
T = int(sys.stdin.readline())
for _ in range(T):
    p_str = sys.stdin.readline().strip()
    stack = deque()
    for p in p_str:
        if len(stack) == 0:
            stack.append(p)
            continue

        if stack[-1] == '(':
            if p == '(':
                stack.append(p)
            else:
                stack.pop()

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
