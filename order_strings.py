from operator import itemgetter
def values(n):
    l=[]
    for i in range(n):
        l.append(input().strip().split())
        l[i].append(i)
    return l

def orderStrings(l,k,r,c):
    if c == 'numeric':
        l = [[int(num) for num in sub] for sub in l]
    if r == 'true':
        l = sorted(l,key = itemgetter(k-1),reverse = True)
    else:
        l = sorted(l,key = itemgetter(k-1))
    return l

n=int(input())
l=values(n)
ref = l[:]
k,r,c = input().strip().split()
l = orderStrings(l,int(k),r,c)
el = len(l[0])-1
for i in range(n):
    id = l[i][el]
    for j in range(el):
        print(ref[id][j],end = ' ')
    print()
    
