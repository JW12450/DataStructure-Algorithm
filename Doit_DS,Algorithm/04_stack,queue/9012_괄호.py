import sys

n = int(sys.stdin.readline())

def check():
    input = sys.stdin.readline()
    stack = []
    for i in range(len(input)-1):
        #print(stack)
        if (input[i] == "("):
            stack.append(input[i])
        else:
            try:
                stack.pop()
            except IndexError:
                return "NO"
    #print(len(stack))
    if (len(stack) == 0):
        return ('YES')
    else:
        return ("NO")

for _ in range(n):
    print(check())