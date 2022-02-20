alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']



def find(start, target):
    move = 0
    s = alp.index(start)
    t = alp.index(target)
    if t > s:
        move = min(t - s , s + 26 - t )
    elif t == s:
        move = 0
    else:
        move = min(t + 26 - s, s - t)

    return move


print(find('C','A'))
print(find('Z','A'))
print(find('Z','D'))
print(find('A','A'))

name = 'APPLE'
print(name[4])
print(find('A',name[1]))