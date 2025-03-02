from sys import stdin
T = int(stdin.readline())
n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
b = list(map(int, stdin.readline().split()))

def lower_bound(arr, target):
    start = 0
    end = len(arr) - 1
    min_idx = 21e8
    flag = 0
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == target:
            end = mid - 1
            min_idx = min(min_idx, mid)
            if flag == 0:
                flag = 1
        elif arr[mid] > target:
            end = mid - 1
        else: # mid < target
            start = mid + 1
    
    if flag == 1:
        return min_idx
    else:
        return False
        
def upper_bound(arr, target):
    start = 0
    end = len(arr) - 1
    max_idx = -1
    flag = 0
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == target:
            start = mid + 1
            max_idx = max(max_idx, mid)
            if flag == 0:
                flag = 1
        elif arr[mid] > target:
            end = mid - 1
        else: # mid < target
            start = mid + 1
    
    if flag == 1:
        return max_idx
    else:
        return -1
        
    
a_prefix_sum = []
for i in range(n):
    pre_sum = 0
    for j in range(i, n):
        pre_sum += a[j]
        a_prefix_sum.append(pre_sum)


b_prefix_sum = []
for i in range(m):
    pre_sum = 0
    for j in range(i, m):
        pre_sum += b[j]
        b_prefix_sum.append(pre_sum)
     
a_prefix_sum.sort()
b_prefix_sum.sort()

# print(a_prefix_sum)
# print(b_prefix_sum)

result = 0
for i in range(len(a_prefix_sum)):
    upper = upper_bound(b_prefix_sum, T - a_prefix_sum[i])
    lower = lower_bound(b_prefix_sum, T -a_prefix_sum[i])
    # print(upper, lower)
    if upper != -1 and lower != -1:
        cnt = upper - lower + 1
        result += cnt
print(result)
        
    
