import sys
from itertools import product

target_channel = sys.stdin.readline().strip()
ruined_cnt = int(sys.stdin.readline().strip())
buttons = [i for i in range(0, 10)]

if ruined_cnt == 0:
    print(min(len(target_channel), abs(100-int(target_channel))))
elif ruined_cnt == 10:
    print(abs(100-int(target_channel)))
else:
    ruined_buttons = list(sys.stdin.readline().strip().split())
    int_ruined_buttons = list(map(int, ruined_buttons))
    normal_buttons = set(buttons) - set(int_ruined_buttons)

    min_diff = float('inf')
    closest_num = None
    digits = list(normal_buttons)
    digits.sort()
    no_zero_digits = [d for d in digits if d != 0]
    closest_num1, closest_num2, closest_num3 = 1e9, 1e9, 1e9
    for length in range(len(target_channel) - 1, len(target_channel) + 2):
        if length > 0 and length == len(target_channel) - 1:
            closest_num1 = int(''.join(str(digits[-1])*(len(target_channel) - 1)))
            
        elif length == len(target_channel) + 1:
            permutations = product(no_zero_digits, *([digits]*(length-1)))
            for perm in permutations:
                closest_num3 = int(''.join(map(str, perm)))
                break
        else:
            if len(target_channel) == 1:
                permutations = product(digits, repeat=len(target_channel))
            else:
                permutations = product(no_zero_digits, *([digits]*(length-1)))
            for perm in permutations:
                num = int(''.join(map(str, perm)))
                diff = abs(num - int(target_channel))
                if diff < min_diff:
                    min_diff = diff
                    closest_num2 = num

    close1 = abs(int(target_channel) - closest_num1)
    close2 = abs(int(target_channel) - closest_num2)
    close3 = abs(int(target_channel) - closest_num3)

    closest_result = min(close1, close2, close3)
    if closest_result == close1:
        next_channel = str(closest_num1)
        print(min(closest_result + len(next_channel), abs(100 - int(target_channel))))
    elif closest_result == close2:
        next_channel = str(closest_num2)
        print(min(closest_result + len(next_channel), abs(100 - int(target_channel))))
    elif closest_result == close3:
        next_channel = str(closest_num3)
        print(min(closest_result + len(next_channel), abs(100 - int(target_channel))))


