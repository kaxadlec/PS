n, m = map(int, input().split())
points = list(map(int, input().split()))
segments = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

def lower_bound(target):
    left = 0
    right = n - 1
    min_idx = n

    while left <= right:
        mid = (left + right) // 2
        if points[mid] >= target:
            right = mid - 1
            min_idx = min(min_idx, mid)
        else:
            left = mid + 1

    return min_idx


def upper_bound(target):
    left = 0
    right = n - 1
    min_idx = n

    while left <= right:
        mid = (left + right) // 2
        if points[mid] > target:
            right = mid - 1
            min_idx = min(min_idx, mid)
        else:
            left = mid + 1
    
    return min_idx

points.sort()
for seg in segments:
    st, en = seg
    result = upper_bound(en) - lower_bound(st)
    print(result)
