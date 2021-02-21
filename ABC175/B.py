N = int(input())
L_list = list(map(int,input().split()))

#3角形の条件
#a+b>c かつ b+c>a かつ c+a>b
ans = 0
for a in range(N - 2):
    for b in range(a,N - 1):
        for c in range(b,N):
            if (L_list[a] != L_list[b] and L_list[b] != L_list[c] and L_list[a] != L_list[c]) \
                and (L_list[a] + L_list[b] > L_list[c] and L_list[b] + L_list[c] > L_list[a] and L_list[c] + L_list[a] > L_list[b]):
                ans +=1
print(ans)
