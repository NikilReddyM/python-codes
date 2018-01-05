from collections import Counter
nshoes=input()
shoesizes = Counter(input().split())
ncust = int(input())
earned = 0
for i in range(ncust):
    size,cost = input().split()
    if size in shoesizes :
        earned += int(cost)
        shoesizes[size] -= 1
        if shoesizes[size] == 0:
            del(shoesizes[size])
print(earned)