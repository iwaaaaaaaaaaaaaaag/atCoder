N, X = map(int,input().split())
A_list = list(map(int,input().split()))

ans_list = [i for i in A_list if i != X]
print(*ans_list)