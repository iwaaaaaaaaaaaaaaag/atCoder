N, M = (int(x) for x in input().split())

light_bulb = [list(map(int, input().split())) for _ in range(M)]

p = list(map(int, input().split()))


ans = 0
for i in range(2 ** N):  # スイッチのbit検索
    switch_pattern = bin(i)[2:].rjust(N, '0')  # 2進数表現にして0詰め 0~k-1
    is_on = True 
    for j in range(M):  # 電球の数
        switch_tmp = 0
        for k in range(1, light_bulb[j][0]+1):  # 電球のスイッチ 1~k スイッチの数をカウント
            if switch_pattern[light_bulb[j][k] - 1] == '1':
                switch_tmp += 1
        if switch_tmp % 2 != p[j]:
            is_on = False
    if is_on:
        ans += 1
print(ans)

'''
<配列全てがtrueになる条件>
・初期値true 1つでもNGならfalse

<for文が多すぎてわけわからなくなる>
'''