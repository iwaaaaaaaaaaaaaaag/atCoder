# 自分で考えたやつ
'''
X,Y,Z = map(int,input().split())

for i in range(1000000,0,-1):
    if i * X < Y * Z:
        print(i)
        break
else:
    print(0)
'''

# 他の回答
X,Y,Z = map(int,input().split())
print((Y * Z - 1)//X)