S = str(input())
cnt = 0
tmp = 0
for i in range(len(S)):
    if S[i] == "R":
        tmp += 1
        cnt = max(cnt,tmp)
    else:
        tmp = 0

print(cnt)