from collections import Counter
import operator
for i in sorted(sorted(Counter(input()).items()),key = operator.itemgetter(1),reverse = True)[:3]:
    print(i[0],i[1])