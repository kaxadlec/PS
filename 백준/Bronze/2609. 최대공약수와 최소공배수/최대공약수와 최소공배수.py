n1, n2 = map(int, input().split())
max_num = max(n1, n2)
min_num = min(n1, n2)
for n in range(min_num, -1, -1):
    if min_num % n == 0:
        if max_num % n == 0:
            result1 = n
            break

i = 1
while 1:
    if (max_num*i) % min_num == 0:
        result2 = max_num*i
        break
    else:
        i += 1

print(result1)
print(result2)