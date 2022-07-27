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
    check_num = fill_num - ((arr_size - 1) * 3)
    if check_num == 0:
        step += 1
    if direction == 'right':
        for col in range(step, arr_size - 1 - step, 1):
            fill_num += 1
            arr[row][col] = fill_num
        direction = 'down'
        col += 1
        continue
    if direction == 'down':
        for row in range(step, arr_size - 1 - step, 1):
            fill_num += 1
            arr[row][col] = fill_num
        direction = 'left'
        row += 1
        continue
    if direction == 'left':
        for col in range(arr_size - 1 - step, step, -1):
            fill_num += 1
            arr[row][col] = fill_num
        direction = 'up'
        col -= 1
        continue
    if direction == 'up':
        for row in range(arr_size - 1 - step, step + 1, -1):
            fill_num += 1
            arr[row][col] = fill_num
        direction = 'right'
        row -= 1
        continue


# print(arr)
for row in range(len(arr)):
    for col in range(len(arr[0])):
        print(arr[row][col], end=' ')
    print()
print('************')


