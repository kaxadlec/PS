from sys import stdin

N, M = map(int, stdin.readline().split())

pw_dict = dict()
for i in range(N):
    addr, pw = stdin.readline().split()
    pw_dict[addr] = pw

for i in range(M):
    addr = stdin.readline().rstrip()
    print(pw_dict[addr])