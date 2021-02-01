import itertools
N = int(input())
input_lists = [list(map(int, input().split())) for _ in range(N)]

comb_all = list(range(N))
comb = list(itertools.combinations(comb_all,3))

for i in range(len(comb)):
    check = []
    for j in range(1,len(comb[i])):
        x = input_lists[comb[i][j]][0] - input_lists[comb[i][0]][0]
        y = input_lists[comb[i][j]][1] - input_lists[comb[i][0]][1]
        if x == 0:
            check.append('infinity')
        else:
            check.append(y/x)
    if len(set(check)) == 1:
        print('Yes')
        break
else:
    print('No')
