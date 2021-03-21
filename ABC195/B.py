import math
A,B,W = map(int,input().split())

W = W * 1000

weight = 0
min_count = 99999999
max_count = 0

for i in range(math.floor(W / B), math.ceil(W / A) + 1):
    weight = W / i
    if A <= weight and  weight <= B:
         min_count = min(min_count,i)
         max_count = max(max_count,i)

if min_count == 99999999 and max_count == 0: 
    print('UNSATISFIABLE')        
else:
    print(min_count,max_count)
