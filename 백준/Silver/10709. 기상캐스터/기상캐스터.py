# 행 개수, 열 개수
H, W = map(int, input().split())
for i in range(H):
    arr = input()
    temp_j = -1
    for j in range(W):
        if arr[j] == 'c':
            temp_j = j
        if temp_j == -1:
            print(temp_j, end=' ')
        else:
            print(j-temp_j, end=' ')
    print()
