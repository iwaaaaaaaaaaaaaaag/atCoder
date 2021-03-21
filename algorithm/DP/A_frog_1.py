N = int(input())
h_list = list(map(int,input().split()))

# dpテーブルの作成
dp_table = list([0] * (N))

for i in range(N):
    if i == 0:
        dp_table[i] = 0
    elif i == 1:
        dp_table[i] = dp_table[i - 1] + abs(h_list[i] - h_list[i - 1])
    else:
        dp_table[i] = min(dp_table[i - 1] + abs(h_list[i] - h_list[i - 1]),
        dp_table[i - 2] + abs(h_list[i] - h_list[i - 2]))
print(dp_table[-1])
