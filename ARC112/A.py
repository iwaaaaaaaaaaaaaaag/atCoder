# L <= A,B,C <= R
T = int(input())
case_list = [list(map(int,input().split())) for _ in range(T)]

for case in case_list:
    if case[1] - case[0] < case[0]:
        print(0)
    else:
        n = (case[1] - case[0]) - case[0] + 1
        print(int(1/2 * n * (n + 1)))
    

