import numpy as np

N = int(input())

'''
これだとLTE
A_list = list(map(int, input().split()))
sum = 0
for i in range(N):
    for j in range(i+1, N):
        sum += abs(A_list[i] - A_list[j])
        print(i,j)
print(sum)
'''

'''
配列をずらして計算
これでもLTE
A_list = np.array(list(map(int, input().split())))
A_list.sort()
sum = 0
for i in range(N):
    sum += (A_list[i:] - A_list[:N - i]).sum()
print(sum)
'''

'''
ポイント
* ロジックを簡単にするためにソートする。
* for文の中にfor文を使用しない
'''
A_list = list(map(int, input().split()))
A_list.sort()
sum = 0
ruiseki = 0
for i in range(N):
    sum += i * A_list[i]

for i in range(0,N - 1):
    ruiseki += A_list[i]
    sum -= ruiseki
print(sum)