def operation(a,x,b):
    if x[0] == 'intersection_update':
        a.intersection_update(b)
    elif x[0] == 'update':
        a.update(b)
    elif x[0] == 'symmetric_difference_update':
        a.symmetric_difference_update(b)
    else:
        a.difference_update(b)
    
    
    
n = input()
a = set(input().split())
m = int(input())
for i in range(m):
    x = input().split()
    b = set(input().split())
    operation(a,x,b)
print(sum(a))