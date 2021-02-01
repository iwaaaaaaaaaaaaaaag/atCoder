L = int(input())
#nCr
r = 11
r_kaizyou = 1
for i in range(1,L - r):
    r_kaizyou *= i 
n_kaizyou = 1
for i in range(r + 1,L):
    n_kaizyou *= i 

print(n_kaizyou//r_kaizyou)
