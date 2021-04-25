N,M = map(int,input().split())
A_list = list(map(int,input().split()))
B_list = list(map(int,input().split()))
ans = []
for i in range(N):
    if A_list[i] not in B_list:
         ans.append(A_list[i])

for i in range(M):
    if B_list[i] not in A_list:
         ans.append(B_list[i])

ans.sort()
print(*ans)