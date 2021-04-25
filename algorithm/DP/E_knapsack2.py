N, W = map(int,input().split())
w_v  = [list(map(int,input().split())) for _ in range(N)]

# DPテーブル作成
DP = [[0]*(W + 1) for _ in range(N)]

for i in range(N):
    for j in range(1,V+1):
        if i == 0: # 初回
            if j >= w_v[i][0]:
                DP[i][j] = w_v[i][1]
        else:
            if j < w_v[i][0]:
                DP[i][j] = DP[i-1][j]
            else:
                DP[i][j] = max(w_v[i][1] + DP[i - 1][j - w_v[i][0]]
                            ,DP[i - 1][j])

print(DP[-1][-1])
