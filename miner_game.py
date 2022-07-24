print ('input field size (x y) and number of mines, use space as a separator: ', end='')
n, m, k = (int(i) for i in input().split())
a = [[0 for j in range(m)] for i in range(n)]
#print(a)
for i in range(k):
    print('enter mine #',i+1 ,' coordinates (x y): ',end='')
    row, col = (int(j) - 1 for j in input().split())
    a[row][col] = -1
#    print(a)
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            for di in range(-1,2):
                for dj in range(-1,2):
                    ai = i + di
                    aj = j + dj
                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
                        a[i][j] += 1
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            print('*', end='')
        elif a[i][j] == 0:
            print('.', end='')
        else:
            print(a[i][j], end='')
    print()




