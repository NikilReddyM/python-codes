from itertools import combinations
l = int(input())
x= list(combinations(''.join(input().split()),int(input())))
count = 0
for i in x:
    if 'a' in i:
        count  += 1
print("%.3f"%(count/len(x)))