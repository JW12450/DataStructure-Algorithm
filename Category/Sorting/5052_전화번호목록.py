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


"""
#재풀이
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    num = [sys.stdin.readline().rstrip() for i in range(n)]
    num.sort()
    check = False
    for i in range(n-1):
        if num[i] == num[i+1][0:len(num[i])]:
            check = True

    if check:
        print("NO")
    else:
        print("YES")

"""