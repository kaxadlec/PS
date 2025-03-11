from sys import stdin

score_dict = dict()
N = int(stdin.readline())
alphabet = [stdin.readline().rstrip() for _ in range(N)]
for alpha in alphabet:
    # print(alpha)
    len_alpha = len(alpha)
    for idx in range(len_alpha):
        num = len_alpha - idx
        eng = alpha[idx]
        if score_dict.get(eng) is None:
            score_dict[eng] = 0
        score_dict[eng] += (10**num)

sorted_score_dict = sorted(score_dict.items(), key=lambda x:x[1], reverse=True)
# print(sorted_score_dict)
alpha_num_matching = dict()

for i in range(len(sorted_score_dict)):
    alpha_num_matching[sorted_score_dict[i][0]] = 9 - i

# print(alpha_num_matching)
result = 0
for alpha in alphabet:
    # print(alpha)
    for i in range(len(alpha)):
        digit = len(alpha) - i
        result += alpha_num_matching[alpha[i]] * (10**(digit-1))

    
print(result)


