N = int(input())
lists = [list(map(int,input().split())) for _ in range(N)]

ans1 = 0

A_min = 999999999
A_index = -1
for i in range(N):
    if A_min > lists[i][0]:
        A_min = lists[i][0]
        A_index = i

B_min = 999999999
for i in range(N):
    if i != A_index:
        if B_min > lists[i][1]:
            B_min = lists[i][1]
    else:
        if B_min > lists[i][1] + A_min:
            B_min = lists[i][1] + A_min

        
ans1 = max(A_min,B_min)


B_min = 999999999
B_index = -1
for i in range(N):
    if B_min > lists[i][1]:
        B_min = lists[i][1]
        B_index = i

ans2 = 0
A_min = 999999999
for i in range(N):
    if i != B_index:
        if A_min > lists[i][0]:
            A_min = lists[i][0]
    else:
        if B_min > lists[i][0] + B_min:
            B_min = lists[i][0] + B_min

ans2 = max(A_min,B_min)

print(min(ans1,ans2))