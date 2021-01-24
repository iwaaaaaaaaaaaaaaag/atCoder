N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
a_max = 0

for ai, bi in zip(A, B):
    a_max = max(a_max, ai)
    ans = max(ans, a_max * bi)
    print(ans)

