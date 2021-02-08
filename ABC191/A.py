V,T,S,D = map(int,input().split())

#zikan = D / V
if T * V <= D and D <= S * V:
    print('No')
else:
    print('Yes')

