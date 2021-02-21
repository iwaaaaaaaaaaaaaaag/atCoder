import math
N,D = map(int,input().split())

x_y_list = [list(map(int,input().split())) for _ in range(N)]

ans= 0
for i in x_y_list:
    if math.sqrt(i[0]**2 + i[1]**2) <= D:
        ans +=1

print(ans)