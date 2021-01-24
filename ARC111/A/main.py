import math
tmp = list(map(int, input().split()))
N = tmp[0]
M = tmp[1]
output = math.floor(pow(10,N)/M % M)
print(output)