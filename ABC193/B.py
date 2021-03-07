N = int(input())
lists = [list(map(int,input().split())) for _ in range(N)]
# 最小の金額
max_value = 10 ** 9 + 1
ans = max_value
for i in range(N):
    a,p,x = lists[i][0],lists[i][1],lists[i][2]
    if x > a:
        ans = min(ans,p)
if ans == max_value:
    ans = -1
print(ans)