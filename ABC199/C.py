'''
# 方針
O(S)の各ループの中でT=2を行うとTLEになる
そこで、極力T=2をせずT=1のみでT=2を表現する

# ロジック
1.T=2の回数
  * T=2 -> T=2 は前後半の文字入れ替えは発生しない
  * T=2 -> T=2 -> T=2 は前後半の文字入れ替えは発生する
  → T=2が偶数回->前後半の文字入れ替えは発生しない
    T=2が奇数回->前後半の文字入れ替えは発生する
2.T=2 -> T=1 と T=1 -> T=2 が等しくなるための条件
  * T=2 -> T=1
    F	L	I	P スタート
    I	P	F	L T=2
    L	P	F	I T=1 1,4入れ替え
* T=1 -> T=2
    F	L	I	P スタート
    F	I	L	P T=1 2,3入れ替え
    L	P	F	I T=2
  →T=2 以降は文字入れ替えする位置を 
   N以下⇒ i + N
   Nより大きい⇒ i - N
   すればT=2を行った場合の文字位置を指定することが出来る

O(S)の各ループの中で2を行い、最後に1を行うことでT=2を最高1回実行に抑えることが出来る
'''
N = int(input())
S = list(input())
Q = int(input())
query_list = [list(map(int,input().split())) for _ in range(Q)]

swap_index = 0 
is_swap = False
for i in range(Q):
    if query_list[i][0] == 1:
        if is_swap:
            for j in range(1,3):
                if query_list[i][j] <= N :
                    query_list[i][j] += N
                else:
                    query_list[i][j] -= N
        S[query_list[i][2] - 1],S[query_list[i][1] - 1] = S[query_list[i][1] - 1],S[query_list[i][2] - 1]       
    elif query_list[i][0] == 2:
        is_swap = not is_swap 
else:
    if is_swap:
        S[N:2*N],S[0:N] = S[0:N],S[N:2*N]

print("".join(S))
