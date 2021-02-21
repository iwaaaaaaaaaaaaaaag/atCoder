import copy
import collections

H, W, K = map(int,input().split())

c_list = [list(map(str,input())) for _ in range(H)]
ans = 0
for i in range(2 ** H):
    for j in range(2 ** W):
        cnt = 0
        tmp_list = copy.deepcopy(c_list)
        for ii in range(H):
            for jj in range(W):
                if bin(i >> ii&1) == bin(0b1) or bin(j >> jj&1) == bin(0b1):
                    tmp_list[ii][jj] = '*'
                if tmp_list[ii][jj] == '#':
                    cnt += 1
        if cnt == K:
            ans += 1
print(ans)
                    
                         

