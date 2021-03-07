N = int(input())
A_list = list(map(int,input().split()))

X2 = 0
X = 0
cnt = 1
ans = 0
for i in range(N-2,-1,-1):
    X2 += A_list[i+1]**2
    X += A_list[i+1]

    ans += X2 -2*A_list[i]*X + cnt*A_list[i]**2
    cnt +=1
print(ans)
 