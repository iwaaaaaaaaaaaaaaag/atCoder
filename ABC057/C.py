import math
N = int(input())
ans = len(str(N))
for i in range(1,round(math.sqrt(N)) + 1):
    if N%i == 0:
        A = i
        B = N//i
        tmp = max(len(str(A)),len(str(B)))
        ans = min(ans,tmp)
print(ans)