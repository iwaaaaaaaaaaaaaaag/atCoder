X,N = map(int,input().split())
p_list = list(map(int,input().split()))
p_list.sort()
i = 0
while True:
    if X - i not in p_list:
        print(X - i)
        break
    elif X + i not in p_list:
        print(X + i)
        break
    else:
        i += 1
