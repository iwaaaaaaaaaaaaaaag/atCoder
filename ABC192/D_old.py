X = int(input())
M = int(input())


ans = 0
n = list(map(str,str(X)))
max_value = int(max(n)) + 1


while True: 
    tmp = 0
    if len(n) == 1:
        ans = 1
        break
    else:
        for i in range(len(n)):
            tmp += int(n[i]) * max_value**(len(n)-1-i) 

    if tmp <= M:
        ans += 1
    else:
        break
    max_value += 1

print(ans)

