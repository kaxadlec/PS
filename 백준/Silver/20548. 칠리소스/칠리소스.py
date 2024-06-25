from sys import stdin

c = int(stdin.readline())
step = 0

power = 0
while 7 ** power <= c:
    power += 1
power -= 1

while power >= 0:
    if 7**power*2 <= c:
        step += (3**power)*2
        c -= 7**power*2
        power -= 1
    elif 7**power*1 <= c:
        step += (3**power)
        c -= 7**power*1
        power -= 1
    else:
        power -= 1

print(step)

