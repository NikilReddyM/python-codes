from collections import defaultdict
n,m = map(int,input().split())
a=[]
b=[]
for i in range(n):
    a.append(input())
for i in range(m):
    b.append(input())
x= defaultdict(list)
for i in range(n):
    x[a[i]].append(i+1)
for i in b:
    j=x[i]
    if(j == []):
        print('-1',end='')
    else:
        for k in j:
            print(k,end=' ')
    print()