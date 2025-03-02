from sys import stdin 

n, m = map(int, stdin.readline().split())
points = [tuple(map(int, stdin.readline().split())) for _ in range(m)]

# 게임 시작시 0 부터 5까지의 고유번호가 부여된 평면 상의 점 6개가 주어짐
# 이 중 어느 세 점도 일직선 위에 놓이지 않음
# c에 속한 임의의 선분의 한 끝점에서 출발하여 모든 선분을 한 번씩만 지나서 출발점으로 되돌아올 수 있다.


def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    
    return parents[x]
    
    
def union(x, y):
    root_x = find(x)
    root_y = find(y)
    
    if root_x == root_y:
        return True
        
    if ranks[root_x] < ranks[root_y]:
        parents[root_x] = root_y
        
    elif ranks[root_x] > ranks[root_y]:
        parents[root_y] = root_x
        
    else:
        parents[root_y] = root_x
        ranks[root_x] += 1
    
    return False

parents = [i for i in range(n)]
ranks = [0] * (n)

for i in range(m):
    x, y = points[i]
    result = union(x, y)
    if result == True:
        print(i+1)
        break

if result == False:
    print(0)

 
    
    
    