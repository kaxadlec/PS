from sys import stdin

N = int(stdin.readline())
arr = [0] + [int(stdin.readline()) for _ in range(N)]
dp = [[0]*2 for _ in range(N+1)]
'''
테이블 정의
2차원 dp 배열을 만들어, dp 배열의 각 요소의 
인덱스 0 : 연속되지않게 계단을 밟았을 경우 (바로 전 계단 안 밟음)
인덱스 1 : 연속되게 계단을 밟았을 경우 (바로 전 계단 밟음)
'''

# 초기값 설정
dp[0][0], dp[0][1] = 0, 0
dp[1][0], dp[1][1] = arr[1], arr[1]

for i in range(2, N+1):
    dp[i][0] = max(dp[i-2][0] + arr[i], dp[i-2][1] + arr[i])
    dp[i][1] = dp[i-1][0] + arr[i]

print(max(dp[N]))