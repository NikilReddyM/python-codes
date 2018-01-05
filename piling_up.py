from collections import deque
def pileup():
    d = deque(map(int,input().split()))
    b=d[0]
    for i in range(len(d)):
        if d[0]>=d[len(d)-1]:
            x=d.popleft()
            if b<x:
                return('No')
            b=x
        else:
            x=d.pop()
            if b<x:
                return('No')
            b=x
    return('Yes')

testcases = int(input())
for i in range(testcases):
    print(pileup())