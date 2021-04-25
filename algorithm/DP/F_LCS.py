S = str(input())
T = str(input())

if len(S) <= len(T):
    s = '-' + S
    t = '-' + T
else:
    s = '-' + T
    t = '-' + S
# 1つ前の文字が、どのインデックスで一致したか
DP = [[0] * (len(t)) for _ in range(len(s))]

# DP
for i in range(1,len(s)):
    for j in range(1,len(t)):
        if s[i] == t[j]:
            DP[i][j] = max(DP[i][j - 1],DP[i - 1][j]) + 1
        else:
            DP[i][j] = max(DP[i][j - 1],DP[i - 1][j])

print(DP)
print(DP[-1][-1])

# 復元
st = []
x = len(S)
y = len(T)
while x > 0 and y > 0:
    print(x,y)
    if DP[x][y] == DP[x-1][y]: x -= 1
    elif DP[x][y] == DP[x][y-1]: y -= 1
    else: 
        x -= 1
        y -= 1
        st += S[x]
print("".join(reversed(st)))