X =str(input())

ans = ""
for x in X:
    if x == '.':
        break
    else:
        ans += x

print(ans)
