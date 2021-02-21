K = int(input())

# 1 * 7
# 2 -> x
# 3 * 9
# 4 -> x
# 5 -> x
# 6 -> x
# 7 * 1
# 8 -> x
# 9 * 3 

if K % 2 == 0:
    print(-1)
    exit()
elif K % 5 == 0:
    print(-1)
    exit()

seven = 0
ans = 0
for i in range(1,K + 1):
    ans = (10*ans + 7)%K
    if ans == 0:
        print(i)
        break
