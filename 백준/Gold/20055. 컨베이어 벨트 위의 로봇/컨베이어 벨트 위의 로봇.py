from sys import stdin

N, K = map(int, stdin.readline().split())
durability = list(map(int, stdin.readline().split()))
is_on_robot = [0]*(2*N)

time = 0
cnt = 0
while 1:
    # 벨트, 로봇 한 칸 회전
    last_is_on_robot = is_on_robot[2*N-1]
    last_durability = durability[2*N-1]
    for i in range(2*N-1, 0, -1):
        durability[i] = durability[i-1]
        is_on_robot[i] = is_on_robot[i-1]
        # 로봇 내리는 위치에 로봇 있으면 내리기
        if i == N-1 and is_on_robot[N-1] == 1:
            is_on_robot[N-1] = 0 
    is_on_robot[0] = last_is_on_robot 
    durability[0] = last_durability 
    
    # 로봇 가능하면 이동
    for i in range(N-1, 0, -1):    
        if durability[i] >= 1 and is_on_robot[i] == 0 and is_on_robot[i-1] == 1:
            if i == N-1:
                is_on_robot[i] = 0
            else:
                is_on_robot[i] = 1
            is_on_robot[i-1] = 0
            durability[i] -= 1
            if durability[i] == 0:
                cnt += 1
       
   
    # 로봇 올리는 위치에 올림
    if durability [0] >= 1 and is_on_robot[0] == 0:
        durability[0] -= 1
        is_on_robot[0] = 1
        if durability[0] == 0:
            cnt += 1
    
    time += 1
    
    if cnt >= K:
        break
    
        
print(time)