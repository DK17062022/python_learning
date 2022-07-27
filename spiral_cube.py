arr_size = int(input())

# fill array by zeros
arr = [[0] * arr_size for _ in range(arr_size)]

print('*** initial array ***')
for row in range(len(arr)):
    for col in range(len(arr[0])):
        print(arr[row][col], end=' ')
    print()
print('************')

# fill arr
direction = 'right'
fill_num = 0
step = 0
row = 0
col = 0
max_num = arr_size * arr_size
while fill_num <= max_num:
    if fill_num == max_num:
        break
    if direction == 'right':
        while col < arr_size:
            if arr[row][col] != 0:
                direction = 'down'
                row += 1
                col -= 1
                break
            elif col == arr_size - 1:
                direction = 'down'
                break
            elif arr[row][col] == 0:
                fill_num += 1
                arr[row][col] = fill_num
                col += 1

    if direction == 'down':
        while row < arr_size:
            if arr[row][col] != 0:
                direction = 'left'
                row -= 1
                col -= 1
                break
            elif row == arr_size - 1:
                direction = 'left'
                break
            elif arr[row][col] == 0:
                fill_num += 1
                arr[row][col] = fill_num
                row += 1

    if direction == 'left':
        while col >= 0:
            if arr[row][col] != 0:
                direction = 'up'
                row -= 1
                col += 1
                break
            elif col == 0:
                direction = 'up'
                break
            elif arr[row][col] == 0:
                fill_num += 1
                arr[row][col] = fill_num
                col -= 1

    if direction == 'up':
        while row >= 0:
            if arr[row][col] != 0:
                direction = 'right'
                row += 1
                col += 1
                break
            elif row == 0:
                direction = 'right'
                break
            elif arr[row][col] == 0:
                fill_num += 1
                arr[row][col] = fill_num
                row -= 1

# print(arr)
for row in range(len(arr)):
    for col in range(len(arr[0])):
        print(arr[row][col], end=' ')
    print()
print('************')


