from sys import stdin

N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
set_arr = list(set(arr))
set_arr.sort()
pos_dict = {}
for i in range(len(set_arr)):
    if pos_dict.get(set_arr[i]) is None:
        pos_dict[set_arr[i]] = i
    
for i in range(N):
    print(pos_dict[arr[i]], end=' ')
