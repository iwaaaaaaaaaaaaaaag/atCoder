A, B = map(int,input().split())
x = (4*A - B)/2
y = (B-2*A)/2
if x == int(x) and y == int(y) and x >= 0 and y >= 0:
    print('Yes')
else:
    print('No')

