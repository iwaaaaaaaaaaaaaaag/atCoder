from decimal import Decimal

A,B = (Decimal(x) for x in input().split())

ans = int(A*B)

print(ans)
