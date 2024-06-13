from sys import stdin
from collections import deque

T = int(stdin.readline())
for tc in range(T):
    perform = stdin.readline().rstrip()
    _ = int(stdin.readline().rstrip())
    input_arr = stdin.readline().strip('[]\n')
    if input_arr:
        number_str = list(input_arr.split(','))
        number_deque = deque(number_str)
    else:
        number_deque = deque()

    # 수행할 함수에서, reverse 중복 줄이기
    perform_stack = deque()
    for p in perform:
        if perform_stack and perform_stack[-1] == 'R' and p == 'R':
            perform_stack.pop()
            continue
        perform_stack.append(p)

    # 주어진 정수 배열에 함수 수행
    error_flag = 0
    reverse_flag = 0
    for per in perform_stack:
        if per == 'R':
            if reverse_flag:
                reverse_flag = 0
            else:
                reverse_flag = 1
        else:
            if number_deque:
                if reverse_flag:
                    number_deque.pop()
                else:
                    number_deque.popleft()
            else:
                error_flag = 1
                break

    if error_flag:
        print('error')
    else:
        if reverse_flag:
            number_deque.reverse()
        result = '['
        for i in range(len(number_deque)):
            if i == len(number_deque)-1:
                result += number_deque[i]
            else:
                result += number_deque[i]
                result += ','
        result += ']'
        print(result)
