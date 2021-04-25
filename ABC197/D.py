import math

N = int(input())
x0,y0 = map(int,input().split())
xN_2,yN_2 = map(int,input().split())

center_x = (xN_2 - x0)/2 + x0
center_y = (yN_2 - y0)/2 + y0

offset_x0 = x0 - center_x
offset_y0 = y0 - center_y

kakudo = 360/N
x1 = offset_x0*round(math.cos(math.radians(kakudo)),11) - offset_y0*round(math.sin(math.radians(kakudo)),11) + center_x 
y1 = offset_x0*round(math.sin(math.radians(kakudo)),11) + offset_y0*round(math.cos(math.radians(kakudo)),11) + center_y
print(x1,y1)
