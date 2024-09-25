from sys import stdin

initial_n = int(stdin.readline())
int_n = initial_n
res = 0
while int_n > 0:
    int_n -= 1
    str_n = str(int_n)
    comparison = 0
    for s in str_n:
        comparison += int(s)

    if initial_n - int_n == comparison:
        res = int_n

print(res)