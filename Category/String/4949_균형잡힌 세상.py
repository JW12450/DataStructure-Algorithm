import sys

while True:
    sen = sys.stdin.readline().rstrip()
    if sen == ".":
        break

    sen = list(sen)
    check = []
    right = True
    for s in sen:
        if s == "(":
            check.append(s)
        elif s=="[":
            check.append(s)
        elif s == ")":
            if len(check) == 0:
                right = False
                break
            if check[-1] == "(":
                check.pop()
            else:
                right = False
                break
        elif s == "]":
            if len(check) == 0:
                right = False
                break
            if check[-1] == "[":
                check.pop()
            else:
                right = False
                break
    if len(check) > 0:
        right = False

    if right:
        print("yes")
    else:
        print("no")