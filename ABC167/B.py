A,B,C,K = map(int,input().split())
ans = 0

ans += min(K,A)
K -= A
if K<=0:
    print(ans)
    exit()

K -= B
if K<=0:
    print(ans)
    exit()

ans -= min(K,C)
print(ans)

    
