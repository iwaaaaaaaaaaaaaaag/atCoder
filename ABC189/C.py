N = int(input())
A_list = list(map(int, input().split()))

sum = 0
for start in range(N):
    x = A_list[start]
    for i in range(start, N):
        x = min(x, A_list[i])
        sum = max(sum, x * (i + 1 - start))
print(sum)
