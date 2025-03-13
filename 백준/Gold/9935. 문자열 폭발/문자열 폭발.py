from sys import stdin
from collections import deque

strings = stdin.readline().rstrip()
boom_strings = stdin.readline().rstrip()
'''
폭발문자열 모두 일단 폭발
그리고 다 이어붙임
근데 거기서 폭발문자열 다시 생길 수 있음
이게 반복됨
'''
# print(strings)
# print(boom_strings)

stack = deque()
final_idx = len(boom_strings) - 1

for i in range(len(strings)):
    if stack and stack[-1][1] is not None and len(boom_strings) > 1 and strings[i] == boom_strings[stack[-1][1] + 1]:
        stack.append((strings[i], stack[-1][1] + 1))
        
        if stack[-1][1] == final_idx:
            for j in range(final_idx+1):
                stack.pop()
    elif strings[i] == boom_strings[0]:
        if len(boom_strings) == 1:
            continue
        stack.append((strings[i], 0))
        
    elif stack and stack[-1][1] is None:
        stack.append((strings[i], None))
    else:
        stack.append((strings[i], None))
    # print(stack)

if not stack:
    print("FRULA")
else:
    for st in stack:
        print(st[0], end="")


    