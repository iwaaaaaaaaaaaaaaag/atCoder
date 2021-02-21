X, K, D = map(int,input().split())

ans = 0
abs_X = abs(X)
cnt = abs_X // D

if cnt >= K:
    ans = abs_X - K * D
else:
    if (K - cnt)%2 == 0:
        ans = abs_X - cnt * D
    else:
        ans = abs(abs_X - (cnt + 1 )* D)
print(ans)