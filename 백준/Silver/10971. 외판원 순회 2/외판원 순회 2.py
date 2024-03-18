def func(level):
    global min_sum_of_price
    if level == N-1:
        sum_of_price = 0
        i = 0
        move_impossible = 0
        for j in path:
            if board[i][j] == 0:    # 도시 간 이동이 불가능한 경우
                move_impossible = 1
                break
            sum_of_price += board[i][j]
            i = j
        if move_impossible == 0:
            j = 0
            if board[i][j] == 0:    # 도시 간 이동이 불가능한 경우
                return
            else:
                sum_of_price += board[i][j]
                if sum_of_price < min_sum_of_price:
                    min_sum_of_price = sum_of_price
        return

    for i in range(1, N):
        if used[i] == 1:
            continue

        used[i] = 1
        path.append(i)
        func(level+1)
        used[i] = 0
        path.pop()


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
path = []
used = [0]*N
min_sum_of_price = 21e8
func(0)
print(min_sum_of_price)