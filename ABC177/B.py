S = str(input())
T = str(input())

cnt = len(T)
for i in range(len(S) - len(T) + 1):
    tmp = 0
    for j in range(0,len(T)):
        if S[i + j] != T[j]:
            tmp += 1
    cnt = min(cnt,tmp)
print(cnt)

    