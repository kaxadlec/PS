def backtrack(level, current_val):
    global max_result, min_result
    if level == N:
        if current_val > max_result:
            max_result = current_val
        if current_val < min_result:
            min_result = current_val
        return

    if operator_used[0]:
        operator_used[0] -= 1
        backtrack(level + 1, current_val + nums_arr[level])
        operator_used[0] += 1
    if operator_used[1]:
        operator_used[1] -= 1
        backtrack(level + 1, current_val - nums_arr[level])
        operator_used[1] += 1
    if operator_used[2]:
        operator_used[2] -= 1
        backtrack(level + 1, current_val * nums_arr[level])
        operator_used[2] += 1
    if operator_used[3]:
        operator_used[3] -= 1
        if current_val < 0:
            backtrack(level + 1, -(-current_val // nums_arr[level]))
        else:
            backtrack(level + 1, current_val // nums_arr[level])
        operator_used[3] += 1


N = int(input())
nums_arr = list(map(int, input().split()))
operator_used = list(map(int, input().split()))  # + - * // 의 수
min_result = float('inf')
max_result = -float('inf')
backtrack(1, nums_arr[0])
print(max_result)
print(min_result)
