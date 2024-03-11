from collections import deque

N = int(input())
stack = deque()
cnt = 0
for i in range(N):
    current = int(input())
    if i == 0:
        stack.append(current)
    else:
        if stack[-1] > current:
            cnt += len(stack)
            stack.append(current)
        elif stack[-1] <= current:
            while 1:
                if not stack:
                    stack.append(current)
                    break
                if stack[-1] > current:
                    cnt += len(stack)
                    stack.append(current)
                    break
                stack.pop()

print(cnt)