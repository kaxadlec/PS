N, K = map(int, input().split())
top = 1
for n in range(1, N+1):
    top = top * n
bottom_one = 1
bottom_two = 1
for i in range(1, N-K+1):
    bottom_one = bottom_one * i
for k in range(1, K+1):
    bottom_two = bottom_two * k

print(top//(bottom_one*bottom_two))


