from sys import stdin

M = int(stdin.readline().rstrip())
S = set()
for _ in range(M):
    operation = list(stdin.readline().rstrip().split())
    if len(operation) == 2:
        x = int(operation[1])
        if operation[0] == 'add' and x not in S:
            S.add(x)
        elif operation[0] == 'remove' and x in S:
            S.remove(x)
        elif operation[0] == 'check':
            if x in S:
                print(1)
            else:
                print(0)
        elif operation[0] == 'toggle':
            if x in S:
                S.remove(x)
            else:
                S.add(x)
    else:
        if operation[0] == 'all':
            S = set(i for i in range(1, 21))
        elif operation[0] == 'empty':
            S = set()