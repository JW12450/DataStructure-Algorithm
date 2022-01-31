import sys


def check(num):
    size = len(num)
    stack = []
    for i in range(size//2):
        stack.append(num[i])

    #print(stack)
    if size % 2 == 1:
        for j in range(size//2+1, size):
            if num[j] != stack.pop():
                return 'no'
                break

        return 'yes'
    else:
        for j in range(size // 2, size):
            if num[j] != stack.pop():
                return 'no'
                break

        return 'yes'



while True:
    num = sys.stdin.readline().rstrip()
    if num == "0":
        break
    else:
        print(check(num))

