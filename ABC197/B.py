H,W,X,Y =list(map(int,input().split()))
S = [list(map(str,input())) for _ in range(H)]

ans = 1
# 右
i = Y 
while i <= W - 1:
    if S[X - 1][i] == '.':
        ans += 1
        i += 1    
    else:
        break

# 左
i = Y - 2 
while i >= 0:
    if S[X - 1][i] == '.':
        ans += 1
        i -= 1    
    else:
        break

# 下
i = X 
while i <= H - 1:
    if S[i][Y - 1] == '.':
        ans += 1
        i += 1    
    else:
        break

# 上
i = X - 2 
while i >= 0:
    if S[i][Y - 1] == '.':
        ans += 1
        i -= 1    
    else:
        break

print(ans)