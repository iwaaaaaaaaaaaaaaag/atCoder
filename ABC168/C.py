import math
from decimal import *

A,B,H,M = list(map(int,input().split()))
# 時針
# 短針
# 1分でそれぞれどれくらい動く？
minute = H * 60 + M

cos_C = math.cos(Decimal((minute/60*2*math.pi - minute/(12*60)*2*math.pi)))
C =  math.sqrt((Decimal(A**2 + B**2 -2*A*B*cos_C)))
print(C)

