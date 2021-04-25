N = int(input())
X_C = [list(map(int,input().split())) for _ in range(N)]

print(X_C)

# DP
DP = [list([0] * 20) for _ in range(N)]

print(DP)
