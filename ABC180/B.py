import math

N = int(input()) 
x_list = list(map(int,input().split()))

manhattan = 0
euclid = 0
chebyChef = 0

for x in x_list:
    tmp = abs(x)
    manhattan += tmp
    euclid += tmp ** 2
    chebyChef = max(chebyChef,tmp)

print(manhattan)
print(math.sqrt(euclid))
print(chebyChef)
