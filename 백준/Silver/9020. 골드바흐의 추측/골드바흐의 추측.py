T = int(input())

for tc in range(T):
    num = int(input())
    # even
    if num % 2 == 0:
        n1 = num // 2
    # odd
    else:
        n1 = (num + 1) // 2 - 1

    while 1:
        false_check = 0
        for i in range(2, n1//2+1):
            if n1 % i == 0:
                n1 -= 1
                false_check = 1
                break
        if false_check == 1:
            continue

        n2 = num - n1
        for j in range(2, n2//2+1):
            if n2 % j == 0:
                n1 -= 1
                false_check = 1
                break
        if false_check == 1:
            continue
        else:
            break

    print(n1, end=' ')
    print(n2)





