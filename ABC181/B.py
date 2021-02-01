N = int(input())
input_lists = [list(map(int, input().split())) for _ in range(N)]

S = 0
for input_list in input_lists:
    n = input_list[1] - input_list[0] + 1
    a = input_list[0]
    l = input_list[1]
    S +=n*(a+l)//2
print(S)