start = list(map(int, input().split()))
end = list(map(int, input().split()))
r1 = start[0]
c1 = start[1]
r2 = end[0]
c2 = end[1]

if (r1 == r2) and (c1 == c2):
    print(0)
elif (r1 + c1 == r2 + c2) or (r1 - c1 == r2 - c2) or (abs(r2 - r1) + abs(c2 - c1) <= 3):
    print(1)
elif (abs(r2 - r1) + abs(c2 - c1) <= 6) or ((abs(r2 - r1) + abs(c2 - c1))%2 == 0) or (abs(r2 - r1 + c2 - c1) <= 3) or (abs(r1 - r2 - c1 + c2 ) <= 3):
    print(2)
else:
    print(3)
    
    
#反省点
#数式を複雑にしすぎた
