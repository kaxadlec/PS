def recursion(A, B, N):
    global cnt
    if N == 1:
        arr.append((A, B))
        cnt += 1
        return

    recursion(A, 6-B-A, N-1)
    arr.append((A, B))
    cnt += 1
    recursion(6-B-A, B, N-1)


N = int(input())  # 첫번째 기둥에 쌓인 원판 개수
cnt = 0
arr = []
recursion(1, 3, N)
print(cnt)
for i in range(cnt):
    print(*arr[i])
