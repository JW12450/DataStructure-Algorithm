import sys

n = int(sys.stdin.readline())\

queue= []

for i in range(n):
    order = sys.stdin.readline().split()

    if order[0] == 'push':
        queue.append(order[1])
    elif order[0] == 'pop':
        if (len(queue) <= 0):
            print(-1)
        else:
            print(queue.pop(0))

    elif order[0] == 'front':
        if (len(queue) <= 0):
            print(-1)
        else:
            print(queue[0])

    elif order[0] == 'back':
        if (len(queue) <= 0):
            print(-1)
        else:
            print(queue[len(queue) -1])

    elif order[0] == 'size':
        print(len(queue))
        #print('check')
    else:
        if (len(queue) <= 0):
            print(1)
        else :
            print(0)