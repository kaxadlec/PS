from sys import stdin

while 1:
    word = stdin.readline().rstrip()
    if word == '0':
        break
    reversed_word = word[-1::-1]
    if word == reversed_word:
        print('yes')
    else:
        print('no')
