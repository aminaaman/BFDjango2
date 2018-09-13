from itertools import groupby

n = input()
a = [list(g) for k, g in groupby(n)]

for i in a:
    print(tuple((len(i),int(i[0]))), end = ' ')
