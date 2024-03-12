from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
people_list = [int(input()) for _ in range(N)]
stack = deque()
cnt = 0
continuous = 1
for i in range(N):
    # cnt = 0
    current_person_value = people_list[i]
    while stack:
        top_person_value, top_person_continuous = stack[-1]
        if top_person_value < current_person_value:
            stack.pop()
            cnt += top_person_continuous
            continuous = 1

        elif top_person_value == current_person_value:
            if len(stack) == 1 and top_person_continuous == 0:  # 스택에 숫자 단 하나 존재
                cnt += 1
                stack.pop()
                continuous = top_person_continuous + 1
                break
            elif len(stack) == 1:   # 스택에 중복 숫자의 종류는 하나이나, 숫자의 개수는 여러개
                cnt += top_person_continuous
                continuous = top_person_continuous + 1
                stack.pop()
                break
            else:
                cnt += (top_person_continuous+1)
                continuous = top_person_continuous + 1
                stack.pop()
                break
        else:
            cnt += 1
            continuous = 1
            break
    stack.append((current_person_value, continuous))
    # print(cnt)
    # print('stack', stack)
print(cnt)
