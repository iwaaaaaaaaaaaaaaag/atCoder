S = list(map(str,input()))
T = list(map(str,input()))
ans = 0
for i in range(len(S)):
    if S[i] != T[i]:
        ans += 1
print(ans)