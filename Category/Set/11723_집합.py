import sys

n = int(sys.stdin.readline())\

s = set()

for i in range(n):
    order = sys.stdin.readline().split()

    if order[0] == 'add':
        if int(order[1]) not in s:
            s.add(int(order[1]))

    elif order[0] == 'remove':
        if int(order[1]) in s:
            s.remove(int(order[1]))

    elif order[0] == 'check':
        if int(order[1]) in s:
            print(1)
        else:
            print(0)
    elif order[0] == 'toggle':
        if int(order[1]) in s:
            s.remove(int(order[1]))
        else:
            s.add(int(order[1]))
    elif order[0] == 'all':
        for i in range(1, 21):
            if i not in s:
                s.add(i)
    else:
        s = set()

    #print(order)
    #print(s)
    #print()