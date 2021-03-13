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


'''
# 1番目のカード
for j in range(limit + 1):
    if num_list[0] <= j:
        dp_table[0][j] = list[0] # 1番目のカードを追加

# 2番目以降のカード
for i in range(list_len):
    for j in range(limit + 1):
        tmp_not_choice = dp_table[i-1][j]
        if num_list[i] > j: # コスト不足のとき
            dp_table[i][j] = tmp_not_choice 
        else:
            tmp_choice = dp_table[i-1][j - num_list[i]] + num_list[i]
            dp_table[i][j] = max(tmp_choice,tmp_not_choice)


return dp_table[list_len - 1][limit]

'''