from sys import stdin

N, max_weights = map(int, stdin.readline().split())
items = [tuple(map(int, stdin.readline().split())) for _ in range(N)]
items.sort()
dp = [[0]*N for _ in range(max_weights+1)]
for weights in range(1, max_weights+1):
    for n in range(N):
        w, v = items[n]
        if weights < w:
            if n == 0:
                dp[weights][n] = 0
            else:
                dp[weights][n] = dp[weights][n-1]
            continue
        if n == 0:
            dp[weights][n] = v
            continue
        dp[weights][n] = max(dp[weights][n-1], dp[weights-w][n-1] + v)

print(dp[max_weights][N-1])

