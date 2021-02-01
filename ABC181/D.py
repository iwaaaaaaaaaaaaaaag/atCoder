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