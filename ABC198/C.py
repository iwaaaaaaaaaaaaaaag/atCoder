import math
a,b = map(int,input().split())

# ポイント
# どれをループ対象にするか
# この場合はgcdの候補をループの対象とする 
# gcdの組み合わせは気にしなくて良い
# Bの商から、A-1の商を引いて2以上にするのがミソ
# Bの商から、Aの商を引いて1以上にするじゃだめ
ans = 1
for i in reversed(range(1,b)):
    if (b // i) - ((a-1) // i) >= 2:
        ans = i
        break
print(ans)
