lists = [2,4,7,9,8,10]
max_value = 20

# dpテーブルの作成
dp_table = [list([0] * (max_value + 1)) for _ in range(len(lists))]
print(dp_table)

# 1番目
for j in range(len(dp_table[0])):
    if j >= lists[0]:
        dp_table[0][j] = lists[0] 
print(dp_table)

# 2番目以降
for i in range(1,len(lists)):
    for j in range(len(dp_table[0])):
        if j < lists[i]: # コストが不足している時
            dp_table[i][j] = dp_table[i -1][j] # 一個前の重さを入れる
        else:
            dp_table[i][j] = max(dp_table[i -1][j],dp_table[i - 1][j - lists[i]] + lists[i])

print(*dp_table, sep='\n')

