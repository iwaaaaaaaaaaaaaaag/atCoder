N, M, T = (int(x) for x in input().split())
N_max = N
B_init = 0
for i in range(M):
    A, B = (int(x) for x in input().split())
    N -= (A - B_init)
    if N <= 0:
        print('No')
        break
    N += (B - A)
    N = min(N, N_max)
    B_init = B
else:
    N -= (T - B_init)
    if N <= 0:
        print('No')
    else:
        print('Yes')
