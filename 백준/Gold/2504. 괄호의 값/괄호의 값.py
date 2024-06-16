from sys import stdin
from collections import deque

strs = stdin.readline().rstrip()
stack = deque()
parenthesis = ['(', ')', '[', ']']

for st in strs:
    if not stack:
        stack.append(st)
        continue
    elif stack[-1] == '(' and st == ')':
        stack.pop()
        if stack and stack[-1] not in parenthesis:
            x = stack.pop()
            stack.append(str(int(x) + 2))
        else:
            stack.append('2')
    elif stack[-1] == '[' and st == ']':
        stack.pop()
        if stack and stack[-1] not in parenthesis:
            x = stack.pop()
            stack.append(str(int(x) + 3))
        else:
            stack.append('3')
    elif stack[-1] not in parenthesis:
        if len(stack) > 1:
            if stack[-2] == '(' and st == ')':
                x, _ = stack.pop(), stack.pop()
                if stack and stack[-1] not in parenthesis:
                    y = stack.pop()
                    stack.append(str(2 * int(x) + int(y)))
                else:
                    stack.append(str(2 * int(x)))

            elif stack[-2] == '[' and st == ']':
                x, _ = stack.pop(), stack.pop()
                if stack and stack[-1] not in parenthesis:
                    y = stack.pop()
                    stack.append(str(3 * int(x) + int(y)))
                else:
                    stack.append(str(3 * int(x)))

            else:
                stack.append(st)
        elif len(stack) == 1:
            stack.append(st)
    else:
        stack.append(st)

if len(stack) == 1 and stack[0] not in parenthesis:
    print(stack[0])
else:
    print(0)
