# 問題をいくつかの簡単で小さな問題に分割
# それぞれの問題の計算結果を表に記録
# 同じ問題に対しては表から計算結果を参照する

N = int(input())
fib_list = [0] * (N+1)
fib_list[0] = fib_list[1] = 1  
print(fib_list)

for i in range(2,N + 1):
    fib_list[i] = fib_list[i - 1] + fib_list[i - 2]

print(fib_list) 
    