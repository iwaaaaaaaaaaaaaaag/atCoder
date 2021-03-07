lists = list(map(int,input().split()))
for i in range(len(lists)):
    if lists[i] == 0:
        print(i + 1)

