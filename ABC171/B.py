
N,K = map(int,input().split())
lists = list(map(int,input().split()))
lists.sort()
ans = 0
for _ in range(K):
    ans += lists.pop(0)
print(ans)
