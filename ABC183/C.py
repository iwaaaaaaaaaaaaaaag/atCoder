import itertools
N,K = (int(x) for x in input().split())

T_list = []
for i in range(N):
    T_list.append(list(map(int,input().split())))

kaizyou_list = list(itertools.permutations(range(1,N)))
count = 0
for kaizyou in kaizyou_list:
    start = 0
    kyori = 0
    for end in kaizyou:
        kyori += T_list[start][end]
        start = end
    else:
        kyori += T_list[start][0]

    if kyori == K:
        count += 1
print(count)