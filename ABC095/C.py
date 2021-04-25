A,B,C,X,Y = map(int,input().split())

ans = C*max(X,Y)*2

for i in range(0,max(X,Y)*2+1,2):
    tmp = A*X + B*Y + C*i
    ans = min(ans,tmp)
    X -= 1
    Y -= 1
    if X < 0 or Y < 0:
        break

print(ans)
