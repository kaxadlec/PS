from sys import stdin

N, M = map(int, stdin.readline().split())
heights = list(map(int, stdin.readline().split()))

start = 0
end = max(heights)
result = 0

while start <= end:
    mid = start + (end - start) // 2
    home_tree = 0
    for h in heights:
        if h > mid:
            home_tree += (h - mid)

    if home_tree >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
