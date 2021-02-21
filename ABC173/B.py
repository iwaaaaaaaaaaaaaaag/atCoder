import collections
N = int(input())

inp_list = list([input() for _ in range(N)])

print('AC x {cnt}'.format(cnt=collections.Counter(inp_list)['AC']))
print('WA x {cnt}'.format(cnt=collections.Counter(inp_list)['WA']))
print('TLE x {cnt}'.format(cnt=collections.Counter(inp_list)['TLE']))
print('RE x {cnt}'.format(cnt=collections.Counter(inp_list)['RE']))