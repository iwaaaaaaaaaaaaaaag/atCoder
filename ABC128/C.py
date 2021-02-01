N, M = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(M)]  #sの各要素のはじめはk
p = list(map(int, input().split()))
ans = 0

# 0をoffとして2進数でパターンを表現
for i in range(2 ** N): #bit探索
    ptn = bin(i)[2:].rjust(N, "0")
    print("スイッチのパターン:",ptn[0],ptn[1])
    light = True
    for j in range(M): #電球の数
        tmp = 0
        for n in range(1, s[j][0] + 1): #スイッチの数
            print("スイッチのインデックス:",s[j][n] - 1)
            if ptn[s[j][n] - 1] == "1":
                tmp += 1
        if tmp % 2 != p[j] % 2: #スイッチのオンの数を検査
            light = False
    if light:
        ans += 1

print(ans)