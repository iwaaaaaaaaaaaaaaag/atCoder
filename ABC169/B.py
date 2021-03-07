N=int(input())
lists = list(map(int,input().split()))
ans = 1
if 0 in lists:
    print(0)
    exit()

for i in range(N):
    ans *= lists[i]
    if ans > 10**18:
        print(-1)
        break
else:
    print(ans)