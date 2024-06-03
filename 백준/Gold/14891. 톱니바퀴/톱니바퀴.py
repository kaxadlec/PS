from sys import stdin
from collections import deque

first_cog = deque(stdin.readline().rstrip())
second_cog = deque(stdin.readline().rstrip())
third_cog = deque(stdin.readline().rstrip())
fourth_cog = deque(stdin.readline().rstrip())
turn_cnt = int(stdin.readline())

def first_cog_turn_clockwise():
    first_cog.appendleft(first_cog.pop())
def first_cog_turn_counter_clockwise():
    first_cog.append(first_cog.popleft())
def second_cog_turn_clockwise():
    second_cog.appendleft(second_cog.pop())
def second_cog_turn_counter_clockwise():
    second_cog.append(second_cog.popleft())
def third_cog_turn_clockwise():
    third_cog.appendleft(third_cog.pop())
def third_cog_turn_counter_clockwise():
    third_cog.append(third_cog.popleft())
def fourth_cog_turn_clockwise():
    fourth_cog.appendleft(fourth_cog.pop())
def fourth_cog_turn_counter_clockwise():
    fourth_cog.append(fourth_cog.popleft())


for _ in range(turn_cnt):
    which_cog_turn, dir = map(int, stdin.readline().split())
    if which_cog_turn == 1:
        if dir == 1: # 시계방향
            if first_cog[2] != second_cog[6]:
                if second_cog[2] != third_cog[6]:
                    if third_cog[2] != fourth_cog[6]:
                        fourth_cog_turn_counter_clockwise()
                    third_cog_turn_clockwise()
                second_cog_turn_counter_clockwise()
            first_cog_turn_clockwise()

        else:   # 반시계방향
            if first_cog[2] != second_cog[6]:
                if second_cog[2] != third_cog[6]:
                    if third_cog[2] != fourth_cog[6]:
                        fourth_cog_turn_clockwise()
                    third_cog_turn_counter_clockwise()
                second_cog_turn_clockwise()
            first_cog_turn_counter_clockwise()

    elif which_cog_turn == 2:
        if dir == 1:
            if second_cog[6] != first_cog[2]:
                first_cog_turn_counter_clockwise()
            if second_cog[2] != third_cog[6]:
                if third_cog[2] != fourth_cog[6]:
                    fourth_cog_turn_clockwise()
                third_cog_turn_counter_clockwise()
            second_cog_turn_clockwise()
        else:
            if second_cog[6] != first_cog[2]:
                first_cog_turn_clockwise()
            if second_cog[2] != third_cog[6]:
                if third_cog[2] != fourth_cog[6]:
                    fourth_cog_turn_counter_clockwise()
                third_cog_turn_clockwise()
            second_cog_turn_counter_clockwise()

    elif which_cog_turn == 3:
        if dir == 1:
            if third_cog[2] != fourth_cog[6]:
                fourth_cog_turn_counter_clockwise()
            if third_cog[6] != second_cog[2]:
                if second_cog[6] != first_cog[2]:
                    first_cog_turn_clockwise()
                second_cog_turn_counter_clockwise()
            third_cog_turn_clockwise()
        else:
            if third_cog[2] != fourth_cog[6]:
                fourth_cog_turn_clockwise()
            if third_cog[6] != second_cog[2]:
                if second_cog[6] != first_cog[2]:
                    first_cog_turn_counter_clockwise()
                second_cog_turn_clockwise()
            third_cog_turn_counter_clockwise()

    else:
        if dir == 1:
            if fourth_cog[6] != third_cog[2]:
                if third_cog[6] != second_cog[2]:
                    if second_cog[6] != first_cog[2]:
                        first_cog_turn_counter_clockwise()
                    second_cog_turn_clockwise()
                third_cog_turn_counter_clockwise()
            fourth_cog_turn_clockwise()
        else:
            if fourth_cog[6] != third_cog[2]:
                if third_cog[6] != second_cog[2]:
                    if second_cog[6] != first_cog[2]:
                        first_cog_turn_clockwise()
                    second_cog_turn_counter_clockwise()
                third_cog_turn_clockwise()
            fourth_cog_turn_counter_clockwise()


score = 0
if first_cog[0] == '1':
    score += 1
if second_cog[0] == '1':
    score += 2
if third_cog[0] == '1':
    score += 4
if fourth_cog[0] == '1':
    score += 8

print(score)
