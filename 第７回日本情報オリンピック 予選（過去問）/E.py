import math
import copy
R,C = map(int,input().split())
senbei_base = [list(map(int,input().split())) for _ in range(R)]

ans = 0
for i in range(2 ** R):
    senbei = copy.deepcopy(senbei_base) 
    for j in range(R): # 行についてビット探索
        if (i>>j)&1: # ひっくり返す
            for k in range(C):
                if senbei[j][k] == 0:
                    senbei[j][k] = 1
                else:
                    senbei[j][k] = 0

    goukei = 0 # 0の数をカウント
    for j in range(C):
        zero_cnt = 0 # 各列の0の数をカウント
        for k in range(R):
            if senbei[k][j] == 0:
                zero_cnt += 1
        if zero_cnt >= math.ceil(R/2):  
            goukei += zero_cnt
        else: # ひっくり返す
            goukei += R - zero_cnt
    ans = max(ans,goukei)

print(ans)