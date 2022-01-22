import sys

n = int(sys.stdin.readline())

def arithmetic_sequence(n):
    count = 0

    for i in range(1,n+1):
        if (i < 100):
            count +=1
            continue

        array = []
        #print(i//10)
        for j in range(len(str(i))):
            #print(j)
            array.append(int(str(i)[j]))
        #print(array)

        check = True
        for j in range(len(str(i)) - 2):
            #print(j)
            if (array[j+1] - array[j]) != (array[j+2] - array[j+1]):
                check = False

        if check:
            count += 1

    return count

print(arithmetic_sequence(n))
