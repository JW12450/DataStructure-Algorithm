import sys

n = int(sys.stdin.readline())\

deque = []

for i in range(n):
    order = sys.stdin.readline().split()

    if order[0] == 'push_front':
        deque.insert(0, order[1])
    elif order[0] == 'push_back':
        deque.append(order[1])
    elif order[0] == 'front':
        if (len(deque) <= 0):
            print(-1)
        else:
            print(deque[0])
    elif order[0] == 'back':
        if (len(deque) <= 0):
            print(-1)
        else:
            print(deque[len(deque) -1])

    elif order[0] == 'pop_front':
        if (len(deque) <= 0):
            print(-1)
        else:
            print(deque.pop(0))
    elif order[0] == 'pop_back':
        if (len(deque) <= 0):
            print(-1)
        else:
            print(deque.pop(len(deque)-1))

    elif order[0] == 'size':
        print(len(deque))

    else:
        if (len(deque) <= 0):
            print(1)
        else :
            print(0)