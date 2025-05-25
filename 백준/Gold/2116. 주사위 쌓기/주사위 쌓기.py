from sys import stdin

N = int(stdin.readline())
dices = [list(map(int, stdin.readline().split())) for _ in range(N)]
first_dice = dices[0]
top_down_dict = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
idx_set = {0, 1, 2, 3, 4, 5}

ans = 0
for i in range(6): # 첫번째 주사위 top을 바꾸면서 생각
    top_idx, down_idx = i, top_down_dict[i]
    first_top_num, down_top_num = first_dice[top_idx], first_dice[down_idx]
    remove_idx_set = {top_idx, down_idx}
    side_idx_set = idx_set - remove_idx_set

    result = 0
    first_max = 0
    for side_idx in side_idx_set:
        first_max = max(first_max, first_dice[side_idx])
    result += first_max

    top_num = first_top_num
    for x in range(1, N): # 첫번째 주사위 이후 주사위들 계산
        dice = dices[x]  # 주사위 정보
        for y in range(6): # 주사위 여섯면 탐색
            if dice[y] == top_num:  # 주사위의 밑면 숫자가 전 주사위의 윗면 숫자와 같으면
                down_idx = y    # 주사위 밑면 인덱스 저장
                top_idx = top_down_dict[down_idx] # 주사위 윗면 인덱스 저장
                top_num = dice[top_idx] # 주사위 top_num
                break
        remove_idx_set = {top_idx, down_idx}
        side_idx_set = idx_set - remove_idx_set

        side_max_num = 0
        for side_idx in side_idx_set:
            side_max_num = max(side_max_num, dice[side_idx])
        result += side_max_num

    ans = max(ans, result)

print(ans)
