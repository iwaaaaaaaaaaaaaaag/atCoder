import math
N, M =  (int(x) for x in input().split())
A_list = list(map(int, input().split()))
A_list.sort()
A_diff = []

if A_list == []:
    print(1)
    exit()

for i in range(0,len(A_list) + 1):
    if i == 0:
        A_diff.append(A_list[i] - 1)
    elif i == len(A_list):
        A_diff.append(N - A_list[i - 1])
    else:
        A_diff.append(A_list[i] - A_list[i - 1] - 1)
    
    if A_diff[-1] == 0:
        del A_diff[-1]

count = 0
if A_diff == []:
    print(count)
    exit()

A_min = min(A_diff)
for A in A_diff:
    count += math.ceil(A / A_min)

print(count)