from sys import stdin

N, new_score, P = map(int, stdin.readline().split())
if N > 0:
    score_list = list(map(int, stdin.readline().split())) + [-1] * (P-N)
    rank_list = [0] * P
    rank_list[0] = 1
    new_rank = 0
    # print(score_list)
    duplicate_cnt = 0
    for i in range(1, P):
        if score_list[i-1] > score_list[i]:
            rank_list[i] = rank_list[i-1] + duplicate_cnt + 1
            duplicate_cnt = 0
        elif score_list[i-1] == score_list[i]:
            rank_list[i] = rank_list[i-1]
            duplicate_cnt += 1
    # print(rank_list)

    for i in range(P-1, -1, -1):
        if new_score > score_list[i]:
            if i == 0:
                new_rank = 1
            continue
        elif new_score == score_list[i]:
            if i == P-1:
                new_rank = -1
            else:
                new_rank = rank_list[i]
            break
        else:  # new_score < score_list[i]
            if i == P-1:
                new_rank = -1
            else:
                new_rank = rank_list[i+1]
            break

else:   # N == 0
    if P == 0:
        new_rank = -1
    else:
        new_rank = 1

print(new_rank)