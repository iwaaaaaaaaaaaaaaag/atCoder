N = int(input())
A = list(map(int,input().split()))

ans = float('inf')
for bit in range(2 ** N): 
    temp_xor = 0
    temp_or = 0

    parent = [] # デバッグ用
    children = [] # デバッグ用
    for i in range(N):
        children.append(A[i])
        temp_or |= A[i]
        if (bit>>i) & 1: # bitが立っているとき
            parent.append(children)
            children = []
            temp_xor ^= temp_or
            temp_or = 0

    if (bit>>(N - 1)) & 1: # 最高位（一番右）のビットが立っているもののみ計算の対象
        ans = min(ans,temp_xor)
print(ans)