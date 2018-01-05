from collections import OrderedDict
d=OrderedDict()
for i in range(int(input())):
    x=input().rpartition(' ')
    if x[0] in d:
        d[x[0]] += int(x[2])
    else:
        d[x[0]] = int(x[2])
for i in d:
    print(i,d[i])