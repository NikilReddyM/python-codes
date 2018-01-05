from itertools import groupby
for i in [(len(list(g)),k) for k,g in groupby(input())]:
    print(i,end = ' ')