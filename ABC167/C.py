N,M,X = map(int,input().split())

lists = [list(map(int,input().split())) for _ in range(N) ]

#ビット探索
bit_lists = []
for i in range(2**N):
    tmp = [0]*N
    for j in range(N):
        if (i>>j)&1 == 1:     
            tmp[j] = 1
    bit_lists.append(tmp)

SUM_VALUE = 99999999999999999999999
sum_value = SUM_VALUE
for bit_list in bit_lists:
    rikaido = [0] * M
    for i in range(M):
        rikaido_tmp = 0
        sum_value_tmp = 0
        for j in range(N):
            if bit_list[j] == 1:
               rikaido_tmp += lists[j][i+1]
               sum_value_tmp += lists[j][0]
        rikaido[i] = rikaido_tmp
    
    if all(r >= X for r in rikaido):
        sum_value = min(sum_value,sum_value_tmp)

if sum_value == SUM_VALUE:
    print(-1)
else:
    print(sum_value)