S = input()
ans = 0
for i in range(len(S)): # start
    cnt = 0
    for j in range(i,len(S)): # end
        if S[j] in ['A','C','G','T']:
            cnt += 1
        else:
            cnt = float('inf') * -1
        ans = max(ans,cnt)
print(ans)