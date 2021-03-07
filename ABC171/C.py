n = int(input()) - 1 
alphabet = 'abcdefghijklmnopqrstuvwxyz'

ans = ''
while n >= 0:
    ans = alphabet[n % 26] + ans #0~25の範囲
    n //= 26
    n -= 1

print(ans)
