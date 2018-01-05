from itertools import product
l,m = map(int,input().split())
x=[]
for i in range(l):
    x.append(set(map(int,input().split()[1:])))
x=list(product(*x))
for i in range(len(x)):
    x[i] = sum(map(lambda x:x**2 , x[i]))%m
print(max(x))