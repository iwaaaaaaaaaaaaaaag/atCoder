N = int(input())

A_list = list(map(int,input().split()))

diff = 0
ans = 0
for i in range(1,N):
    diff = A_list[i - 1] - A_list[i]
    if diff > 0:
        ans += diff
        A_list[i] = A_list[i - 1]
print(ans)