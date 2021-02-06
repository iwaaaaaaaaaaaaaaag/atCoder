N = int(input())
saikoro = [list(map(int,input().split())) for _ in range(N)]

cnt = 0
for i in saikoro:
    if i[0] == i[1]:
       cnt += 1
    else:
        cnt = 0
    if cnt == 3:
        print('Yes')
        break
else:
    print('No')
