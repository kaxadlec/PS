from collections import deque

N, K = map(int, input().split())
nums = input()
stack = deque()
final_stack_len = N-K

for i in range(N):
    num = int(nums[i])

    if i == 0:
        stack.append(num)
        continue


    if stack[-1] < num:
        while stack:
            if final_stack_len-len(stack) == N-i:
                break
            if stack[-1] < num:
                stack.pop()
            else:
                break
        stack.append(num)
    else:
        if final_stack_len == len(stack):
            break
        stack.append(num)

for i in list(stack):
    print(i, end='')