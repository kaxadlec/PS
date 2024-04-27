from sys import stdin

N = int(stdin.readline())
n_set = set(map(int, stdin.readline().split()))  
M = int(stdin.readline())
m_arr = list(map(int, stdin.readline().split()))

for m in m_arr:
    if m in n_set:  
        print(1)
    else:
        print(0)