from sys import stdin

strings = stdin.readline().rstrip()
boom_strings = list(stdin.readline().rstrip())
boom_strings_len = len(boom_strings)
stack = []
for st in strings:
    stack.append(st)
    if len(stack) >= boom_strings_len:
        while stack[-boom_strings_len:] == boom_strings:
            del stack[-boom_strings_len:]
result = "".join(stack) if stack else "FRULA"
print(result)
