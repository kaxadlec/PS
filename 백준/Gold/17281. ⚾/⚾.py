from sys import stdin
from collections import deque
from itertools import permutations

N = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]

arr = [1, 2, 3, 4, 5, 6, 7, 8]
max_score = 0

for perm in permutations(arr, 8):
    batter_order = list(perm[:3]) + [0] + list(perm[3:])  # 4번 타순에 0번 타자를 고정
    batter_order = deque(batter_order)  # 등번호가 나열되어있는 타순 (인덱스가 타순번호)
    score = 0
    for inning in range(N):
        # print(inning + 1, '이닝 시작')
        out_count = 0
        bases = [0, 0, 0]   # 1루, 2루, 3루
        while out_count < 3:
            order = batter_order.popleft()  # 어떤 등번호의 선수 등장 (선수이름이 번호라고 생각)
            batter_order.append(order)  # 타순 나왔으니 다시 마지막 타순으로   
            plate_appearance = board[inning][order]    # 타석에서 어떤행동을 할까
            
            if plate_appearance == 0:   # 아웃
                out_count += 1
            elif plate_appearance == 1:     # 안타
                score += bases[2]
                bases = [1] + bases[:2]
            elif plate_appearance == 2:     # 2루타 치면
                score += bases[2] + bases[1]
                bases = [0, 1] + bases[:1]
            elif plate_appearance == 3:     # 3루타 치면
                score += bases[2] + bases[1] + bases[0]
                bases = [0, 0, 1]
            elif plate_appearance == 4:     # 홈런 치면
                score += bases[2] + bases[1] + bases[0] + 1
                bases = [0, 0, 0]
    max_score = max(max_score, score)
print(max_score)
