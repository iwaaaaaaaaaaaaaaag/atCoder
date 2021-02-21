S = str(input())

for i in range(len(S)):
    if i % 2 == 0: 
        if S[i].islower() == False:
            print('No')
            break
    else:
        if S[i].isupper() == False:
            print('No')
            break
else:
    print('Yes')
        