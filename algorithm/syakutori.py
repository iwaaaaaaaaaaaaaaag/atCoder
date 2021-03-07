n, k = map(int, input().split())
s = [int(input()) for _ in range(n)]

# 0が含まれる場合
if 0 in s: 
    ans = n
else:
    r, l = 0, 0 # 右端と左端のインデックス
    sum_s = 1 # 右端と左端に含まれる合計値
    ans = 0
    while r < n:
        # 右端を進めたときの積がK以下なら、右端を進める
        if sum_s * s[r] <= k:
            sum_s *= s[r]
            r += 1
            ans = max(ans, r - l)
        # 右端と左端を進める
        elif r == l:
            r += 1
            l += 1
        # 左端を進める
        else:
            sum_s //= s[l] # 左端を進めたときに取り除かれる要素を合計値からも取り除く
            l += 1
        # print('l={}, r={}, size={}, {}'.format(l, r, r - l, s[l:r]))
print(ans)