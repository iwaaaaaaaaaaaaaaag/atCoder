N,K = map(int,input().split())
h_list = list(map(int,input().split()))

# dpテーブルの作成
dp_table = [float('inf')] * N
dp_table[0] = 0

for i in range(1,N):
    for k in range(1, K+1):
        if i < k:
            continue
        dp_table[i] = min(dp_table[i], dp_table[i - k] + abs(h_list[i] - h_list[i - k]))


print(dp_table[-1])