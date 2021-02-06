import itertools
import math

N = int(input())
zahyou = [list(map(int,input().split())) for _ in range(N)]

p = list(itertools.permutations(list(range(N)), N))
kyori = 0
for i in range(len(p)):
    for j in range(N - 1):

        x = zahyou[p[i][j + 1]][0] - zahyou[p[i][j]][0]
        y = zahyou[p[i][j + 1]][1] - zahyou[p[i][j]][1]
        kyori += math.sqrt(x**2 + y**2)

print(kyori/len(p))