from collections import deque
l=deque()
for i in range(int(input())):
    x=input().split()
    if x[0]== 'append':
        l.append(x[1])
    elif x[0] == 'appendleft':
        l.appendleft(x[1])
    elif x[0] == 'pop':
        l.pop()
    else:
        l.popleft()
print(" ".join(l))
    