H = int(input())

count = 0
# rangeの範囲に注意する事！
for i in range(1, H+1):
    # 10進数
    if '7' in str(i):
        count += 1
        continue
    # 8進数
    elif '7' in str(oct(i)):
        count += 1
        continue

print(H - count)
