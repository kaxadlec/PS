from sys import stdin

N = int(stdin.readline())
nums = [int(stdin.readline()) for _ in range(N)]
if nums.count(1) > nums.count(0):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")

