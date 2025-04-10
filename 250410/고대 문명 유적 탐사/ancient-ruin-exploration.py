from sys import stdin
from collections import deque
import heapq

'''
5 * 5 격자
1~7 배치

1. 탐사진행
- 5 * 5 격자 내에서 3 * 3 격자 선택
- 선택한 3 * 3 격자 회전
- 선택한 3 * 3 격자 회전 방향은 시계방향으로 90도, 180도, 270도 중 하나 
- 선택한 3 * 3 격자 회전은 항상 진행
[회전목표] 가능한 회전 방법 중에
1-1. 유물 1차 획득 가치를 최대화할 수 있는 방법 선택
1-2. 1-1 방법이 여러가지면, 회전한 각도가 가장 작은 방법 선택
1-3. 1-2 방법이 여러가지면, 회전 중심 좌표의 열이 가장 작은 방법 선택
1-4. 회전 중심 좌표 열이 같다면, 행이 가장 작은 방법 선택
'''

'''
2. 유물 획득
[유물 1차 획득]
5 * 5 격자에서,
- 상하좌우로 인접한 같은 종류의 "유물 조각"(같은 숫자)이 3개 이상 연결되면, 조각이 모여 "유물"이 되고 사라짐.
- 유물의 가치는 모인 조각의 개수와 같음
- 유적지에서 유물이 사라지면, 유물조각 칸 빈칸 되어버림.
[유적의 벽면]
- 유적의 벽면에 새로 생겨나는 조각에 대한 정보 있음
- 조각이 사라진 위치에는 유적의 벽면에 적혀있는 순서대로 새로운 조각 생겨남
[새로운 조각 생성 방법]
2-1. 열번호가 작은 순
2-2. 열번호가 같다면, 행번호가 큰 순
* 벽면의 숫자는 충분히 많이 적혀 있어 생겨날 조각 수가 부족한 경우는 없음.
* 유적의 벽면에 써 있는 숫자를 사용한 이후에는 다시 사용할 수 없음. 이후부터는 남은 숫자부터 순서대로 사용.
[유물 연쇄 획득]
- 새로운 유물 조각이 생겨난 이후에도, 조각들이 3개 이상 연결될 수 있음.
- 똑같은 방식으로 조각이 모여 유물이 되고 사라짐.
- 사라진 위치에는 또다시 새로운 조각 생겨남.
- 더 이상 조각이 3개 이상 연결되지 않아 유물이 될 수 없을 때까지 반복
'''

'''
3. 탐사 반복
- 탐사 진행 ~ 유물 연쇄 획득의 과정까지를 1턴으로 생각.
- 총 k번의 턴에 걸쳐 진행.
- 각 턴마다 획득한 유물의 가치의 총합하는 프로그램 작성해야함.
- 아직 k번의 턴을 진행하지 못했지만, 탐사진행 과정에서 어떠한 방식으로든 유물을 획득할 수 없었다면 모든 탐사는 즉시 종료.
- 이 경우에는 얻을 수 있는 유물이 존재하지 않으므로, 종료되는 턴에는 아무 값도 출력하지 말 것.
'''

'''
초기에 주어지는 유적지에는 탐사 진행 이전에 유물이 발견되지는 않음.
첫번째 턴에서 탐사를 진행한 이후에는 항상 유물이 발견됨을 가정.
'''

def rotate(center_coordinate, angle_idx):
    copy_board = [row[:] for row in board]
    ci, cj = center_coordinate
    for x in range(8):
        di, dj = directions[x]
        pre_di, pre_dj = directions[x-((angle_idx+1)*2)]
        ni, nj = ci + di, cj + dj
        pre_ni, pre_nj = ci + pre_di, cj + pre_dj
        copy_board[ni][nj] = board[pre_ni][pre_nj]
    return copy_board

