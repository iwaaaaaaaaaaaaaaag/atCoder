N, M = map(int,input().split())
A_list = [list(map(int,input().split())) for _ in range(N)]
ans = 0
for i in range(M-1):
    for j in range(i+ 1,M):
        tmp = 0
        for k in range(N):
            tmp += max(A_list[k][i],A_list[k][j])    
        ans = max(ans,tmp)
print(ans)
