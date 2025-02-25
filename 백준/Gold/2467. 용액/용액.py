from sys import stdin

N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
arr.sort()

min_sum = 21e8


for i in range(N-1):
    first_num = arr[i]

    start = i + 1
    end = N - 1
    target_num = -first_num
    close_to_target_num = None
    min_gap = 21e8

    while start <= end:
        mid = (start + end) // 2
        gap = abs(target_num - arr[mid])
        if gap < min_gap:
            close_to_target_num = arr[mid]
            min_gap = gap

        if arr[mid] > target_num:
            end = mid - 1
        else:
            start = mid + 1

    second_num = close_to_target_num
    if min_sum > abs(first_num + second_num):
        min_sum = abs(first_num + second_num)
        result = (first_num, second_num)


print(*result)



