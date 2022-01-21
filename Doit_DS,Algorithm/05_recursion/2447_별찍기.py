import sys, math

n = int(sys.stdin.readline())

def recur_star(n):
    if n == 1:
        return ['*']


    stars = recur_star(n//3)
    result = []
    #print(stars)
    for star in stars:
        result.append(star * 3)
    for star in stars:
        result.append(star + " "*(n//3) + star)
    for star in stars:
        result.append(star*3)
    #print(result)
    return result

print("\n".join(recur_star(n)))