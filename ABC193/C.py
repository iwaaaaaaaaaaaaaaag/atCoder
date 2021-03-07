import math
N = int(input())
left = 2
right = int(math.sqrt(10 ** 10)) +1
 
while left + 1 != right:
    middle = (left + right) //2
    if middle > N:
        right = middle
    else:
        left = middle
ruizyou = []
for i in range(2,left+1):
    exp = 2
    while i ** exp <= N:
       ruizyou.append(i ** exp)
       exp += 1 
ruizyou = list(set(ruizyou))
print(N - len(ruizyou))