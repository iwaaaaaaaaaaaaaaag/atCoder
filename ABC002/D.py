# 1 <= N <= 12

# 1 <= N <= 12
N,M = map(int,input().split())
jinmyaku = [list(map(int,input().split())) for _ in range(M)]

ans = 1
# ビット探索
for i in range(1,2 ** N):
    target = []
    for j in range(N):
        if (i>>j)&1:
            target.append(j + 1)

    # 配列に対して全検索
    is_jinmyaku_expand = True
    for k in range(len(target) - 1 ):
        for l in range(k + 1, len(target)):
            if [target[k],target[l]] not in jinmyaku:
                is_jinmyaku_expand = False
                break
    
    # 全て含まれている場合
    if is_jinmyaku_expand:
        ans = max(ans,len(target))

print(ans)