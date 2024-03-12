from collections import deque
N = int(input())
original_num_list = list(map(int, input().split()))
indexed_num_list = [(idx, value) for idx, value in enumerate(original_num_list)]
stack = deque()
result = [-1]*N
for i in range(N):
    current_num = indexed_num_list[i]
    if i == 0:
        stack.append(current_num)
    else:
        if stack[-1][1] < current_num[1]:
            result[stack[-1][0]] = current_num[1]
            stack.pop()
            while stack:
                if stack[-1][1] < current_num[1]:
                    result[stack[-1][0]] = current_num[1]
                    stack.pop()
                else:
                    break
            stack.append(current_num)
        else:
            stack.append(current_num)

print(*result)
