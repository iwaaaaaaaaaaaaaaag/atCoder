N = int(input())
Squares_list = [list(map(int,input().split())) for _ in range(N)]

ans = float('inf')
for i in range(N):
    start = Squares_list[i][0]
    for j in range(N):
        goal = Squares_list[j][1]
        dist = 0
        for k in range(N):
            dist += min(abs(start - Squares_list[k][0]) + abs(Squares_list[k][0] - Squares_list[k][1]) + abs(goal - Squares_list[k][1]),\
                        abs(start - Squares_list[k][1]) + abs(Squares_list[k][0] - Squares_list[k][1]) + abs(goal - Squares_list[k][0]))
        ans = min(ans,dist)

print(ans)