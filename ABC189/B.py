# 少数を少数のまま扱わない
N, X = (int(x) for x in input().split())
X *= 100

for i in range(N):
    v, p = (int(x) for x in input().split())
    X -= (v * p)
    if X < 0:
        print(i + 1)
        break
else:
    print(-1)
