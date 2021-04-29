# 1 ≤ m ≤ 200
# 1 ≤ n ≤ 1000
# x座標とy座標はすべて0以上1000000以下

m = int(input())
target_star = [list(map(int,input().split())) for _ in range(m)]
n = int(input())
all_star = [list(map(int,input().split())) for _ in range(n)]

for j in range(n):
    dx,dy = all_star[j][0] - target_star[0][0] ,all_star[j][1] - target_star[0][1]
    cnt = 1
    for i in range(1,m):
        move_x, move_y = target_star[i][0] + dx, target_star[i][1] + dy
        if [move_x, move_y] in all_star:
            cnt += 1
    if cnt == m:
        print(dx,dy)
        break