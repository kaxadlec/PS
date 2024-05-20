N = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
print(sum(scores)/max_score*100/len(scores))
