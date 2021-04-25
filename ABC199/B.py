N = int(input())
A_list = list(map(int,input().split()))
B_list = list(map(int,input().split()))
ans_list = set(range(1,1001))
for i in range(N):
    ans_list &= set(range(A_list[i],B_list[i] + 1))

print(len(ans_list))