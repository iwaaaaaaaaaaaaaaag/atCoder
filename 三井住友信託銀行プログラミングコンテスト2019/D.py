# 方針
# PIN番号の全通り(10*10*10)に対して、SのPINとして存在するかを確認する
N = int(input())
S = str(input())

ans = 0
for i in range(10):
    first_PIN_index = S.find(str(i))
    if first_PIN_index != -1:
        for j in range(10): 
            second_PIN_index = S.find(str(j),first_PIN_index + 1) 
            if second_PIN_index != -1:
                for k in range(10):
                    third_PIN_index = S.find(str(k),second_PIN_index + 1)
                    if third_PIN_index != -1:
                        ans += 1

print(ans)
