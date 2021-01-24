def change(a, b, p):
    for c in range(K): #ゴールのx
        for d in range(K): #ゴールのy
            if (a + b) == (c + d) or (a - b) == (c - d) or (abs(a - c) + abs(b - d)) <= 3:
                if grid[c][d] == -1:
                    grid[c][d] = p + 1


K = 40
grid = [[-1] * K for _ in range(K)] #初期値設定 全てに-1する
grid[K // 2][K // 2] = 0 #原点を0にする


for i in range(10):
    for a in range(K): #スタートのx
        for b in range(K): #スタートのy
            if grid[a][b] == i:
                change(a, b, i)

for row in grid:
    print(*row)
