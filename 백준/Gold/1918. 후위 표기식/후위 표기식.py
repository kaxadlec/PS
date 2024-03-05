from collections import deque
formula = input()
stack = deque()
order = {
    '(': 3,
    '*': 1,
    '/': 1,
    '+': 2,
    '-': 2
}
postfix = ''
for s in formula:
    if s == '+' or s == '-' or s == '*' or s == '/':
        while stack:
            item = stack.pop()
            if order.get(item) <= order.get(s):  # 들어오는 것이 우선순위 값 클 때
                postfix += item
            else:
                stack.append(item)
                break
        stack.append(s)
    elif s == '(':
        stack.append(s)
    elif s == ')':
        while stack:
            item = stack.pop()
            if item == '(':
                break
            else:
                postfix += item
    else:
        postfix += s
    # print(stack, postfix)
while stack:
    postfix += stack.pop()

print(postfix)
