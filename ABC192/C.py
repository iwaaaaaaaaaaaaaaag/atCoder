N, K = map(int,input().split())
# N = 1756928475
# K = 100000

ans = N
for i in range(K):
    n = list(map(str,str(ans)))
    
    n.sort(reverse=True)
    max_value = int(''.join(n))
    n.sort()
    min_value = int(''.join(n))
    
    ans = max_value - min_value

    if ans == 0:
        break

print(ans)
    