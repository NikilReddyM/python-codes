from itertools import groupby
for i in [(len(list(g)),int(k)) for k,g in groupby(input())]:
    print(i,end = ' ')