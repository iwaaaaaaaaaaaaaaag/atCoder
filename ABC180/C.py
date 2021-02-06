import math

N = int(input())

ans=[]
for i in range(1,int(math.sqrt(N)) + 1):
    if N%i==0:
        ans.append(i)
        ans.append(N//i)

ans = sorted(set(ans))
[print(x) for x in ans]
