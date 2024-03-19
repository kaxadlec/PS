def power(x, n, z):
    if n == 1:
        return x % z

    elif n % 2 == 0:    # 거듭제곱이 짝수 일때
        divided_x = power(x, n//2, z)
        return divided_x * divided_x % z

    elif n % 2 == 1:    # 거듭제곱이 홀수 일때
        divided_x = power(x, (n-1)//2, z)
        return divided_x * divided_x * x % z


A, B, C = map(int, input().split())
print(power(A, B, C))
