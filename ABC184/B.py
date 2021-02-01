N, X = (int(x) for x in input().split())
S = input()
point = X
for s in S:
    if s == 'o':
        point += 1
    elif s == 'x':
        point += -1
        point = max(0,point)

print(point)