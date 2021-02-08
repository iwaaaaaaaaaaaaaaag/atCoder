N, X, T = map(int,input().split())
cnt = 1
while True:
    if cnt * X >= N :
        print(cnt * T)
        break
    cnt += 1