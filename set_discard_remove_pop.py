def operate(s,commands):
    for i in commands:
        if i[0] == 'pop':
            s.pop()
        elif i[0] == 'remove':
            s.remove(int(i[1]))
        else:
            s.discard(int(i[1]))
    print(sum(s))

n = int(input())
s = set(map(int, input().split()))
commands = []
for i in range(int(input())):
    commands.append(input().split())
operate(s,commands)

    