def calculate_value(cur_board):
    visited = [[False]*5 for _ in range(5)]
    result = 0
    for x in range(5):
        for y in range(5):
            if visited[x][y]:
                continue
            base_num = cur_board[x][y]
            visited[x][y] = True
            # bfs
            queue = deque()
            queue.append((x, y))
            cnt = 1
            while queue:
                i, j = queue.popleft()
                for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    ni, nj = i + di, j + dj
                    if not (0 <= ni < 5 and 0 <= nj < 5):
                        continue
                    if visited[ni][nj]:
                        continue
                    if cur_board[ni][nj] == base_num:
                        queue.append((ni, nj))
                        visited[ni][nj] = True
                        cnt += 1
            if cnt >= 3:
                result += cnt
    return result


def eliminate_path(cur_board, cur_flag):
    visited = [[False]*5 for _ in range(5)]
    result = 0
    for x in range(5):
        for y in range(5):
            if visited[x][y]:
                continue
            base_num = cur_board[x][y]
            visited[x][y] = True
            # bfs
            queue = deque()
            queue.append((x, y))
            cnt = 1
            connected = [(x, y)]
            while queue:
                i, j = queue.popleft()
                for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    ni, nj = i + di, j + dj
                    if not (0 <= ni < 5 and 0 <= nj < 5):
                        continue
                    if visited[ni][nj]:
                        continue
                    if cur_board[ni][nj] == base_num:
                        queue.append((ni, nj))
                        visited[ni][nj] = True
                        cnt += 1
                        connected.append((ni, nj))
            if cnt >= 3:
                result += cnt
                cur_flag = True
                for x, y in connected:
                    cur_board[x][y] = None

    return cur_board, cur_flag, result

def create_piece(cur_board):
    global walls_idx
    # [새로운 조각 생성 방법]
    # 2-1. 열번호가 작은 순
    # 2-2. 열번호가 같다면, 행번호가 큰 순
    for j in range(5):
        for i in range(4, -1, -1):
            if cur_board[i][j] is None:
                cur_board[i][j] = walls[walls_idx]
                walls_idx += 1
    return cur_board


K, M = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(5)]
walls = list(map(int, stdin.readline().split()))
walls_idx = 0
# 8개 방향
directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
# 회전 중심 좌표들
rotate_center_coordinates = [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
# 각 턴마다 획득한 유물의 가치 배열
ans = []

for _ in range(K):
    pq = []
    # 1. 탐사 진행 - 회전 중심 좌표, 회전 각도 선정
    for coordinate in rotate_center_coordinates:
        for idx in range(3):
            rotate_board = rotate(coordinate, idx)
            rotate_value = calculate_value(rotate_board)
            # 유물 1차 획득 가치, 회전한 각도가 가장 작은 방법, 회전 중심 좌표의 열이 가장 작은 방법, 행이 가장 작은 방법
            heapq.heappush(pq, (-rotate_value, idx, coordinate[1], coordinate[0]))

    # 2
    # 회전 중심 좌표 선정 후 작업
    value, rotate_idx, cj, ci = heapq.heappop(pq)
    value = -1 * value
    # 회전
    rotate_board = rotate((ci, cj), rotate_idx)
    # print("rotate_board", rotate_board)
    # 유물 1차 획득 단계
    # 유물 사라지게 하기
    eliminated_board, eliminated_flag, cur_turn_value = eliminate_path(rotate_board, False)
    # print("eliminated_board", eliminated_board, "eliminated_flag", eliminated_flag, "cur_turn_value", cur_turn_value)
    if not eliminated_flag: # 아직 k번의 턴을 진행하지 못했지만, 탐사진행 과정에서 어떠한 방식으로든 유물을 획득할 수 없었다면 모든 탐사는 즉시 종료.
        break
    # 새로운 조각 생성
    created_board = create_piece(eliminated_board)
    # print("created_board", created_board)

    chain_board = [row[:] for row in created_board]
    # 유물 연쇄 획득
    while eliminated_flag is True:
        chain_board, eliminated_flag, chain_value = eliminate_path(chain_board, False)
        # print("chain_board", chain_board, "eliminated_flag", eliminated_flag, "chain_value", chain_value)
        chain_created_board = create_piece(chain_board)
        # print("chain_created_board", chain_created_board)
        cur_turn_value += chain_value
    board = [row[:] for row in chain_created_board]
    ans.append(cur_turn_value)

print(*ans)