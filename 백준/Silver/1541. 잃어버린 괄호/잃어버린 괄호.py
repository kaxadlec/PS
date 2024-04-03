import sys
from collections import deque

formula = sys.stdin.readline()
stack = deque()
num_str = ''
for f in formula:
    if f == '+':
        num_str = ''
        stack.append(f)
    elif f == '-':
        num_str = ''
        stack.append(f)
    else:
        if stack and stack[-1] != '+' and stack[-1] != '-':
            f_temp = stack.pop()
            f_temp += f
            stack.append(f_temp)
            continue
        stack.append(f)

queue = stack
new_stack = deque()
while queue:
    element = queue.popleft()
    if element == '+':
        new_stack.append(element)
    elif element == '-':
        new_stack.append(element)
    else:
        if new_stack and new_stack[-1] == '+':
            top = new_stack.pop()
            next_top = new_stack.pop()
            new_stack.append(next_top + int(element))
            continue
        new_stack.append(int(element))

new_queue = new_stack
stack = deque()
while new_queue:
    element = new_queue.popleft()
    if element != '-':
        if stack and stack[-1] == '-':
            stack.pop()
            num = stack.pop()
            stack.append(num - element)
            continue
        stack.append(element)
    else:
        stack.append(element)

print(stack[-1])