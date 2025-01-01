from sys import stdin

word = stdin.readline().strip()
word_dict = dict()
for st in word:
    st = st.upper()
    if word_dict.get(st) is None:
        word_dict[st] = 1
    else:
        word_dict[st] += 1

result_word = ''
max_len = -1
for word in word_dict:
    if word_dict[word] > max_len:
        max_len = word_dict[word]
        result_word = word
    elif word_dict[word] == max_len:
        result_word = '?'

print(result_word)