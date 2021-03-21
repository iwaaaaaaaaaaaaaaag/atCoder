from itertools import chain

N = int(input())
lists = [list(map(int,input().split())) for _ in range(N)]

max_value = len(lists[0])

# DP
DP = [list([0] * N) for _ in range(max_value)]

for i in range(N):
    for j in range(max_value):
        if i == 0:
            DP[j][i] = lists[0][j]            
        else:
            tmp_db = []
            for k in range(max_value):
                if k != j:
                    tmp_db.append(DP[k][i - 1])
            DP[j][i] = lists[i][j] + max(tmp_db) 

print(max(chain(*DP)))