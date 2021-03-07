X = int(input())
M = int(input())

n = list(map(str,str(X)))
d = int(max(n)) 

#Xが一桁の場合
if len(n) == 1:
    if X <= M:
        print(1)
    else:
        print(0)
    exit()

ok = d          #left
ng = M + 1      #right 最大は10の時で、1*M^1となる

while ng - ok > 1: #ng = ok + 1の場合になるまで繰り返す

    mid = (ok + ng) // 2
    value = 0
    for i in range(len(n)):
        value += int(n[-(i+1)]) * mid**i
    
    if value <= M:
        ok = mid
    else:
        ng = mid

print(ok - d)
