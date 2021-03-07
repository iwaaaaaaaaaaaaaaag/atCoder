N = 3
cond = []
for i in range(2 ** N):
    cond.append([0] * N)
    for j in range(N):
        if (i>>j)&1 == 1:
            cond[i][j] = 1
print(*cond)