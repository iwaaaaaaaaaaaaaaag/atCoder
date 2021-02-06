a,b,c,d = map(int,input().split())
# a<=x<=b
# c<=y<=d
ans = a * c
ans = max(ans,a * d)
ans = max(ans,b * c)
ans = max(ans,b * d)
print(ans)