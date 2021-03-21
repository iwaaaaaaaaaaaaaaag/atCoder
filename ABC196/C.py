N = str(input())

ans = 0
if len(N) == 1: # 一桁の場合は0を出力
    pass
elif len(N) % 2 == 1: # 桁数が奇数の場合
    for i in range(2,len(N),2):
        if i == 2:
            ans += 9
        else:
            num = i / 2
            ans += 9 * 10**(num - 1)
elif len(N) % 2 == 0: # 桁数が偶数の場合
    for i in range(0,len(N)+1,2):
        if i == 2 and len(N) != 2:
            ans += 9
        elif i != len(N):
            num = i / 2
            ans += 9 * 10**(num - 1)
        else:
            for j in range(10**(len(N) // 2 - 1),10**(len(N) // 2)): # ここだけ実装すればよかったっぽい。。。
                tmp = int(str(j) + str(j))
                if tmp <= int(N):
                    ans +=1
                else:
                    break

print(int(ans))
