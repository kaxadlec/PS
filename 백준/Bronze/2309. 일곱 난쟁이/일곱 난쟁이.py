def dwarf(height_arr):
    sum_all_height = sum(height_arr)
    for i in range(9):
        for j in range(i + 1, 9):
            sum_height = sum_all_height - height_arr[i] - height_arr[j]
            if sum_height == 100:
                height_arr[i] = 101
                height_arr[j] = 101
                return height_arr


height_arr = []
for i in range(9):
    height = int(input())
    height_arr.append(height)

dwarf(height_arr)
height_arr.sort()
height_arr.pop()
height_arr.pop()

for i in height_arr:
    print(i)
