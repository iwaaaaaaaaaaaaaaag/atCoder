N,M,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

#Aの累積和
A_ruiseki = [0]
for i in range(len(A)):
    A_ruiseki.append(A[i] + A_ruiseki[i])

B_ruiseki = [0]
for i in range(len(B)):
    B_ruiseki.append(B[i] + B_ruiseki[i])

ans = 0

for i in range(len(A_ruiseki)):
    #2分探索でKを超えないギリギリの値を探す
    ok = 0 #左
    ng = len(B) + 1 #右

    K_tmp = K - A_ruiseki[i]
    if K_tmp < 0:
        continue
    while ok + 1 != ng:
        mid = (ok + ng)//2 #中間点
        if K_tmp < B_ruiseki[mid]:
            ng = mid
        elif K_tmp >= B_ruiseki[mid]:
            ok = mid
    ans = max(ans,i + ok)
print(ans)


