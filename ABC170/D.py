import math

N = int(input())
lists = list(map(int,input().split()))
lists.sort(reverse=True)
list_set = set(lists)
ans = 0
for i in range(N):
    divisors = []    
    for j in range(2,int(math.sqrt(lists[i])) + 1):
        if lists[i] % j == 0:
            divisors.append(lists[i] // j)
            divisors.append(j)
    if len(list_set&set(divisors)) > 0:
        ans +=1

if ans == 0:
    print(0)
else:
    print(N - ans)