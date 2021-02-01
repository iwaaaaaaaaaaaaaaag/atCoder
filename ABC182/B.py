N = int(input())
A_list = list(map(int, input().split()))

gcd = 0
index = A_list[0]
for i in range(2, max(A_list)+1):
    gcd_temp = 0
    for j in A_list:
        if j % i == 0:
            gcd_temp += 1
    if gcd_temp > gcd:
        gcd = gcd_temp
        index = i   
print(index)