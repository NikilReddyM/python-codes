from collections import namedtuple
n = int(input())
sheet = namedtuple('sheet',input().split())
total = 0
for i in range(n):
    total += int(sheet(*input().split()).MARKS)
print("%.2f" % (total/n))