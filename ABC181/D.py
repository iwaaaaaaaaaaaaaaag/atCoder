'''
下1桁:8で割り切れる
下2桁:8で割り切れる
下3桁:8で割り切れる
下4桁:下3桁が8で割り切れる
下5桁:下3桁が8で割り切れる
下6桁:下3桁が8で割り切れる

考え方
・3桁までの8で割り切れる数字を配列で取得
・counterで各桁の数を取得
・Sの各桁の数が上記のもの以上だった場合8で割り切れることになる

'''


from collections import Counter

def check():
    S = str(input())
    # 1桁のチェック
    if len(S) <=2 and int(S) % 8 == 0:
        return True
    # 2桁のチェック
    elif len(S) == 2 and int(S[-1] + S[-2])%8 == 0:
        return True

    # 3桁以上のチェック
    for i in range(104, 1001, 8):
        if Counter(str(i)) - Counter(S) == Counter():
            return True
    return False
if check():
    print('Yes')
else:
    print('No')

'''
#順列で解く方法は時間がかかりすぎる
import sys
import itertools
S = list(str(input()))

cnt = 0
for s in S:
    if int(s) %2 == 1:
        cnt +=1
if cnt == len(S):
    print('No')
    sys.exit()

p_list = list(itertools.permutations(S))
for p in p_list:
    num = int("".join(p))
    if num %8 == 0:
        print('Yes')
        break
else:
    print('No')
'''
