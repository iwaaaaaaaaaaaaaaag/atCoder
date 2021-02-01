H, W = (int(x) for x in input().split())

blocks = []
min_value = 999
for i in range(H):
    blocks.append(list(map(int, input().split())))
    min_value = min(min_value, min(blocks[i]))

minus_sum = 0
for i in range(H):
    for j in range(W):
        if blocks[i][j] != min_value:
            minus_sum += blocks[i][j] - min_value

print(minus_sum)  
