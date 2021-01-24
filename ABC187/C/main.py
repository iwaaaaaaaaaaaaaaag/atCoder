import re

N = int(input())
S_lists = list(set(input() for i in range(N)))
a = set()
b = set()
for i in range(len(S_lists)):
    if re.search('^!',S_lists[i]):
        a.add(re.sub('^!','',S_lists[i]))
    else:
        b.add(S_lists[i])

a_and_b = list(a&b)
if a_and_b == []:
    print('satisfiable')
else:
    print(a_and_b[0])

