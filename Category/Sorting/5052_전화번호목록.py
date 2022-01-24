import sys

t = int(sys.stdin.readline())

def phone_num_check():
    n = int(sys.stdin.readline())
    array = []
    for i in range(n):
        array.append(sys.stdin.readline(). rstrip())

    array.sort()
    for i in range(n-1):
        length = len(array[i])
        if (array[i] == array[i+1][0:length]):
            return "NO"

    return "YES"

for i in range(t):
    print(phone_num_check())