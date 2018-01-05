from collections import OrderedDict
l=OrderedDict()
for i in range(int(input())):
    x=input()
    if x in l:
        l[x] += 1
    else:
        l[x] = 1
print(len(l))
for i in l:
    print(l[i],end=' ')