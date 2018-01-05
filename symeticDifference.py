def symmetric_difference(a,b):
    return list(a.union(b)-a.intersection(b))
    
n = int(input())
a=set(map(int,input().split()))
m = int(input())
b=set(map(int,input().split()))
lst = sorted(symmetric_difference(a,b))
for i in lst:
    print(i)