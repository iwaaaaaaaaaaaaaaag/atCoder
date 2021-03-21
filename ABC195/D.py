N,M,Q = map(int,input().split())

w = []
v = []
max_weight = 0
for i in range(N):
    x,y = map(int,input().split())
    w.append(x)
    v.append(y)
    max_weight += x
X_list = list(map(int,input().split()))
query_list = [map(int,input().split()) for _ in range(Q)]

dp = [[0]*(max_weight+1) for j in range(N+1)] # DPテーブルの作成


# dpテーブルの作成
# 縦→荷物の数
# 横→重さ
# セルの合計値→荷物に詰めた価値
for query in query_list:
    query = set(query)
    for i in range(N):
        for j in range(max_weight+1):
            if j < w[i]: # 選ばない時
                dp[i+1][j] = dp[i][j]
            else: # 選ぶ時
                dp[i+1][j] = max(dp[i][j],dp[i][j-w[i]]+v[i])

print(*dp,sep='\n')
