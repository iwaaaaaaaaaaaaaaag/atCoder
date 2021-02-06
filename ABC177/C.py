N = int(input())
A_list = list(map(int,input().split()))

ans = 0
A_sum = sum(A_list)
for i in range(N):
   A_sum -= A_list[i]
   ans += A_list[i] * A_sum
print(ans%((10 ** 9) + 7))