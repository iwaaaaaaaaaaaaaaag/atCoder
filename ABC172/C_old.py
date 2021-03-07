N,M,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ALL = A.copy()
ALL.extend(B)
ALL.sort()

ruiseki = []
#累積和
for i in range(len(ALL)):
    if i == 0:
        ruiseki.append(ALL[0])
    else:
        ruiseki.append(ALL[i] + ruiseki[i - 1])

#2分探索でKを超えないギリギリの値を探す
ok = 0 #左
ng = len(ruiseki) #右
while ok + 1 != ng:
    mid = (ok + ng)//2 #中間点
    if K < ruiseki[mid]:
        ng = mid
    elif K >= ruiseki[mid]:
        ok = mid
    print(ok,mid,ng)
print(ok + 1)
